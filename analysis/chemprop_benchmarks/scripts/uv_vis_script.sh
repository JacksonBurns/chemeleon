#!/bin/bash -l
echo 'date: ' $(date)
conda activate chemprop

results_dir="results"
data_path="/home/akshatz/bond_order_free/multi_molecule/dataset/mult_mol_data_filtered.csv"
splits_path="/home/akshatz/bond_order_free/multi_molecule/dataset/splits_filtered.json"

chemprop train \
-t regression \
-s smiles solvent \
--data-path $data_path \
--splits-file $splits_path \
--num-workers 20 \
--epochs 50 \
--pytorch-seed 42 \
--save-dir $results_dir \
--ensemble-size 5 \
--metrics mae r2 \
--from-foundation CheMeleon \
--accelerator gpu \
--devices 1 \