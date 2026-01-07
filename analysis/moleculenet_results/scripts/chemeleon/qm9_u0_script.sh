#!/bin/bash -l
echo 'date: ' $(date)

results_dir="qm9_u0_results"
data_path="/home/akshatz/bond_order_free/qm9/dataset/qm9_data.csv"
splits_path="/home/akshatz/bond_order_free/qm9/dataset/splits.json"

chemprop train \
-t regression \
--data-path $data_path \
--splits-file $splits_path \
--num-workers 20 \
--epochs 50 \
--pytorch-seed 42 \
--accelerator gpu \
--devices "1," \
--save-dir $results_dir \
--ensemble-size 5 \
--metrics mae rmse \
--target-columns u0_atom \
--from-foundation chemeleon \