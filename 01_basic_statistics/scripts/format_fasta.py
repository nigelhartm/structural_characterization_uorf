import sys
input_path = sys.argv[1]
input_file = open(input_path, "r")
output_file = open("formatted_" + input_path, "w")
line = input_file.readline()
output_file.write(line)
line = input_file.readline()
while line:
    if line.startswith(">"):
        output_file.write("\n" + line)
    else:
        output_file.write(line[0:len(line)-1])
    line = input_file.readline()
output_file.write("\n")
input_file.close()
output_file.close()