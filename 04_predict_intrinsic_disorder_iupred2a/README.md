# iupred2a_prediction

## 1 clone folder
into a new folder

## 2 download IUPred2A
download from https://iupred2a.elte.hu and put it in to folder

## 3 run format_disordered_region.py
parameter a file with uORF'S in following format:

>AT1G77760.1 | [1-117] | chr1:29239368-29239484 REVERSE LENGTH=117
>AT1G77765.3 | [1-306] | chr1:29244775-29245080 FORWARD LENGTH=306
uORF_1_SEQ:ATGTATCTATTTTAG
uORF_1_START:21@UTR5
uORF_1_STOP:35@UTR5
uORF_1_LENGTH:5
uORF_1_TYPE:1
uORF_2_SEQ:ATGTAA
uORF_2_START:106@UTR5
uORF_2_STOP:111@UTR5
uORF_2_LENGTH:2
uORF_2_TYPE:1
...
