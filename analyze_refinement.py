
# usage: python3 analyze_refinement.py system_topology_file.[pdb,prmtop,etc] traj_file.dcd starting_structure.pdb xtal_structure.pdb 
# the last two arguments can be any two structures of the system of interest
# this is just a basic script to calculate RMSD using the full protein as the alignment landmark; most likely this is not what you want

import sys
import MDAnalysis
from MDAnalysis.analysis.align import *
import warnings

top_file  = sys.argv[1]
traj_file = sys.argv[2]
starting_structure = sys.argv[3]
xtal_structure = sys.argv[4]

with warnings.catch_warnings():
    warnings.simplefilter('ignore',UserWarning)
    u = MDAnalysis.Universe(top_file,traj_file)
    u_all = u.select_atoms('all')
    protein = u.select_atoms('protein')
    water = u.select_atoms('resname WAT')

    # rmsd of protein atoms referenced against OpenFold model structure
    ref1 = MDAnalysis.Universe(starting_structure)
    ref1_protein = ref1.select_atoms('protein')
    ref1_all = ref1.select_atoms('all')
    ref1_all.translate(-ref1_protein.center_of_mass())
    ref1_pos = ref1_protein.positions
    ref1_all.write('ref1.pdb')

    # rmsd of protein atoms referenced against Xtal structure
    ref2 = MDAnalysis.Universe(xtal_structure)
    ref2_protein = ref2.select_atoms('protein')
    ref2_all = ref2.select_atoms('all')
    ref2_all.translate(-ref2_protein.center_of_mass())
    ref2_pos = ref2_protein.positions
    ref2_all.write('ref2.pdb')

    # run through trajectory calculating RMSDs against both references
    with open('rmsd_results.dat','w') as output:
        output.write('# FRAME_NUM   RMSD_REF1   RMSD_REF2\n')
        for ts in u.trajectory:
            u_all.translate(-protein.center_of_mass())
            R, rmsd_ref1 = rotation_matrix(protein.positions, ref1_pos)
            R, rmsd_ref2 = rotation_matrix(protein.positions, ref2_pos)
            output.write('%6d   %15f   %15f\n'%(ts.frame,rmsd_ref1,rmsd_ref2))

    ref1.trajectory.close()
    ref2.trajectory.close()

    # go back to frame 0 of the trajectory
    #u.trajectory.rewind()

    # dihedral analysis... or something like that...

    # close out...
    u.trajectory.close()

