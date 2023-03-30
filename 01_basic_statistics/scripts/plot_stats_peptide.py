import matplotlib.pyplot as plt
import calendar
import time
runner_id = str(calendar.timegm(time.gmtime()))
input_file = open("stats_peptides.txt", "r")
plt.xticks(range(0,21), ["A", "G", "L", "V", "I", "F", "Y", "R", "K", "H", "E", "D", "W", "P", "Q", "N", "S", "T", "C", "M", "_"])
line = input_file.readline()
while line:
    if not line.startswith("#"):
        if str(line.split(";")[1])=="relative":
            buf = line.split(";")
            lbl = buf[0]
            y = [buf[3], buf[4], buf[5], buf[6], buf[7], buf[8], buf[9], buf[10], buf[11], buf[12], buf[13], buf[14], buf[15], buf[16], buf[17], buf[18], buf[19], buf[20], buf[21], buf[22], buf[23]]
            y = [float(i) for i in y]
            plt.plot(y, label=lbl, linewidth=0.4)
    line = input_file.readline()
plt.ylabel("frequencies in %")
plt.xlabel("amino acid")
plt.legend()
plt.grid(True)
plt.savefig(runner_id + "aa_plot.png", dpi=96 * 10) # 96 my monitor dpi
