import sys
import matplotlib.pyplot as plt
import calendar
import time
runner_id = str(calendar.timegm(time.gmtime()))

input_file = open("uORF_longest_formatted_Araport11_5_utr_20220914.txt", "r")
N_uORF = 0
locMax = 0
fixed_max = 100
sample_list = [0] * fixed_max
x = range(0, fixed_max)
line = input_file.readline()
while line:
    if line.startswith(">"):
        sample_list[int(locMax)] += 1
        locMax = 0
    elif line.find("TYPE")>=0:
        N_uORF += 1
        locMax += 1
    line = input_file.readline()

#for i in range(0, len(sample_list)):
#    sample_list[i] = float(round(sample_list[i] /N_uORF*100,2))
plt.bar(x, sample_list, 0.9, label="uORF", align="center", color="black")
input_file.close()
plt.ylabel("y Genes")
plt.xlabel("x uORFs")
plt.yscale("log")
plt.xlim((-0.7, 99.7))
plt.legend()
plt.savefig(runner_id + "_uorf_amountplot.png", dpi=96 * 10) # 96 my monitor dpi
plt.close()