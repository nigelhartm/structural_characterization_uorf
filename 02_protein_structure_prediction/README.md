# Protein secondary structure prediction (Simple model)
This project should make three state prediction of proteins. It consists of several python scripts, which conclude in a trained artificial neural network.
Simple means we use one hot encoding for the aminoacids and a sliding window principle. As Data we used a balanced set of proteins collected by cullpdb. The pdb file are converted to dssp files, which we use as input data for our network.
The States
```
H = α-helix
B = residue in isolated β-bridge
E = extended strand, participates in β ladder
G = 3-helix (310 helix)
I = 5 helix (π-helix)
T = hydrogen bonded turn
S = bend
```
are converted to the basic states
```
Helix
Sheet
Coil
```
## 01_all_dl_parse.py
Download all file from cull file as parameter and convert them to dssp

## 02_transform_dssp
Just take out important stuff from dssp and put in data_csv folder

## 03_build data
Create one big table from data_csv shuffle it and transform into right form

## 04_train_model
Trains a model and save it to model

## 05_use_model
Use for prediction parameters:
Sequence and real structure for comparison

## 07_check_acc
Accuracy was doing problem so check if 70% is really achieved

## 08_count_orig_structs
Count actually won function but not working well….