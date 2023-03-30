from ast import arg
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
from tensorflow import keras
import numpy as np
import sys
import pandas as pd

input_path = "all_data.csv"
Y = list()
X = list()

print("\nReading csv....")
df = pd.read_csv(input_path, header=None)
df.columns = ['X', 'Y']

print("\nConvert X Y....")
for index, row in df.iterrows():
    Y.append(np.fromstring(df["Y"].iloc[index][2:len(df["Y"].iloc[index])-2], sep=",", dtype=int))
    X.append(np.fromstring(df["X"].iloc[index][2:len(df["X"].iloc[index])-2], sep=",", dtype=int))

X = np.array(X)
Y = np.array(Y)

print("Predict....")
model = keras.models.load_model("model")
predicted = model.predict(X, verbose=0)
output = np.argmax(predicted, axis=1)

corr = 0
all = 0

for i in range(0, len(output)):
    if max(predicted[i]) > 0.6:
        pred = output[i]
        orig = -1
        if str(Y[i])=="[1 0 0]":
            orig = 0
        elif str(Y[i])=="[0 1 0]":
            orig = 1
        elif str(Y[i])=="[0 0 1]":
            orig = 2
        if orig == -1:
            print("error")
            print(str(Y[i]))
            exit()
        if pred == orig:
            corr+=1
        all += 1
        print("orig: " + str(Y[i]) + " (" + str(orig) +") " + " pred: " + str(pred) + " Accuracy: " + str(corr/all))

print("Accuracy: " + str(corr/all))