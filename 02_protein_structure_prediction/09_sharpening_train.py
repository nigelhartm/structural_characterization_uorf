# and combine with original
from ast import arg
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
from tensorflow import keras
import numpy as np
import sys
import pandas as pd
import glob
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
from keras.wrappers.scikit_learn import KerasClassifier
from keras.utils import np_utils
from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras.callbacks import EarlyStopping
from keras.models import model_from_json
from keras.models import load_model
from tensorflow import keras

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
k=0
frame = 10
struct_frame = 5
X = list()
Y = list()

all_csv = glob.glob("data_csv/*.csv")
for csv in all_csv:
    if k>=1500:
        break
    k+=1
    print(csv + " " + str(k))
    df = pd.read_csv(csv, header=None)
    df.columns = ['ID', 'RES', 'AA', 'STRUCT']
    seq = "".join(df['AA'].tolist())

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
    
    pred_struct = "".join(dssp)
    struct_str = "".join(df['STRUCT'].tolist())
    struct_str = struct_str[frame:len(struct_str)-frame]
    struct_str = struct_str.replace("G", "H")
    struct_str = struct_str.replace("I", "H")
    struct_str = struct_str.replace("T", "C")
    struct_str = struct_str.replace("S", "C") # need to be before converting to s
    struct_str = struct_str.replace(" ", "C")
    struct_str = struct_str.replace("B", "S")
    struct_str = struct_str.replace("E", "S")
    m=struct_frame
    while m+struct_frame < len(pred_struct):
        substruct = pred_struct[m-struct_frame:m+(struct_frame+1)]
        substruct_arr = list()
        for c in range(0, ((struct_frame*2)+1)):
            substruct_arr.append(encodeChar(substruct[c])[0])
            substruct_arr.append(encodeChar(substruct[c])[1])
            substruct_arr.append(encodeChar(substruct[c])[2])
        out = encodeChar(struct_str[m])
        out = np.array(out)
        substruct_arr = np.array(substruct_arr)
        X.append(substruct_arr)
        Y.append(out)
        m += 1

X = np.array(X)
Y = np.array(Y)

model = Sequential()
model.add(Dense(3*((2*struct_frame)+1), input_shape=(3*((2*struct_frame)+1),), activation='sigmoid'))
model.add(Dense(15, activation='sigmoid'))
model.add(Dense(7, activation='sigmoid'))
model.add(Dense(3, activation='softmax'))
model.compile(optimizer='Adam', loss='categorical_crossentropy', metrics=['accuracy'])
model.summary()

train_loss = []
train_acc = []
val_loss = []
val_acc = []

print("\nTrain model....")
train_history = model.fit(X,Y, epochs=10, batch_size=250, shuffle=False, validation_split=0.1, verbose=1)
train_loss = train_history.history['loss']
train_acc = train_history.history['accuracy']
val_loss = train_history.history['val_loss']
val_acc = train_history.history['val_accuracy']

plt.plot(train_acc, '#00ff00', label='Training acc', linewidth=0.5, linestyle='-')
plt.plot(val_acc, '#aeffae', label='Val acc', linewidth=0.5, linestyle='-')
plt.title('Training')
plt.xlabel('Epochs')
plt.ylabel('Accuracy')
plt.legend()
plt.savefig("sharp_training_acc.png", dpi=96 * 10) # 96 my monitor dpi
plt.close()

plt.plot(train_loss, color='#ff0000', label='Training loss', linewidth=0.5, linestyle='-')
plt.plot(val_loss, color='#ffaeae', label='Val loss', linewidth=0.5, linestyle='-')
plt.title('Training')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend()
plt.savefig("sharp_training_loss.png", dpi=96 * 10) # 96 my monitor dpi
plt.close()

# save model
model.save("model_sharp")