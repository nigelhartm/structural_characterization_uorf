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

model = keras.models.load_model("model")
struct_frame = 5
model2 = keras.models.load_model("model_sharp")
frame = 10
app = "0" * frame

input = open(sys.argv[1], "r")
buf=""
buf_len = 0
line = input.readline()
j = 0
hg=0
sg=0
cg=0
N = 0
while line:
    if j >= 1000:
        break
    if line.startswith(">"):
        pass
    else:
        if line.find("_SEQ:") >= 0:
            buf = line.split(":")[1].replace("\n", "")
        elif line.find("_LENGTH:") >= 0:
            buf_len = int(line.split(":")[1].replace("\n", ""))
        elif line.find("_TYPE:") >= 0:
            typ =  int(line.split(":")[1].replace("\n", ""))
            if (typ == 1 or typ == 2) and buf_len >= 50 and buf_len <= 200:
                j+=1
                print(j)
                seq = buf
                seq = app + seq + app
                seq_lst_bin = list()
                for i in range(frame, len(seq)-frame):
                    seq_lst_bin.append(aa_to_binary(seq[i-frame: i+frame+1]))
                data = np.array(seq_lst_bin)
                predicted = model.predict(data, verbose=0)
                output = np.argmax(predicted, axis=1)
                dssp = list()

                for i in output:
                    if i==0:
                        dssp.append("H")
                    elif i==1:
                        dssp.append("S")
                    elif i==2:
                        dssp.append("C")
                

                dssp = "".join(dssp)

                c = list()
                for i in range(struct_frame, len(dssp)-struct_frame):
                    a = dssp[i-struct_frame: i+struct_frame+1]
                    b = list()
                    for k in range(0, len(a)):
                        p = encodeChar(a[k])
                        b.append(p[0])
                        b.append(p[1])
                        b.append(p[2])
                    c.append(b)

                data2 = np.array(c)
                predicted2 = model2.predict(data2, verbose=0)
                output2 = np.argmax(predicted2, axis=1)
                hl=0
                sl=0
                cl=0
                pred_new = list()
                for i in output2:
                    if i==0:
                        hl+=1
                        pred_new.append("H")
                    elif i==1:
                        sl+=1
                        pred_new.append("S")
                    elif i==2:
                        cl+=1
                        pred_new.append("C")
                hg+=hl
                sg+=sl
                cg+=cl
                N+=1
                pred_new = "".join(pred_new)
                pred_new = dssp[0:struct_frame] + pred_new + dssp[len(dssp)-struct_frame:len(dssp)]
    line = input.readline()

hg=hg/N
sg=sg/N
cg=cg/N
sum = hg+sg+cg
hg = hg/sum
sg = sg/sum
cg = cg/sum
print("H: " + str(hg))
print("S: " + str(sg))
print("C: " + str(cg))
