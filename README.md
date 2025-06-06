# `CheMeleon`

![`CheMeleon` logo](./chemeleon_logo_with_background.png)

Supporting code for "Descriptor-based Foundation Models for Molecular Property Prediction".

To finetune your own models using `CheMeleon` simply install [ChemProp 2.2.0 or newer](https://chemprop.readthedocs.io/en/latest/installation.html) (i.e. `pip install 'chemprop>=2.2.0'`) and use the `--from-pretrained CheMeleon` flag in the Command Line Interface.
To finetune models from a Python script, see [`finetuning_demo.ipynb`](./finetuning_demo.ipynb).

The code in this repository is primarily intended to aid in reproducing the results of the original study, but it may also be used to train other foundation models or finetune on new targets.
It is laid out as follows:
 - `analysis` - Jupyter notebooks and their required input data (results from pretraining and finetuning) to generate the facts and figures referenced in the study
 - `models` - Python code for feature calculation, pretraining, and finetuning with each unique model sorted into its own subdirectory
 - `scripts` - convenience scripts used in the study to perform various tasks

See the [Usage](#usage) section for more detailed information.

## Installation

Installation should take less than ten minutes.
We suggest using `conda` to manage dependencies, though other solutions such as `venv` or `uv` may also work.
Python 3.11 was used for initial development, though version 3.12 and newer may also work.
Ubuntu 24 was used for initial development, though the required dependencies should be installable across all platforms.

The first sections below lay out the 'general' dependencies needed for each part of the code.
They are intended to only provide minimum package versions to avoid errors, allowing users to extend the code more easily by allowing for easy addition of other dependencies.
For exact versions used to generate the results of the initial study see [Exact Versions](#exact-versions).

To execute the respective part of the study one must create a virtual environment containing the listed dependencies.
Due to compatibility conflicts, three separate environments are needed - users wishing to execute only some subpart of the code can setup only the corresponding environments.

### Pretraining and Feature Calculation

To pretrain the ChemProp and MLP-PLR models and to calculate the Mordred features needed for this pretraining, the following dependencies are required:

```
numpy
rdkit
mordredcommunity
rdkit
tqdm
zarr>=3
torch
scikit-learn
fastprop>=1.1.1
lightning
chemprop>=2.1
rtdl_num_embeddings
optuna
astartes
```

### Finetuning and Analysis

For finetuning of all models (except minimol) and for analysis of the results, the following dependencies are required:

```
statsmodels
matplotlib
numpy
scipy
scikit_posthocs
seaborn
chemprop>=2.1
fastprop>=1.1.1
polaris-lib>=0.11.6
zarr<3
torch
transformers[torch]
pandas
scikit-learn
datasets
scikit-mol
ipykernel
```

One can further simplify this environment to perform just the finetuning or analysis by omitting the packages which are not `import`-ed at the top of the corresponding file the user wishes to execute, though this was not done in the original study.

### minimol

Due to installation difficulties, minimol has a separate set of dependencies which must be installed in their own environment separately from the other models' dependencies.
Additionally, minimol must be run with Python 3.10 specifically.

```bash
conda env create --name minimol 'python==3.10.*'
pip install 'torch==2.6.0' 'numpy<2'
pip install pyg_lib torch_scatter torch_sparse torch_cluster torch_spline_conv -f https://data.pyg.org/whl/torch-2.6.0+cu124.html
pip install minimol 'torch==2.6.0' 'numpy<2' 'scipy==1.12.*' # force minimol to respect the installed version of pytorch and numpy
pip install polaris-lib
pip install 'scipy==1.12.*'
```

### MolCLR

MolCLR has a distinct set of dependencies that must be installed in a separate environment. It specifically requires Python 3.7, which is incompatible with the Python ≥3.10 requirement of the Polaris benchmark suite (See the note below).

```bash
# Create a Python 3.7 conda environment
conda create --name molclr python=3.7
conda activate molclr

# Install PyTorch and PyTorch Geometric (CUDA 11.0)
pip install torch==1.7.1+cu110 torchvision==0.8.2+cu110 -f https://download.pytorch.org/whl/torch_stable.html
pip install torch-geometric==1.6.3 torch-sparse==0.6.9 torch-scatter==2.0.6 -f https://pytorch-geometric.com/whl/torch-1.7.0+cu110.html

# Additional dependencies
pip install PyYAML
conda install -c conda-forge rdkit=2020.09.1.0 tensorboard nvidia-apex

# Clone the MolCLR repository
git clone https://github.com/yuyangw/MolCLR.git
cd MolCLR
```

**Note:** Due to the Python version mismatch, the full pipeline is split across three stages:

1. **Benchmark Preparation** (Python ≥3.10):  
   Run `create_benchmark_csv.py` to convert Polaris datasets into train/test CSVs and save accompanying metadata.

2. **MolCLR Training** (Python 3.7):  
   Use `train_models_polaris.py` inside the `molclr` environment to train models and generate test predictions.

3. **Evaluation** (Python ≥3.10):  
   Execute `evaluate_polaris.py` to compute final evaluation metrics and summarize the results in a markdown report.

### Exact Versions

For finetuning and data analysis:

```
absl-py==2.2.0
accelerate==1.6.0
aimsim_core==2.2.2
aiohappyeyeballs==2.6.1
aiohttp==3.11.14
aiosignal==1.3.2
annotated-types==0.7.0
anyio==4.9.0
asciitree==0.3.3
astartes==1.3.0
asttokens==3.0.0
attrs==25.3.0
Authlib==1.5.1
autorank==1.2.1
baycomp==1.0.3
biotite==1.2.0
biotraj==1.2.2
boto3==1.35.99
botocore==1.35.99
certifi==2025.1.31
cffi==1.17.1
charset-normalizer==3.4.1
chemprop==2.1.2
click==8.1.8
comm==0.2.2
ConfigArgParse==1.7
contourpy==1.3.1
cryptography==44.0.2
cycler==0.12.1
datamol==0.12.5
datasets==3.5.0
debugpy==1.8.13
decorator==5.2.1
Deprecated==1.2.18
descriptastorus==2.8.0
dill==0.3.8
executing==2.2.0
fasteners==0.19
fastpdb==1.3.1
fastprop==1.1.1
filelock==3.18.0
fonttools==4.56.0
frozenlist==1.5.0
fsspec==2024.12.0
grpcio==1.71.0
h11==0.14.0
httpcore==1.0.7
httpx==0.28.1
huggingface-hub==0.30.2
idna==3.10
importlib_resources==6.5.2
ipykernel==6.29.5
ipython==9.0.2
ipython_pygments_lexers==1.1.1
jedi==0.19.2
Jinja2==3.1.6
jmespath==1.0.1
joblib==1.4.2
jupyter_client==8.6.3
jupyter_core==5.7.2
kiwisolver==1.4.8
lightning==2.5.1
lightning-utilities==0.14.2
loguru==0.7.3
lxml==5.3.1
Markdown==3.7
markdown-it-py==3.0.0
MarkupSafe==3.0.2
matplotlib==3.10.1
matplotlib-inline==0.1.7
mdurl==0.1.2
mhfp==1.9.6
mordredcommunity==2.0.6
mpmath==1.3.0
msgpack==1.1.0
multidict==6.2.0
multiprocess==0.70.16
nest-asyncio==1.6.0
networkx==3.4.2
numcodecs==0.15.1
numpy==1.26.4
nvidia-cublas-cu12==12.4.5.8
nvidia-cuda-cupti-cu12==12.4.127
nvidia-cuda-nvrtc-cu12==12.4.127
nvidia-cuda-runtime-cu12==12.4.127
nvidia-cudnn-cu12==9.1.0.70
nvidia-cufft-cu12==11.2.1.3
nvidia-curand-cu12==10.3.5.147
nvidia-cusolver-cu12==11.6.1.9
nvidia-cusparse-cu12==12.3.1.170
nvidia-cusparselt-cu12==0.6.2
nvidia-nccl-cu12==2.21.5
nvidia-nvjitlink-cu12==12.4.127
nvidia-nvtx-cu12==12.4.127
packaging==24.2
padelpy==0.1.16
pandas==2.2.3
pandas-flavor==0.6.0
parso==0.8.4
patsy==1.0.1
pexpect==4.9.0
pillow==11.1.0
pip==25.0.1
platformdirs==4.3.7
polaris-lib==0.11.10
polars==1.26.0
prompt_toolkit==3.0.50
propcache==0.3.0
protobuf==6.30.1
psutil==7.0.0
ptyprocess==0.7.0
pure_eval==0.2.3
pyarrow==17.0.0
pycparser==2.22
pydantic==2.10.6
pydantic_core==2.27.2
pydantic-settings==2.8.1
Pygments==2.19.1
pyparsing==3.2.2
pyroaring==1.0.0
python-dateutil==2.9.0.post0
python-dotenv==1.0.1
pytorch-lightning==2.5.1
pytz==2025.1
PyYAML==6.0.2
pyzmq==26.3.0
rdkit==2024.9.6
regex==2024.11.6
requests==2.32.3
rich==13.9.4
rtdl_num_embeddings==0.0.11
s3transfer==0.10.4
safetensors==0.5.3
scikit-learn==1.6.1
scikit-mol==0.6.0
scikit-posthocs==0.11.4
scipy==1.15.2
seaborn==0.13.2
selfies==2.2.0
setuptools==75.8.2
shellingham==1.5.4
six==1.17.0
sniffio==1.3.1
stack-data==0.6.3
statsmodels==0.14.4
sympy==1.13.1
tabulate==0.9.0
tensorboard==2.19.0
tensorboard-data-server==0.7.2
threadpoolctl==3.6.0
tokenizers==0.21.1
torch==2.6.0
torchmetrics==1.7.0
tornado==6.4.2
tqdm==4.67.1
traitlets==5.14.3
transformers==4.51.3
triton==3.2.0
typer==0.15.2
typing_extensions==4.12.2
tzdata==2025.2
urllib3==2.3.0
wcwidth==0.2.13
Werkzeug==3.1.3
wheel==0.45.1
wrapt==1.17.2
xarray==2025.3.1
xxhash==3.5.0
yarl==1.18.3
zarr==2.18.4
```

For feature calculation and pretraining:

```
absl-py==2.1.0
aimsim_core==2.2.2
aiohappyeyeballs==2.6.1
aiohttp==3.11.14
aiosignal==1.3.2
alembic==1.15.2
annotated-types==0.7.0
anyio==4.9.0
asciitree==0.3.3
astartes==1.3.0
attrs==25.3.0
Authlib==1.5.1
biotite==1.2.0
biotraj==1.2.2
boto3==1.35.99
botocore==1.35.99
certifi==2025.1.31
cffi==1.17.1
charset-normalizer==3.4.1
chemprop==2.1.2
click==8.1.8
colorlog==6.9.0
ConfigArgParse==1.7
contourpy==1.3.1
crc32c==2.7.1
cryptography==44.0.2
cycler==0.12.1
datamol==0.12.5
Deprecated==1.2.18
descriptastorus==2.8.0
dill==0.3.9
donfig==0.8.1.post1
fasteners==0.19
fastpdb==1.3.1
fastprop==1.1.1
filelock==3.18.0
fonttools==4.56.0
frozenlist==1.5.0
fsspec==2025.3.0
greenlet==3.1.1
grpcio==1.71.0
h11==0.14.0
httpcore==1.0.7
httpx==0.28.1
idna==3.10
importlib_resources==6.5.2
Jinja2==3.1.6
jmespath==1.0.1
joblib==1.4.2
jsonschema==4.23.0
jsonschema-specifications==2024.10.1
kiwisolver==1.4.8
lightning==2.5.0.post0
lightning-utilities==0.14.1
loguru==0.7.3
Mako==1.3.9
Markdown==3.7
markdown-it-py==3.0.0
MarkupSafe==3.0.2
matplotlib==3.10.1
mdurl==0.1.2
mhfp==1.9.6
mordredcommunity==2.0.6
mpmath==1.3.0
msgpack==1.1.0
multidict==6.2.0
multiprocess==0.70.17
networkx==3.4.2
numcodecs==0.15.1
numpy==1.26.4
nvidia-cublas-cu12==12.4.5.8
nvidia-cuda-cupti-cu12==12.4.127
nvidia-cuda-nvrtc-cu12==12.4.127
nvidia-cuda-runtime-cu12==12.4.127
nvidia-cudnn-cu12==9.1.0.70
nvidia-cufft-cu12==11.2.1.3
nvidia-curand-cu12==10.3.5.147
nvidia-cusolver-cu12==11.6.1.9
nvidia-cusparse-cu12==12.3.1.170
nvidia-cusparselt-cu12==0.6.2
nvidia-nccl-cu12==2.21.5
nvidia-nvjitlink-cu12==12.4.127
nvidia-nvtx-cu12==12.4.127
optuna==4.2.1
packaging==24.2
padelpy==0.1.16
pandas==2.2.3
pandas_flavor==0.7.0
pillow==11.1.0
pip==25.0
platformdirs==4.3.7
polars==1.25.2
propcache==0.3.0
protobuf==6.30.1
psutil==7.0.0
pyarrow==17.0.0
pycparser==2.22
pydantic==2.10.6
pydantic_core==2.27.2
pydantic-settings==2.8.1
Pygments==2.19.1
pyparsing==3.2.1
pyroaring==1.0.0
python-dateutil==2.9.0.post0
python-dotenv==1.0.1
pytorch-lightning==2.5.0.post0
pytz==2025.1
PyYAML==6.0.2
ray==2.44.1
rdkit==2024.9.6
referencing==0.36.2
requests==2.32.3
rich==13.9.4
rpds-py==0.24.0
rtdl_num_embeddings==0.0.11
s3transfer==0.10.4
scikit-learn==1.6.1
scipy==1.15.2
seaborn==0.13.2
selfies==2.2.0
setuptools==76.1.0
shellingham==1.5.4
six==1.17.0
sniffio==1.3.1
SQLAlchemy==2.0.40
sympy==1.13.1
tabulate==0.9.0
tensorboard==2.19.0
tensorboard-data-server==0.7.2
tensorboardX==2.6.2.2
threadpoolctl==3.6.0
torch==2.6.0
torchmetrics==1.6.3
tqdm==4.67.1
triton==3.2.0
typer==0.15.2
typing_extensions==4.12.2
tzdata==2025.1
urllib3==2.3.0
Werkzeug==3.1.3
wheel==0.45.1
wrapt==1.17.2
xarray==2025.3.1
yarl==1.18.3
zarr==3.0.6
```

For minimol:

```
aiobotocore==2.21.1
aiohappyeyeballs==2.6.1
aiohttp==3.11.18
aioitertools==0.12.0
aiosignal==1.3.2
annotated-types==0.7.0
antlr4-python3-runtime==4.9.3
anyio==4.9.0
asciitree==0.3.3
async-timeout==5.0.1
attrs==25.3.0
Authlib==1.5.2
biotite==1.2.0
biotraj==1.2.2
boto3==1.35.99
botocore==1.35.99
cachetools==5.5.2
certifi==2025.4.26
cffi==1.17.1
charset-normalizer==3.4.1
click==8.1.8
contourpy==1.3.2
cramjam==2.10.0
cryptography==44.0.2
cycler==0.12.1
datamol==0.12.5
decorator==5.2.1
docker-pycreds==0.4.0
exceptiongroup==1.2.2
fasteners==0.19
fastparquet==2024.11.0
fastpdb==1.3.2
filelock==3.18.0
fonttools==4.57.0
frozenlist==1.6.0
fsspec==2025.3.2
gcsfs==2025.3.2
gitdb==4.0.12
GitPython==3.1.44
google-api-core==2.25.0rc0
google-auth==2.39.0
google-auth-oauthlib==1.2.2
google-cloud-core==2.4.3
google-cloud-storage==3.1.0
google-crc32c==1.7.1
google-resumable-media==2.7.2
googleapis-common-protos==1.70.0
graphium==2.4.7
h11==0.16.0
httpcore==1.0.9
httpx==0.28.1
hydra-core==1.3.2
idna==3.10
importlib_resources==6.5.2
Jinja2==3.1.6
jmespath==1.0.1
joblib==1.4.2
kiwisolver==1.4.8
lightning==2.5.1.post0
lightning-utilities==0.14.3
littleutils==0.2.4
loguru==0.7.3
markdown-it-py==3.0.0
MarkupSafe==3.0.2
matplotlib==3.10.1
mdurl==0.1.2
minimol==1.3.5
mpmath==1.3.0
msgpack==1.1.0
multidict==6.4.3
mup==1.0.0
networkx==3.4.2
numcodecs==0.13.1
numpy==1.26.4
nvidia-cublas-cu12==12.4.5.8
nvidia-cuda-cupti-cu12==12.4.127
nvidia-cuda-nvrtc-cu12==12.4.127
nvidia-cuda-runtime-cu12==12.4.127
nvidia-cudnn-cu12==9.1.0.70
nvidia-cufft-cu12==11.2.1.3
nvidia-cufile-cu12==1.11.1.6
nvidia-curand-cu12==10.3.5.147
nvidia-cusolver-cu12==11.6.1.9
nvidia-cusparse-cu12==12.3.1.170
nvidia-cusparselt-cu12==0.6.2
nvidia-nccl-cu12==2.21.5
nvidia-nvjitlink-cu12==12.4.127
nvidia-nvtx-cu12==12.4.127
oauthlib==3.2.2
ogb==1.3.6
omegaconf==2.3.0
outdated==0.2.2
packaging==24.2
pandas==2.2.3
pillow==11.2.1
pip==25.1
platformdirs==4.3.7
polaris-lib==0.12.1
propcache==0.3.1
proto-plus==1.26.1
protobuf==6.30.2
psutil==7.0.0
pyarrow==17.0.0
pyasn1==0.6.1
pyasn1_modules==0.4.2
pycparser==2.22
pydantic==2.11.4
pydantic_core==2.33.2
pydantic-settings==2.9.1
pyg-lib==0.4.0+pt26cu124
Pygments==2.19.1
pyparsing==3.2.3
pyroaring==1.0.0
python-dateutil==2.9.0.post0
python-dotenv==1.1.0
pytorch-lightning==2.5.1.post0
pytz==2025.2
PyYAML==6.0.2
rdkit==2024.9.6
requests==2.32.3
requests-oauthlib==2.0.0
rich==14.0.0
rsa==4.9.1
s3fs==2025.3.2
s3transfer==0.10.4
scikit-learn==1.6.1
scipy==1.12.0
seaborn==0.13.2
selfies==2.2.0
sentry-sdk==2.27.0
setproctitle==1.3.6
setuptools==80.1.0
shellingham==1.5.4
six==1.17.0
smmap==5.0.2
sniffio==1.3.1
sympy==1.13.1
threadpoolctl==3.6.0
torch==2.6.0
torch_cluster==1.6.3+pt26cu124
torch-geometric==2.6.1
torch_scatter==2.1.2+pt26cu124
torch_sparse==0.6.18+pt26cu124
torch_spline_conv==1.2.2+pt26cu124
torchmetrics==0.10.3
torchvision==0.21.0
tqdm==4.67.1
triton==3.2.0
typer==0.15.3
typing_extensions==4.13.2
typing-inspection==0.4.0
tzdata==2025.2
urllib3==2.4.0
wandb==0.19.10
wheel==0.45.1
wrapt==1.17.2
yarl==1.20.0
zarr==2.18.3
```

## Usage

Every notebook in this repository can be executed by running all cells from the top within the appropriate environment.
Python scripts which take command line arguments to specify inputs and outputs will print their usage upon running `python <script_name>.py`.

Recreating the results of the original study requries significant computational resources.
Feature calculation for 1MM SMILES from PubChem took roughly 500 CPU hours.
Pretraining of the MLP-PLR took roughly 500 GPU hours and pretraining the `CheMeleon` model took about 1,000 GPU hours.
Finetuning a single `CheMeleon`-based model requires <<1 GPU hour, though running all finetuning for all models and all repeitions will take around 100 GPU hours.

Storage of all preatrining and finetuning model checkpoints requries 1+ terabytes of storage - for this reason, intermediate training checkpoints and finetuned models are _not_ retained during finetuning for this study.
This can be easily modified in the provided scripts to facilitate actual deployment and reuse of the finetuned models.
Storage of pretraining features requires ~40 GB of disk space.

### `analysis`

This directory contains Jupyter notebooks which perform the anslysis of modeling results as shown in the original study.
These may be run in VSCode or with whatever notebook application you prefer.
The input data needed to generate the results is saved in the corresponding `_results` subdirectory.
The outputs from running the notebooks, including both the generated figures and the collated results, and shown in the `cliffs` and `hsd` subdirectories.

### `models`

Within this directory there are subdictories for each of the models tested in the original study.
Each subdirectory contains, at minimum, an `evaluate.py` script that generates the results needed for analysis.
Some subdirectories contain additional files needed to pretrain models, where applicable, as well as model definitions and helper functions.
Where models can be pretrained, there is a `pretrain.py` script.

For each script, run `python <script_name>.py` to see the command line usage.

Also within this directory is the `features.py` Python script.
This script ingests a text file of only SMILES strings and emits a cleaned version of that list and a Zarr array of the corresponding molecular descriptors at the indicated location.

### `scripts`

This directory contains a few convenience scripts used in the oroginal study that others may find useful (execute them with `bash <script_name>.sh`):
 - `get_pubchem.sh` - downloads and converts the complete set of SMILES from PubChem and turns them into a `.smiles` file (i.e. a text file with only SMILES in it)
 - `gpus.sh` - adjusts power settings on our hardware to prevent crashes
 - `run_experiments.sh` - after manually performing pretraining, this script (with appropriately named model files provided) will execute all experiments performed in the original study
 - `start_screen.sh` - starts a GNU `screen` session for long-running commands
