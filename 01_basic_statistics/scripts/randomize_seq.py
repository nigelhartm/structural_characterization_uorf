import sys
import random
input_path = sys.argv[1]
N = int(sys.argv[2])
for i in range(1, N+1):
    input_file = open(input_path, "r")
    output_file = open("random" + str(i) + "_" + input_path, "w")
    line = input_file.readline()
    while line:
        if line.startswith('>'):
            output_file.write(line)
        else:
            buf = list(line[0:len(line)-1])
            random.shuffle(buf)
            output_file.write("".join(buf) + "\n")      
        line = input_file.readline()
    input_file.close()
    output_file.close()