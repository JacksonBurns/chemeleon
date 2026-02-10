import numpy as np
import zarr
import torch
from tqdm import tqdm
from concurrent.futures import ProcessPoolExecutor, as_completed
import functools
import os

def combine_stats(stat_a, stat_b):
    """
    Merges two sets of Welford statistics (n, mean, M2) into one.
    This allows parallel computation of variance.
    """
    na, mean_a, m2_a = stat_a
    nb, mean_b, m2_b = stat_b
    
    # If one side has no data for a specific column, return the other
    # We handle this via masking below to support per-column counts
    
    n_combined = na + nb
    
    # Calculate delta
    delta = mean_b - mean_a
    
    # Combined mean
    # mean_new = mean_a + delta * nb / n_combined
    # Handle division by zero where n_combined is 0
    with np.errstate(divide='ignore', invalid='ignore'):
        mean_combined = mean_a + delta * (nb / n_combined)
        
        # Combined M2 (Sum of squares of differences from the mean)
        # M2 = M2a + M2b + delta^2 * (na * nb) / n_combined
        m2_combined = m2_a + m2_b + (delta ** 2) * (na * nb / n_combined)

    # Where n_combined is 0, everything should be 0 (or handled later)
    # Where only one side had data, we preserve that side's stats
    mask_a_only = (na > 0) & (nb == 0)
    mask_b_only = (nb > 0) & (na == 0)
    
    # Restore values where the other side was empty (fix NaNs from 0/0)
    mean_combined[mask_a_only] = mean_a[mask_a_only]
    m2_combined[mask_a_only] = m2_a[mask_a_only]
    
    mean_combined[mask_b_only] = mean_b[mask_b_only]
    m2_combined[mask_b_only] = m2_b[mask_b_only]
    
    # Fill remaining NaNs (where both were 0) with 0
    mean_combined = np.nan_to_num(mean_combined, nan=0.0)
    m2_combined = np.nan_to_num(m2_combined, nan=0.0)

    return n_combined, mean_combined, m2_combined

def compute_chunk_stats(args):
    """
    Worker function to compute stats for a single chunk.
    Args:
        args: tuple of (zarr_path, start_row, end_row, dtype)
    """
    zarr_path, start, end, dtype = args
    
    # Open in read-only mode inside the process to avoid pickling locks
    # If passing a complex store, you might need to pass the store config instead of path
    z_array = zarr.open(zarr_path, mode='r')
    
    # Read chunk
    chunk = z_array[start:end].astype(dtype, copy=False)
    
    # Mask finite values
    finite = np.isfinite(chunk)
    bcount = finite.sum(axis=0)
    
    # If chunk has no valid data at all
    if not np.any(bcount):
        n_cols = z_array.shape[1]
        return (
            np.zeros(n_cols, dtype=np.int64), 
            np.zeros(n_cols, dtype=dtype), 
            np.zeros(n_cols, dtype=dtype)
        )

    # Compute local mean
    # Use 0.0 for non-finite to not affect sum, then divide by count
    chunk_sum = np.where(finite, chunk, 0.0).sum(axis=0)
    
    mean = np.zeros_like(chunk_sum)
    valid = bcount > 0
    mean[valid] = chunk_sum[valid] / bcount[valid]
    
    # Compute local M2 (sum of squared differences from the mean)
    # diff = x - mean
    diff = np.where(finite, chunk - mean, 0.0)
    m2 = (diff * diff).sum(axis=0)
    
    return bcount, mean, m2

def mean_std_zarr_parallel(
    zarr_path, 
    max_workers=None, 
    dtype=np.float64
):
    """
    Computes mean and std in parallel using ProcessPoolExecutor.
    """
    zarr_array = zarr.open(zarr_path, mode='r')
    n_rows, n_cols = zarr_array.shape
    chunk_rows = zarr_array.chunks[0]
    
    if max_workers is None:
        # Leave a couple of cores free for the system/coordinator
        max_workers = max(1, os.cpu_count() - 1)

    # Prepare tasks
    tasks = []
    for i in range(0, n_rows, chunk_rows):
        end = min(i + chunk_rows, n_rows)
        # We pass the path, not the object, to avoid pickling large Zarr objects
        tasks.append((zarr_path, i, end, dtype))

    print(f"Processing {len(tasks)} chunks with {max_workers} workers...")

    results = []
    with ProcessPoolExecutor(max_workers=max_workers) as executor:
        # Submit all tasks
        futures = [executor.submit(compute_chunk_stats, t) for t in tasks]
        
        # Gather results with progress bar
        for future in tqdm(as_completed(futures), total=len(futures), desc="Computing chunks"):
            results.append(future.result())

    print("Merging statistics...")
    
    # Reduce step: Combine all partial stats
    # Initialize accumulator with zeros
    total_stats = (
        np.zeros(n_cols, dtype=np.int64), 
        np.zeros(n_cols, dtype=dtype), 
        np.zeros(n_cols, dtype=dtype)
    )
    
    # Iteratively merge
    for part_stats in results:
        total_stats = combine_stats(total_stats, part_stats)
        
    final_count, final_mean, final_m2 = total_stats

    # Calculate final Std Dev
    variance = np.full(n_cols, np.nan, dtype=dtype)
    valid_final = final_count > 1
    
    # Variance = M2 / (n - 1) for sample variance
    variance[valid_final] = final_m2[valid_final] / (final_count[valid_final] - 1)
    std = np.sqrt(variance)

    return final_mean.astype(np.float32), std.astype(np.float32), final_count

if __name__ == "__main__":
    import sys
    from pathlib import Path
    
    try:
        input_path = Path(sys.argv[1])
    except:
        print("Usage: python script.py <zarr_path>")
        exit(1)
    
    if not input_path.exists():
        print(f"Error: {input_path} not found.")
        exit(1)

    mean, std, count = mean_std_zarr_parallel(input_path)
    
    print(f"Computed stats for {input_path.stem}:")
    print(f"  Count: {count.sum()} finite samples (aggregated)")
    print(f"  Mean (first 5): {mean[:5]}")
    print(f"  Std  (first 5): {std[:5]}")
    
    torch.save(mean, f"feature_means_cached_{input_path.stem}.pt")
    torch.save(std, f"feature_vars_cached_{input_path.stem}.pt")
