#!/bin/bash -l
echo 'date: ' $(date)
conda activate chemprop

results_dir="results"
data_path="/home/akshatz/bond_order_free/hiv/dataset/hiv_data_filtered.csv"
splits_path="/home/akshatz/bond_order_free/hiv/dataset/splits_filtered.json"

chemprop train \
-t classification \
--data-path $data_path \
--splits-file $splits_path \
--num-workers 20 \
--epochs 50 \
--pytorch-seed 42 \
--save-dir $results_dir \
--ensemble-size 5 \
--accelerator gpu \
--devices 1 \