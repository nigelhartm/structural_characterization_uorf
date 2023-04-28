import sys
import os
import glob

all_dssp = glob.glob("data_fold_dssp/*.dssp")

h_g = 0
s_g = 0
c_g = 0
j=0
for dssp in all_dssp:
    input_file = open(dssp, "r")
    dssp_structure = list()
    flg_start = False
    line = input_file.readline()
    while line:
        if flg_start:
            dssp_structure.append(str(line[16:17]).upper())
        if line.find("#")>=0:
            flg_start = True
        line = input_file.readline()
    stc = "".join(dssp_structure)
    stcnew=""
    h_l = 0
    s_l = 0
    c_l = 0
    for i in range(0, len(stc)):
        if stc[i]=="H" or stc[i]=="G" or stc[i]=="I":
            stcnew+="H"
            h_l+=1
        elif stc[i]=="E" or stc[i]=="B":
            stcnew+="S"
            s_l+=1
        else: # df.iloc[i,3]==" ":
            stcnew+="C"
            c_l+=1
    print(stcnew)
    print("H: " + str(h_l/len(stcnew)) + "\tS:" +str(s_l/len(stcnew))+"\tC:" + str(c_l/len(stcnew)))
    h_g += (h_l/len(stcnew))
    s_g += (s_l/len(stcnew))
    c_g += (c_l/len(stcnew))
    j+=1
print("Global:")
print("H: " + str(h_g/j) + "\tS:" +str(s_g/j)+"\tC:" + str(c_g/j))