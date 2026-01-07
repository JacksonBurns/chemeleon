# Run the embedding analysis
set -e

N_JOBS=32 # set number of parallel jobs

REPO_ROOT="$( cd "$( dirname "${BASH_SOURCE[0]}" )/.." && pwd )"
EXPERIMENT_ROOT_DIR="${REPO_ROOT}/analysis/embedding_analysis"
SCRIPT_DIR=$EXPERIMENT_ROOT_DIR
CONFIG_DIR="${EXPERIMENT_ROOT_DIR}/config"


# 01 preprocess data
# python ${SCRIPT_DIR}/01_preprocess_data.py --n_jobs $N_JOBS

# 02 run clustering/splitting on pre-selected endpoints only
# python ${SCRIPT_DIR}/02_assign_groups.py --endpoint "${CONFIG_DIR}/endpoints.yaml" --n_groups 5 --n_jobs $N_JOBS

# 03 calculate descriptors
# python ${SCRIPT_DIR}/03_calc_descriptors.py --endpoint "${CONFIG_DIR}/endpoints.yaml" --n_jobs $N_JOBS --descriptor morgan
# python ${SCRIPT_DIR}/03_calc_descriptors.py --endpoint "${CONFIG_DIR}/endpoints.yaml" --n_jobs $N_JOBS --descriptor morgan_count
# python ${SCRIPT_DIR}/03_calc_descriptors.py --endpoint "${CONFIG_DIR}/endpoints.yaml" --n_jobs $N_JOBS --descriptor rdkit_physchem
# python ${SCRIPT_DIR}/03_calc_descriptors.py --endpoint "${CONFIG_DIR}/endpoints.yaml" --n_jobs $N_JOBS --descriptor mordred


# 04 compute embeddings on all data splits and all endpoints
CUDA_VISIBLE_DEVICES=0 python ${SCRIPT_DIR}/04_calc_embeddings.py --endpoint "${CONFIG_DIR}/endpoints.yaml" --n_jobs 2 --model-name chemeleon
CUDA_VISIBLE_DEVICES=0 python ${SCRIPT_DIR}/04_calc_embeddings.py --endpoint "${CONFIG_DIR}/endpoints.yaml" --n_jobs 2 --model-name chemprop
CUDA_VISIBLE_DEVICES=0 python ${SCRIPT_DIR}/04_calc_embeddings.py --endpoint "${CONFIG_DIR}/endpoints.yaml" --n_jobs 2 --model-name chemeleon_no_pretraining

# 05 KNN probing
python ${SCRIPT_DIR}/05_knn_probing.py --endpoint "${CONFIG_DIR}/endpoints.yaml" --n_jobs $N_JOBS