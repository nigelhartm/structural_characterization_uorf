import sys
import matplotlib.pyplot as plt
import calendar
import time
runner_id = str(calendar.timegm(time.gmtime()))
input_paths = sys.argv[1]
input_paths = input_paths.split("+")
output_file = open("stats.txt", "w")
output_file.write("# Number of sequences; Sum of lengths; Mean of lengths; Min length; Max length; Origin\n")
runn = 0
for input_path in input_paths:
    input_file = open(input_path, "r")
    name = ""
    line = input_file.readline()
    N_Seq = 0 # Overall Sequences in file
    AA_len_sum = 0
    AA_len_max = 0
    AA_len_min = 1000000
    while line:
        if line.startswith(">"):
            N_Seq += 1
        else:
            if line.find("LENGTH") >= 0:
                AA_len = int(line.split(":")[1])
                AA_len_sum += AA_len
                if AA_len > AA_len_max:
                    AA_len_max = AA_len
                if AA_len < AA_len_min:
                    AA_len_min = AA_len
        line = input_file.readline()
    AA_len_mean = AA_len_sum / N_Seq
    output_file.write(str(N_Seq) + ";" + str(AA_len_sum) + ";" + str(AA_len_mean) + ";" + str(AA_len_min) + ";" + str(AA_len_max) + ";" + input_path + "\n")
    input_file.close()
    input_file = open(input_path, "r")
    line = input_file.readline()
    fixed_max = 990 + 10
    sample_list = [0] * fixed_max
    while line:
        if line.startswith(">"):
            pass
        else:
            if line.find("LENGTH") >= 0:
                AA_len = int(line.split(":")[1])
                for i in range(0, fixed_max):
                    if AA_len <= i:
                        sample_list[int(i)] += 1
                        break
        line =input_file.readline()
    for i in range(0, len(sample_list)):
        sample_list[i] = sample_list[i] / N_Seq
    if input_path.find("random")<0:
        plt.plot(sample_list, "r-", label="original", linewidth=0.4)
    else:
        runn+=1
        plt.plot(sample_list, label="random"+str(runn), linewidth=0.4)
    input_file.close()
output_file.close()
plt.ylabel("number uORFs relative")
plt.xlabel("length")
plt.yscale("log")
plt.legend()
plt.savefig(runner_id + "plot.png", dpi=96 * 10) # 96 my monitor dpi
plt.close()
