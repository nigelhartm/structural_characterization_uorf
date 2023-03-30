from ast import arg
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
from tensorflow import keras
import numpy as np
import sys

def aa_to_binary(AA):
    binary_list = []
    for e in AA:
        if e == "A":
            binary_list += [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        elif e == "G":
            binary_list += [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        elif e == "L":
            binary_list += [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        elif e == "V":
            binary_list += [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        elif e == "I":
            binary_list += [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        elif e == "F":
            binary_list += [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        elif e == "Y":
            binary_list += [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        elif e == "R":
            binary_list += [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        elif e == "K":
            binary_list += [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        elif e == "H":
            binary_list += [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        elif e == "E":
            binary_list += [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        elif e == "D":
            binary_list += [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        elif e == "W":
            binary_list += [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        elif e == "P":
            binary_list += [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        elif e == "Q":
            binary_list += [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        elif e == "N":
            binary_list += [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        elif e == "S":
            binary_list += [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]
        elif e == "T":
            binary_list += [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0]
        elif e == "C":
            binary_list += [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0]
        elif e == "M":
            binary_list += [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0]
        elif e == "B":
            binary_list += [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0]
        elif e == "Z":
            binary_list += [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0]
        elif e == "X":
            binary_list += [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0]
        elif e == "J":
            binary_list += [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0]
        elif e == "O":
            binary_list += [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
        elif e == "0": # 0 before and after seq to get everything #appendwindow
            binary_list += [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        else:
            print("ERROR 0100:" + str(e))
            exit()
    return binary_list

seq = sys.argv[1]
orig = sys.argv[2] # give the original structure for comparison

frame = 10

app = "0" * frame

seq = app + seq + app

seq_lst_bin = list()

for i in range(frame, len(seq)-frame):
    seq_lst_bin.append(aa_to_binary(seq[i-frame: i+frame+1]))

data = np.array(seq_lst_bin)
print(data)
model = keras.models.load_model("model")
predicted = model.predict(data, verbose=0)
output = np.argmax(predicted, axis=1)

ser = list()

for i in range(0, len(output)):
    if predicted[i][int(output[i])]>=0.9:
        ser.append(9)
    elif predicted[i][int(output[i])]>=0.8:
        ser.append(8)
    elif predicted[i][int(output[i])]>=0.7:
        ser.append(7)
    elif predicted[i][int(output[i])]>=0.6:
        ser.append(6)
    elif predicted[i][int(output[i])]>=0.5:
        ser.append(5)
    elif predicted[i][int(output[i])]>=0.4:
        ser.append(4)
    elif predicted[i][int(output[i])]>=0.3:
        ser.append(3)
    elif predicted[i][int(output[i])]>=0.2:
        ser.append(2)
    elif predicted[i][int(output[i])]>=0.1:
        ser.append(1)
    else:
        ser.append(0)

dssp = list()
for i in output:
    if i==0:
        dssp.append("H")
    elif i==1:
        dssp.append("S")
    elif i==2:
        dssp.append("C")

equal = ""
equal_1 = 0
eq_s = 0
all_s = 0
eq_h = 0
all_h = 0
eq_c = 0
all_c = 0
for i in range(0, len(dssp)):
    if orig[i] == "S":
        all_s += 1
    if orig[i] == "H":
        all_h += 1
    if orig[i] == "C":
        all_c += 1
    if dssp[i] == orig[i]:
        equal += "1"
        equal_1 += 1
        if dssp[i] == "S":
            eq_s += 1
        if dssp[i] == "H":
            eq_h += 1
        if dssp[i] == "C":
            eq_c += 1
    else:
        equal += "0"


print("")
print("orig : " + orig)
print("pred : " + "".join(dssp))
print("accu : " + "".join(str(x) for x in ser))
print("equal: " + equal)
print("")
print("Equal " + str(equal_1) + " of " + str(len(equal)) + " conclude in  " + str(equal_1/len(equal)))
print("S     " + str(eq_s) + " of " + str(all_s) + " conclude in  " + str(eq_s/all_s))
print("H     " + str(eq_h) + " of " + str(all_h) + " conclude in  " + str(eq_h/all_h))
print("C     " + str(eq_c) + " of " + str(all_c) + " conclude in  " + str(eq_c/all_c))