"""
features.py

Calculates the mordred descriptors for a file of SMILES strings, writes them
as float32 to a zarr file
"""

import sys
from multiprocessing import Pool
import warnings

import numpy as np
from rdkit import rdBase
from mordred import Calculator, descriptors
from rdkit.Chem import MolFromSmiles, RemoveHs
from tqdm import tqdm
import zarr

warnings.filterwarnings('ignore', category=FutureWarning)


# convert to mols, filtering invalid
def _f(smi):
    mol = MolFromSmiles(smi)
    if mol is None:
        return False
    try:
        _ = RemoveHs(mol, updateExplicitCount=True)
    except:
        print("Skipping mol {smi} - failed RemoveHs")
        return False
    return True

# convert to mols
def _s(smi):
    return MolFromSmiles(smi)


if __name__ == "__main__":
    p = Pool(64)

    calc = Calculator(descriptors, ignore_3D=True)
    calc.config(timeout=1)

    n_features = len(calc)

    blocker = rdBase.BlockLogs()
    try:
        smiles_file = sys.argv[1]
        out_file = sys.argv[2]
    except:
        print("Usage: python features.py SMILES_FILE OUTPUT_PATH")
        exit(1)

    with open(smiles_file, "r") as file:
        smiles = [i.strip() for i in tqdm(file.readlines(), "Reading SMILES")]

    # monomethyl auristatin E (one of the largest small molecule drugs) has a SMILES string
    # with 143 characters - let's filter out anything much larger than that
    cutoff = 150
    smiles = list(filter(lambda s: len(s) < cutoff, tqdm(smiles, desc=f"Filtering SMILES > {cutoff} chars.")))

    # filter out mixtures
    smiles = list(filter(lambda s: "." not in s, tqdm(smiles, desc=f"Filtering mixture SMILES")))

    valid_mols = list(p.map(_f, tqdm(smiles, desc="Generating RDKit mols"), chunksize=1_024))

    smiles = [s for (s, v) in zip(smiles, valid_mols) if v]
    with open("cleaned_" + smiles_file, "w") as file:
        for smi in tqdm(smiles, desc="Writing cleaned SMILES"):
            file.write(smi + "\n")
    n_mols = len(smiles)

    # Define array dimensions
    shape = (n_mols, n_features)
    dtype = np.float32

    # Estimate chunk size for ~1MB chunks
    # other suggestions here: https://github.com/zarr-developers/zarr-python/issues/86#issuecomment-254439393
    bytes_per_value = np.dtype(dtype).itemsize
    chunk_rows = (1 * 1024 * 1024) // (n_features * bytes_per_value)
    chunk_shape = (chunk_rows, n_features)
    print(f"Number of rows per chunk: {chunk_rows}")

    # Create the dataset with compression and concurrency settings
    # z = zarr.create_array(
    #     store=out_file,
    #     shape=shape,
    #     chunks=chunk_shape,
    #     dtype=dtype,
    #     compressors=None,  # disable compression
    #     fill_value=np.nan,
    # )
    z = zarr.open_array(out_file)

    # restarting from previous - otherwise start at i = 0
    i = 7_680_096
    with tqdm(total=n_mols, desc="Calculating features") as pbar:
        while i < n_mols:
            mols = list(p.map(_s, smiles[i:i+chunk_rows], chunksize=chunk_rows // 64))
            for mol in mols:
                mol.SetProp("_Name", "")  # prevent mordred from doing this in a rather expensive way
            batch = calc.pandas(mols, quiet=True, nproc=64).fill_missing().to_numpy(dtype=np.float32)
            z[i:i+chunk_rows, :] = batch
            pbar.update(chunk_rows)
            i += chunk_rows
        mols = list(p.map(_s, smiles[i-chunk_rows:n_mols], chunksize=chunk_rows // 64))
        for mol in mols:
            mol.SetProp("_Name", "")  # prevent mordred from doing this in a rather expensive way
        batch = calc.pandas(mols, quiet=True, nproc=64).fill_missing().to_numpy(dtype=np.float32)
        z[i-chunk_rows:n_mols, :] = batch
        pbar.update(n_mols - (i-chunk_rows))
