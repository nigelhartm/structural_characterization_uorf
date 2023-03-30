import glob
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
import pandas as pd
import numpy as np
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

frame = 10
aa_classes = 25 # 25

model = Sequential()
model.add(Dense(aa_classes*((2*frame)+1), input_shape=(aa_classes*((2*frame)+1),), activation='sigmoid'))
model.add(Dense(50, activation='sigmoid'))
model.add(Dense(26, activation='sigmoid'))
model.add(Dense(3, activation='softmax'))
model.compile(optimizer='Adam', loss='categorical_crossentropy', metrics=['accuracy'])
model.summary()

train_loss = []
train_acc = []
val_loss = []
val_acc = []

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

print("\nTrain model....")
train_history = model.fit(X,Y, epochs=5, batch_size=100, shuffle=False, validation_split=0.1, verbose=1)
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
plt.savefig("training_acc.png", dpi=96 * 10) # 96 my monitor dpi
plt.close()

plt.plot(train_loss, color='#ff0000', label='Training loss', linewidth=0.5, linestyle='-')
plt.plot(val_loss, color='#ffaeae', label='Val loss', linewidth=0.5, linestyle='-')
plt.title('Training')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend()
plt.savefig("training_loss.png", dpi=96 * 10) # 96 my monitor dpi
plt.close()

# save model
model.save("model")