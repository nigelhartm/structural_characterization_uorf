import sys
import iupred2a_lib
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import random
import scipy.stats as stats
from matplotlib.ticker import PercentFormatter

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
        seq = line
        seq = seq.replace("_", "")
        seq = seq.replace("\n", "")
        leng = len(seq)
        # leng amino acids
        if leng >= 50 and leng <= 400:
            rndm = list(seq)
            random.shuffle(rndm)
            rndm = "".join(rndm)
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
plt.savefig("cds_disordered_region_vs_random.png", bbox_inches='tight', dpi=96 * 10)