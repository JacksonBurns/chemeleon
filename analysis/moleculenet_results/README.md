# MoleculeNet Benchmarks

This folder contains all scripts required to run the benchmarks using **Chemprop** both with and without **CheMeleon** initialization. Chemprop 2.2.0 or newer is required.

All datasets used in this study can be downloaded from [Zenodo](https://doi.org/10.5281/zenodo.8174267).  
You may either manually download and extract `data.tar.gz`, or use the following commands:

```
wget https://zenodo.org/records/10078142/files/data.tar.gz
tar -xzvf data.tar.gz
```

Each benchmark can be executed individually by running one of the shell scripts in the `scripts` directory.  
For example, to run the `uv_vis` benchmark, first activate your Chemprop environment as described in the [Chemprop repository](https://github.com/chemprop/chemprop), then run:

```
cd scripts/chemeleon
./uv_vis_script.sh
```

This will train Chemprop models with CheMeleon initialization and generate a results folder, which includes model checkpoints and test set predictions.

The following benchmark tasks are supported:

- `hiv`: HIV replication inhibition (MoleculeNet + OGB) with scaffold splits  
- `pcba_random`: Biological activity (MoleculeNet) with random splits  
- `pcba_random_nans`: Same as above, with missing targets retained (for OGB comparability)  
- `pcba_scaffold`: Biological activity (MoleculeNet + OGB) with scaffold splits  
- `qm9_multitask`: DFT properties (MoleculeNet + OGB), trained as a multi-task model  
- `qm9_u0`: Single-task training on QM9 U0 target  
- `qm9_gap`: Single-task training on QM9 HOMO-LUMO gap  
- `sampl`: Water-octanol partition coefficients (SAMPL6, 7, 9)   
- `multi_molecule`: UV/Vis peak wavelengths in multiple solvents  
- `pcqm4mv2`: HOMO-LUMO gap prediction for PCQM4Mv2 molecules  

**Results Summary**

After running the benchmarks, summary markdown files are generated:
- `CheMeleon.md`: Contains results/metrics for all datasets using Chemprop with CheMeleon initialization.
- `ChemProp.md`: Contains results/metrics for all datasets using Chemprop without CheMeleon initialization.

These files provide a comprehensive overview of model performance across all tasks.

**Note**

A small number of invalid SMILES were found in the original benchmark datasets.  
We provide a filtering notebook (`filtering_invalid_smiles.ipynb`) to remove them prior to training.

While these represent a negligible fraction of the data and typically have minimal impact on performance,  
we ensure that only valid SMILES are used in all evaluations.
