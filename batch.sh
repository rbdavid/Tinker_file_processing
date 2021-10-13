#!/bin/bash
#SBATCH -A bip198
#SBATCH -p batch
#SBATCH -t 6:00:00
#SBATCH -N 1
#SBATCH -J OFA
#SBATCH -o ./analysis.out
#SBATCH -e ./analysis.err

# this chunk of code below is pulled from my .bashrc after initializing the conda install
# >>> conda initialize >>>
# !! Contents within this block are managed by 'conda init' !!
__conda_setup="$('/where/ever/your/conda/environment/is/installed' 'shell.bash' 'hook' 2> /dev/null)"
if [ $? -eq 0 ]; then
    eval "$__conda_setup"
else
    if [ -f "/ccs/home/davidsonrb/Apps/miniconda3_ANDES/etc/profile.d/conda.sh" ]; then
        . "/ccs/home/davidsonrb/Apps/miniconda3_ANDES/etc/profile.d/conda.sh"
    else
        export PATH="/ccs/home/davidsonrb/Apps/miniconda3_ANDES/bin:$PATH"
    fi
fi
unset __conda_setup

# <<< conda initialize <<<
conda activate OpenFold-amber

time python3 write_dcd.py reps_160_k_50.00_run_051_sim.arc
time python3 analyze_refinement.py reps_160_k_50.00_run_051_sim.pdb traj.dcd /gpfs/alpine/bip198/proj-shared/ForRuss_1ubq_model_amoeba_traj/reps_160_k_50.00_run_051_sim.pdb /gpfs/alpine/bip198/proj-shared/ForRuss_1ubq_xtal_amoeba_traj/1ubq_sim.pdb

