import sys
import pandas as pd
import os
import glob

input_path = sys.argv[1]
input_file = open(input_path, "r")

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
for i in range(0, len(stc)):
	if stc[i]=="H" or stc[i]=="G" or stc[i]=="I":
		stcnew+="H"
	elif stc[i]=="E" or stc[i]=="B":
		stcnew+="H"
	else: # df.iloc[i,3]==" ":
		stcnew+="C"
print(stcnew)
