import os
import glob
all_pdb = glob.glob("data_fold_pdb/*.pdb")
for pdb in all_pdb:
    print(pdb)
    id = pdb.split(".")[0]
    id = id.split("/")[1]
    os.system("./dssp " + pdb + " data_fold_dssp/" + id + ".dssp")