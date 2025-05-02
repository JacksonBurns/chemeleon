conda env create --name minimol 'python==3.10.*'
pip install 'torch==2.6.0' 'numpy<2'
pip install pyg_lib torch_scatter torch_sparse torch_cluster torch_spline_conv -f https://data.pyg.org/whl/torch-2.6.0+cu124.html
pip install minimol 'torch==2.6.0' 'numpy<2' 'scipy==1.12.*' # force minimol to respect the installed version of pytorch and numpy
pip install polaris-lib
pip install 'scipy==1.12.*'
