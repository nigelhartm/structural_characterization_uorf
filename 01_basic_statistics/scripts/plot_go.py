import sys
from turtle import color
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
input_path = sys.argv[1]
df = pd.read_csv(input_path, sep='\t', header=0)
df = df.sort_values(by=str(list(df.columns)[6]), ascending=True)
##
## cut 30 at highest folding
##
df = df.iloc[0:15, :]
go = df.iloc[:,0]
x = range(0,go.shape[0])
plt.yticks(x, go)
fold = df.iloc[:,5]
p = df.iloc[:,6]
c = ["#000000"] * go.shape[0]
for i in range(0, go.shape[0]):
    if float(p.iloc[i]) < 1e-10:
        c[i] = "#000000"
    elif  float(p.iloc[i]) < 1e-8:
        c[i] = "#333333"
    elif  float(p.iloc[i]) < 1e-6:
        c[i] = "#666666"
    elif  float(p.iloc[i]) < 1e-4:
        c[i] = "#999999"
    elif  float(p.iloc[i]) < 0.01:
        c[i] = "#cccccc"
    elif  float(p.iloc[i]) < 0.05:
        c[i] = "#eeeeee"
    else:
        c[i] = "#ffffff"
legend_elements = [Line2D([0], [0], marker='o', color='w', label='p < 1e-10',
                          markerfacecolor='#000000', markersize=15),
                          Line2D([0], [0], marker='o', color='w', label='p < 1e-8',
                          markerfacecolor='#333333', markersize=15),
                          Line2D([0], [0], marker='o', color='w', label='p < 1e-6',
                          markerfacecolor='#666666', markersize=15),
                          Line2D([0], [0], marker='o', color='w', label='p < 1e-4',
                          markerfacecolor='#999999', markersize=15),
                          Line2D([0], [0], marker='o', color='w', label='p < 0.01',
                          markerfacecolor='#cccccc', markersize=15),
                          Line2D([0], [0], marker='o', color='w', label='p < 0.05',
                          markerfacecolor='#eeeeee', markersize=15),
                          Line2D([0], [0], marker='o', color='w', label='p >= 0.05',
                          markerfacecolor='#ffffff', markersize=15),]
plt.xlabel("Folding Enrichment")
plt.barh(x, fold, color=c)
plt.gca().invert_yaxis()
plt.legend(handles=legend_elements, loc=(1.04, 0))
plt.savefig(input_path.split(".")[0]+".png",bbox_inches='tight', dpi=96 * 10)
