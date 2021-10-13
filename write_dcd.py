
# usage: python3 write_dcd.py example_traj_file.arc

import sys
import MDAnalysis
import warnings

traj_file = sys.argv[1] # read in a Tinker .arc file

with warnings.catch_warnings():
    warnings.simplefilter('ignore',UserWarning)
    u = MDAnalysis.Universe(traj_file)
    all_ = u.select_atoms('all')
    with MDAnalysis.Writer('traj.dcd',all_.n_atoms) as W:
        for ts in u.trajectory:
            W.write(all_)
    
