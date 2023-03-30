import sys

option_x = str(sys.argv[2]) # min|max
fixed_len = int(sys.argv[3]) #length of file

maxid = [""] * fixed_len
input_path = sys.argv[1]
output_file = open(option_x+"_"+input_path, "w")
for i in range(1, fixed_len):
    print(str(i) + "/"+ str(fixed_len))
    input_file = open(input_path, "r")
    line = input_file.readline()
    max = 0
    if option_x == "min":
        max = 1000000
    max_id = ""
    header=""
    seq=""
    while line:
        if line.startswith(">"):
            id = line[1:line.find(' ')]
            l = int(line.split("LENGTH=")[1])
            if option_x=="max":
                if id not in maxid and l>=max:
                    max = l
                    max_id = id
                    header = line
                    line = input_file.readline()
                    seq = line
            else:
                if id not in maxid and l<=max:
                    max = l
                    max_id = id
                    header = line
                    line = input_file.readline()
                    seq = line
        line = input_file.readline()
    maxid[i] = max_id
    input_file.close()
    output_file.write(header)
    output_file.write(seq)