# Tinker_file_processing
Repository for files used to post-process and analyze Tinker simulations.

### Installing CONDA environment on ANDES
```bash
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
# Install miniconda; initialize the miniconda install within your shell during installation.
bash Miniconda3-latest-Linux-x86_64.sh
# Add conda-forge to the channel list (it may already be present, but worth checking). 
conda config --add channels conda-forge
# Update to conda-forge versions of packages
conda update --yes --all
# Create a new conda environment named Tinker_env
conda create -n Tinker_env python==3.8
# Activate the Tinker_env environment
conda activate Tinker_env
# Install MDAnalysis
conda install MDAnalysis
```




