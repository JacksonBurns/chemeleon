# Chemprop Benchmarks with CheMeleon

This folder contains all scripts required to run the **Chemprop** benchmarks using **CheMeleon**.

All datasets used in this study can be downloaded from [Zenodo](https://doi.org/10.5281/zenodo.8174267).  
You may either manually download and extract `data.tar.gz`, or use the following commands:

```
wget https://zenodo.org/records/10078142/files/data.tar.gz
tar -xzvf data.tar.gz
```

Each benchmark can be executed individually by running one of the shell scripts in the `scripts` directory.  
For example, to run the `barriers_e2` benchmark, first activate your Chemprop environment as described in the [Chemprop repository](https://github.com/chemprop/chemprop), then run:

```
cd scripts
./barriers_e2.sh
```

This will train Chemprop models initialized with CheMeleon and generate the `results_barriers_e2` folder, which includes model checkpoints and test set predictions.

The following benchmark tasks are supported:

- `hiv`: HIV replication inhibition (MoleculeNet + OGB) with scaffold splits  
- `pcba_random`: Biological activity (MoleculeNet) with random splits  
- `pcba_random_nans`: Same as above, with missing targets retained (for OGB comparability)  
- `pcba_scaffold`: Biological activity (MoleculeNet + OGB) with scaffold splits  
- `qm9_multitask`: DFT properties (MoleculeNet + OGB), trained as a multi-task model  
- `qm9_u0`: Single-task training on QM9 U0 target  
- `qm9_gap`: Single-task training on QM9 HOMO-LUMO gap  
- `sampl`: Water-octanol partition coefficients (SAMPL6, 7, 9)  
- `barriers_e2`: Reaction barrier heights for E2 reactions  
- `barriers_sn2`: Reaction barrier heights for S<sub>N</sub>2 reactions  
- `barriers_cycloadd`: Reaction barrier heights for cycloadditions  
- `barriers_rdb7`: Reaction barriers in the RDB7 dataset  
- `barriers_rgd1`: Reaction barriers in the RGD1-CNHO dataset  
- `multi_molecule`: UV/Vis peak wavelengths in multiple solvents  
- `pcqm4mv2`: HOMO-LUMO gap prediction for PCQM4Mv2 molecules  

**Note**

A small number of invalid SMILES were found in the original benchmark datasets.  
We provide a filtering notebook (`filtering_invalid_smiles.ipynb`) to remove them prior to training.

While these represent a negligible fraction of the data and typically have minimal impact on performance,  
we ensure that only valid SMILES are used in all evaluations.
