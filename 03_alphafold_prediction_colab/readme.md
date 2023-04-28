#1
cp no_edit__normal_0_50/*.zip data_fold_pdb

#2
cd data_fold_pdb

#3
unzip '*.zip'

#4
replace bibtex???? [A]ll

#5
rm *.zip
rm *.png
rm *.json
rm *.a3m
rm cite.bibtex

#6
python to_dssp.py

#7
python cnt_strct.py
