import sys
input_path = sys.argv[1]
input_file = open(input_path, "r")
output_file = open("longest_" + input_path, "w")
max_head = ""
max_seq = ""
max_len = 0
act_id = ""
flag_new_max = False
# first line
line = input_file.readline()
act_id = line.split(sep=".")[0]
# as long there is a line
while line:
    # header line
    if line.startswith('>'):
        # set new id
        new_id = line.split(sep=".")[0]
        # new id is no same than before
        if new_id != act_id:
            #write maximimum to file
            output_file.write(max_head)
            output_file.write(max_seq)
            #reset everythin
            max_head = line
            max_seq = ""
            max_len = int(line.split(sep="LENGTH=")[1])
            act_id = new_id
            flag_new_max = True
        else:
            new_len = int(line.split(sep="LENGTH=")[1])
            if new_len > max_len:
                flag_new_max = True
                max_len = new_len
                max_head = line
    # sequence line
    else:
        if flag_new_max:
            max_seq = line
            flag_new_max = False
    line = input_file.readline()
output_file.write(max_head)
output_file.write(max_seq)
input_file.close()
output_file.close()