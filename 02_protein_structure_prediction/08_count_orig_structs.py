from cgitb import small
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
import pandas as pd
import glob
import re
import numpy as np
import keras
import re

def calcOwn(seq, ser):
    print(seq)
    print(ser)
    h=0
    s=-0
    for match in re.finditer("H{1,}(.{0,1}H{1,}){0,}", seq):
        if (match.end()-match.start() > 1):
            x = ser[match.start():match.end()]
            x = [int(i) for i in x]
            ybuf = seq[match.start():match.end()]
            y = [0] * len(ybuf)
            cnt = 0
            for c in range(0, len(ybuf)):
                if ybuf[c] == "H":
                    y[c] = 1
                    cnt += 1
            xy = [0] * len(ybuf)
            print(x)
            print(y)
            print(ybuf)
            print(xy)
            for m in range(0, len(ybuf)):
                xy[m] = int(x[m]) * int(y[m])
            if int(sum(xy)/cnt) >= 5 and len(x)>=2:
                h += 1
    return [h, s]

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

identifier_lst = list()
helix_lst = list()
sheet_lst = list()

frame = 10

print("getOriginal counts minus the ones covered by frame")
all_dssp = glob.glob("data_dssp/*.dssp")
k=0
for dssp in all_dssp:
    if k>200:
        break
    k+=1
    identifier = dssp.split("/")[1].split(".")[0]
    input_file_pdb = open("data_pdb/" + identifier + ".pdb", "r")
    input_file_dssp = open("data_dssp/" + identifier + ".dssp", "r")
    residue = identifier[len(identifier)-1:len(identifier)]
    start = 0
    end = 0
    history_lst = list()
    cnt = -1
    line = input_file_dssp.readline()
    while line:
        if line.find("#")>=0:
            cnt = 0
        elif (str(line[11:12]) != residue) and (cnt > 0):
            break
        elif cnt >= 0 and cnt < frame:
            cnt += 1
            buf = int(line[5:10])
            history_lst.append(buf)
        elif cnt == frame:
            buf = int(line[5:10])
            start = int(buf)
            cnt += 1
        elif cnt >= 11:
            buf = int(line[5:10])
            history_lst.pop(0)
            history_lst.append(buf)
            cnt += 1
        line = input_file_dssp.readline()
    end = history_lst[0]

    helix = 0
    sheet = 0

    line = input_file_pdb.readline()
    while line:
        if line.startswith("HELIX"):
            res = str(line[19:20])
            if res == "A":
                # end>start begin<end
                if int(line[32:37]) > start and int(line[20:25]) < end:
                    helix += 1
        if line.startswith("SHEET"):
            res = str(line[13:14])
            if res == "A":
                # end>start begin<end
                if int(line[33:37]) > start and int(line[22:26]) < end:
                    sheet += 1
        if line.startswith("ATOM"):
            break
        line = input_file_pdb.readline()
    identifier_lst.append(identifier)
    helix_lst.append(helix)
    sheet_lst.append(sheet)
    input_file_pdb.close()
    input_file_dssp.close()

print("Creating DF....")
df = pd.DataFrame(list(zip(identifier_lst, helix_lst, sheet_lst)), columns = ['id', 'helix', 'sheet'])

model = keras.models.load_model("model")

h_ges = 0
h_ges_cnt = 0
h_corr = 0
s_corr = 0
smaller = 0
bigger = 0
both = 0
all = 0
print("Getting seqeunces")
all_csv = glob.glob("data_csv/*.csv")
k=0
for csv in all_csv:
    if k>200:
        break
    k+=1
    identifier = csv.split("/")[1].split(".")[0]
    try:
        csv_df = pd.read_csv(csv, header=None)
    except:
        print("Error reading file " + csv)
    finally:
        AA = ""
        j = 0
        while j < csv_df.shape[0]:
            AA += csv_df.iloc[j,2]
            j += 1
        seq_lst_bin = list()
        if len(AA) >= 21:
            for i in range(frame, len(AA)-frame):
                seq_lst_bin.append(aa_to_binary(AA[i-frame: i+frame+1]))
            data = np.array(seq_lst_bin)
            predicted = model.predict(data, verbose=0)
            output = np.argmax(predicted, axis=1)
            dssp = list()
            # Helix sheet coil
            for i in output:
                if i==0:
                    dssp.append("H")
                elif i==1:
                    dssp.append("S")
                elif i==2:
                    dssp.append("C")
            dssp = "".join(dssp)
            
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
            ser="".join(str(x) for x in ser)
            ##
            ## claculation
            hs = calcOwn(dssp, ser)
            ##
            h = hs[0]
            s = hs[1]
            # compare to original
            all += 1
            h_orig = int(df.loc[df['id'] == identifier].iloc[0][1])
            s_orig = int(df.loc[df['id'] == identifier].iloc[0][2])
            h_ges_cnt += 1
            h_buf = (max(h, h_orig)-min(h, h_orig)) / (h+h_orig)
            if h==h_orig:
                h_corr += 1
            if s==s_orig:
                s_corr += 1
            if h==h_orig and s==s_orig:
                both += 1
            if h>h_orig:
                bigger+=1
            if h<h_orig:
                smaller += 1
            print(str(df.loc[df['id'] == identifier].iloc[0][0]) + "\tOriginal H:" + str(h_orig) + "\tS:" + str(s_orig) + "\tPredicted: H:" + str(h) + "\tS:" + str(s) + "\tAccH:" + str(round(h_corr/all,2)) + "\tAccS:" + str(round(s_corr/all,2)) + "\tAcc:" + str(round(both/all, 2)) + "\tsmaller:" + str(smaller)+ "\tbigger:" + str(bigger)+ "\t H new:"+str(h_ges/h_ges_cnt))
        else:
            print("Error to small frame" + csv)