import sys
import pandas as pd
import os
import glob

all_dssp = glob.glob("data_dssp/*.dssp")
frame = 10
i=0
for dssp in all_dssp:
    i+=1
    print("##########")
    print("### "+str(i)+" ####")
    print("##########")
    input_path = dssp
    input_file = open(input_path, "r")

    input_name = input_path.split("/")[1].split(".")[0]

    res_main = input_name[len(input_name)-1:len(input_name)] # main residue

    dssp_residue = list()
    dssp_identifier = list()
    dssp_aa = list()
    dssp_structure = list()

    flg_start = False

    #appendwindow
    for k in range(0, frame):
        dssp_identifier.append(0)
        dssp_aa.append("0")
        dssp_residue.append(res_main)
        dssp_structure.append("0")

    line = input_file.readline()
    while line:
        if flg_start:
            buf_residue = str(line[11:12])
            if buf_residue==res_main:
                dssp_identifier.append(int(line[0:5]))
                dssp_residue.append(str(line[11:12]).upper())
                dssp_aa.append(str(line[13:14]).upper())
                dssp_structure.append(str(line[16:17]).upper())
        if line.find("#")>=0:
            flg_start = True
        line = input_file.readline()
    
    #appendwindow
    for k in range(0, frame):
        dssp_identifier.append(0)
        dssp_aa.append("0")
        dssp_residue.append(res_main)
        dssp_structure.append("0")

    if not os.path.exists("data_csv"):
        os.mkdir("data_csv")
    df = pd.DataFrame(list(zip(dssp_identifier, dssp_residue, dssp_aa, dssp_structure)), columns = ["Id", "Residue", "AA", "Structure"])
    df.to_csv("data_csv/" + input_name + ".csv", index=False, header=False)