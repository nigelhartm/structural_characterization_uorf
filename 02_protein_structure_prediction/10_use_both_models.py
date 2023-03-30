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

def encodeChar(x):
    if x=="H":
        return [1, 0, 0]
    elif x=="S":
        return [0, 1, 0]
    elif x=="C":
        return [0, 0, 1]
    else:
        print("error")
        exit

seq = sys.argv[1]
orig = sys.argv[2] # give the original structure for comparison

frame = 10
app = "0" * frame
seq = app + seq + app
seq_lst_bin = list()

for i in range(frame, len(seq)-frame):
    seq_lst_bin.append(aa_to_binary(seq[i-frame: i+frame+1]))

data = np.array(seq_lst_bin)
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
for i in range(0, len(dssp)):
    if dssp[i] == orig[i]:
        equal += "1"
        equal_1 += 1
    else:
        equal += "0"

pred_struct = "".join(dssp)
dssp = "".join(dssp)

print("")
print("orig : " + orig)
print("pred : " + dssp)
print("accu : " + "".join(str(x) for x in ser))
print("equal: " + equal)
print("")
print("Equal " + str(equal_1) + " of " + str(len(equal)) + " conclude in  " + str(equal_1/len(equal)))

##
## MODEL2
##
struct_frame = 5
c = list()

for i in range(struct_frame, len(pred_struct)-struct_frame):
    a = pred_struct[i-struct_frame: i+struct_frame+1]
    b = list()
    for k in range(0, len(a)):
        p = encodeChar(a[k])
        b.append(p[0])
        b.append(p[1])
        b.append(p[2])
    c.append(b)

data2 = np.array(c)
model2 = keras.models.load_model("model_sharp")
predicted2 = model2.predict(data2, verbose=0)
output2 = np.argmax(predicted2, axis=1)

pred_new = list()
for i in output2:
    if i==0:
        pred_new.append("H")
    elif i==1:
        pred_new.append("S")
    elif i==2:
        pred_new.append("C")

pred_new = "".join(pred_new)
pred_new = dssp[0:struct_frame] + pred_new + dssp[len(dssp)-struct_frame:len(dssp)]
print("pred_new : " + pred_new)