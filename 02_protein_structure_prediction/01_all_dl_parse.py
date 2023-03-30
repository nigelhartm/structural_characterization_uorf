import requests
import sys
import os
#import time

input_path = sys.argv[1]
input_file = open(input_path, "r")

line = input_file.readline() # header
line = input_file.readline()
s = requests.Session()
a = requests.adapters.HTTPAdapter(max_retries=100)
s.mount('http://', a)

i=0
while line:
    i+=1
    print("##########")
    print("### "+str(i)+" ####")
    print("##########")
    identifier = str(line.split(" ")[0]) # no tab??????
    if len(identifier)<=5:
        response = s.get("https://files.rcsb.org/download/" + identifier[0:4] + ".pdb", verify=False)
        open("data_pdb/" + identifier + ".pdb", "wb").write(response.content)
        os.system("./dssp data_pdb/" + identifier + ".pdb data_dssp/" + identifier + ".dssp")
    line = input_file.readline()
    #time.sleep(0.04)
input_file.close()
