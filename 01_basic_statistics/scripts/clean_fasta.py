import sys
import random
import os
input_path = sys.argv[1]
input_file = open(input_path, "r")
output_file = open("buf_" + input_path, "w")
line = input_file.readline()
while line:
    if line.startswith('>'):
        output_file.write(line)
    else:
        output_file.write(line.replace("Y", "").replace("K", "").replace("S", "").replace("W", "").replace("M", ""))
    line = input_file.readline()
input_file.close()
output_file.close()
os.remove(input_path)
os.rename("buf_" + input_path, input_path)