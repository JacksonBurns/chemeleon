#!/bin/bash -l
echo 'date: ' $(date)
conda activate chemprop

results_dir="results"
data_path="/home/akshatz/bond_order_free/pcba_random_nan/dataset/pcba_random_nan_data_filtered.csv"
splits_path="/home/akshatz/bond_order_free/pcba_random_nan/dataset/splits_filtered.json"

chemprop train \
-t classification \
--data-path $data_path \
--splits-file $splits_path \
--num-workers 20 \
--epochs 50 \
--pytorch-seed 42 \
--save-dir $results_dir \
--ensemble-size 5 \
--from-foundation chemeleon \
--accelerator gpu \
--devices "1," \