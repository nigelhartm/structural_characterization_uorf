import sys
import iupred2a_lib
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import random
import scipy.stats as stats
from matplotlib.ticker import PercentFormatter

def get_peptideseq(seq):
    global err_flag
    table = {
        'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
        'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
        'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
        'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',                 
        'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
        'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
        'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
        'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
        'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
        'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
        'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
        'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
        'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
        'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
        'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
        'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W',
    }
    protein =""
    if len(seq)%3 == 0:
        for i in range(0, len(seq), 3):
            codon = seq[i:i + 3]
            protein += table[codon]
    else:
        for i in range(0, len(seq)-len(seq)%3, 3):
            codon = seq[i:i + 3]
            protein += table[codon]
        err_flag = True
    return protein

input_path = sys.argv[1]
input_file = open(input_path, "r")

alist = []
blist = []
head=""
seq=""
leng = 0
i = 0
max_g = 0
min_g = 0
mean_g = 0
line = input_file.readline()
while line:
    if i >= 2000:
        print("Succesful all elements")
        break
    if line.startswith(">"):
        head=line
        head = head.replace("\n", "")
    else:
        if line.find("SEQ:") >= 0:
            seq = line.split(":")[1]
        if line.find("LENGTH:") >= 0:
            leng = int(line.split(":")[1])
        if line.find("TYPE:") >= 0:
            typ = int(line.split(":")[1])
            # leng nucleotides
            if (typ == 1 or typ == 2)  and leng%3==0 and leng >= 50 and leng <= 400:
                id = int(line.split("_")[1])
                seq = seq.replace("\n", "")
                seq = get_peptideseq(seq)
                seq = seq.replace("_", "")
                rndm = list(seq)
                random.shuffle(rndm)
                rndm = "".join(rndm)
                print("original" + str(seq))
                print("random" + str(rndm))
                iupred2_result = iupred2a_lib.iupred(seq, 'short')
                iupred2_random_result = iupred2a_lib.iupred(rndm, 'short')
                max_l = max(iupred2_result[0])
                min_l = min(iupred2_result[0])
                mean_l = sum(iupred2_result[0])/len(iupred2_result[0])
                mean_random_l = sum(iupred2_random_result[0])/len(iupred2_random_result[0])
                max_g += max_l
                min_g += min_l
                mean_g += mean_l
                for j in range(0, len(iupred2_result[0])):
                    alist.append(iupred2_result[0][j])
                for k in range(0, len(iupred2_random_result[0])):
                    blist.append(iupred2_random_result[0][k])
                print("max: " + str(max_l) + "\tmin:" +str(min_l)+"\tmean:" + str(mean_l))
                i+=1
    line = input_file.readline()
input_file.close()
print("max_g: " + str(max(alist)) + "\tmin_g:" +str(min(alist))+"\tmean_g:" + str(sum(alist)/len(alist)))
print(str(i) + "Succesful all elements")
a = np.array(alist)
b = np.array(blist)

plt.hist([a,b], range=(0.0, 1.0), weights=[np.ones(len(a))/len(a), np.ones(len(b))/len(b)], bins=20, label=['original', 'random'])
#plt.gca().yaxis.set_major_formatter(PercentFormatter(1))
plt.legend(loc='upper right')
plt.xlabel("IUPred2A score distribution")
plt.ylabel("frequency density")
#plt.ylim(0.0, 0.5)
plt.yscale("log")
plt.savefig("test__uorf_disordered_region_vs_random.png", bbox_inches='tight', dpi=96 * 10)