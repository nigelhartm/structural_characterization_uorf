from ast import operator
import sys
input_path = str(sys.argv[1])
sign = str(sys.argv[2])
length = int(sys.argv[3])
N=0
flg = False
input_file = open(input_path, "r")
output_file = open("ids_" + sign + str(length) + "_" + input_path, "w")
line = input_file.readline()
while line:
    if line.startswith(">"):
        if flg:
            if(sign == "equal"):
                if N == length:
                    output_file.write(identifier + "\n")
            if(sign == "greater"):
                if N > length:
                    output_file.write(identifier + "\n")
        identifier = line[1:line.find(' ')-2]
        flg = True
        N=0
    else:
        if line.find("LENGTH") >= 0:
            N += 1
    line = input_file.readline()
if flg:
    if(sign == "equal"):
        if N == length:
            output_file.write(identifier + "\n")
    if(sign == "greater"):
        if N > length:
            output_file.write(identifier + "\n")
input_file.close()
output_file.close()