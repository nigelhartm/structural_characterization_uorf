import matplotlib.pyplot as plt
import numpy as np
import calendar
import time
runner_id = str(calendar.timegm(time.gmtime()))
input_file = open("stats_peptides.txt", "r")
#plt.xticks(range(0,42, 2), ["A", "G", "L", "V", "I", "F", "Y", "R", "K", "H", "E", "D", "W", "P", "Q", "N", "S", "T", "C", "M", "_"])
#new order
plt.xticks(range(0,40, 2), ["A", "G", "L", "V", "I", "F", "Y", "W", "R", "K", "H", "E", "D", "P", "C", "Q", "N", "S", "T", "M"])
plt.yticks(range(0,20))
line = input_file.readline()
# wegen bar plot
i=-0.375
c = "black"
while line:
    if not line.startswith("#"):
        if str(line.split(";")[1])=="relative":
            buf = line.split(";")
            lbl = buf[0]
            if lbl=="original":
                lbl = "CDS"
            else:
                lbl = "uORF"
            y = [buf[3], buf[4], buf[5], buf[6], buf[7], buf[8], buf[9],buf[15], buf[10], buf[11], buf[12], buf[13], buf[14],buf[16], buf[21], buf[17], buf[18], buf[19], buf[20], buf[22]]
            y = [float(i) for i in y]
            #plt.plot(y, label=lbl, linewidth=0.4)
            x = np.arange(0.0, 40.0, 2.00)
            plt.bar(x+i,y, 0.75, label=lbl, align="center", linewidth=3, zorder=3, color=c)
            i+=0.75
            c="grey"
    line = input_file.readline()
plt.ylabel("Frequencies in %")
plt.xlabel("Aminoacid")
plt.legend()
plt.grid(True,color='#000000',linestyle=':', linewidth=0.2, zorder=0)
plt.xlim((-0.75, 38.75))
plt.savefig(runner_id + "plot_aa_cdsuorf_distrib.png", dpi=96 * 10) # 96 my monitor dpi
