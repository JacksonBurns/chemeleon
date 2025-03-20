"""
features.py

Calculates the mordred descriptors for a file of SMILES strings, writes them
as float32 to a zarr file
"""

import sys

import numpy as np
from rdkit import rdBase
from mordred import Calculator, descriptors
from rdkit import Chem
from tqdm import tqdm
import zarr

calc = Calculator(descriptors, ignore_3D=True)
calc.config(timeout=60)

n_features = len(calc)

blocker = rdBase.BlockLogs()
try:
    smiles_file = sys.argv[1]
    out_file = sys.argv[2]
except:
    print("Usage: python features.py SMILES_FILE OUTPUT_PATH")
    exit(1)

with open(smiles_file, "r") as file:
    smiles = [i.strip() for i in file.readlines()]

mols = list(filter(lambda m: m is not None, map(Chem.MolFromSmiles, tqdm(smiles, desc="Generating RDKit mols"))))
for mol in mols:
    mol.SetProp("_Name", "")
n_mols = len(mols)

# Define array dimensions
shape = (n_mols, n_features)
dtype = np.float32

# Estimate chunk size for ~64MB chunks
# suggested here: https://github.com/zarr-developers/zarr-python/issues/86#issuecomment-254439393
bytes_per_value = np.dtype(dtype).itemsize
chunk_rows = (64 * 1024 * 1024) // (n_features * bytes_per_value)
chunk_shape = (chunk_rows, n_features)
print(f"Number of rows per chunk: {chunk_rows}")

# Create the dataset with compression and concurrency settings
z = zarr.create_array(
    store=out_file,
    shape=shape,
    chunks=chunk_shape,
    dtype=dtype,
    compressors=None,  # disable compression
)

i = 0
with tqdm(total=n_mols, desc="Calculating features") as pbar:
    while i < n_mols:
        batch = np.array(list(calc.map(mols[i:i+chunk_rows], quiet=True)), dtype=dtype)
        z[i:i+chunk_rows, :] = batch
        pbar.update(chunk_rows)
        i += chunk_rows
    batch = np.array(list(calc.map(mols[i-chunk_rows:n_mols], quiet=True)), dtype=dtype)
    z[i-chunk_rows:n_mols, :] = batch
    pbar.update(n_mols - (i-chunk_rows))
