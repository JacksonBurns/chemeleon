#! /bin/bash
DESCRIPTOR_LIST="morgan morgan_count rdkit_physchem mordred"
MODEL_LIST="chemeleon_frozen chemprop chemprop_large chemeleon_finetuned"
n_jobs=-1
n_workers=2

python 01_preprocess_data.py --n_jobs $n_jobs

python 02_assign_groups.py --endpoint config/endpoints.yaml --n_groups 5 --n_jobs $n_jobs

for descriptor in $DESCRIPTOR_LIST; do
    python 03_calc_descriptors.py --endpoint config/endpoints.yaml --n_jobs $n_jobs --descriptor $descriptor
done

for model in $MODEL_LIST; do
    CUDA_VISIBLE_DEVICES=0 python 04_calc_embeddings.py --endpoint config/endpoints.yaml --model-name $model --n_workers $n_workers
done

python 05_knn_probing.py --endpoint config/endpoints.yaml --n_jobs $n_jobs