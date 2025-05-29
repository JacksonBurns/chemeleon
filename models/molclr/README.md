Environment setup instructions for training [MolCLR](https://github.com/yuyangw/MolCLR) models.

### Setup Instructions

```bash
# Create conda environment
conda create --name molclr python=3.7
conda activate molclr

# Install PyTorch & PyTorch Geometric
pip install torch==1.7.1+cu110 torchvision==0.8.2+cu110 -f https://download.pytorch.org/whl/torch_stable.html
pip install torch-geometric==1.6.3 torch-sparse==0.6.9 torch-scatter==2.0.6 -f https://pytorch-geometric.com/whl/torch-1.7.0+cu110.html

# Other dependencies
pip install PyYAML
conda install -c conda-forge rdkit=2020.09.1.0 tensorboard nvidia-apex

# Clone the MolCLR repo
git clone https://github.com/yuyangw/MolCLR.git
cd MolCLR
