import sys

def getCDS(identifier, file):
    line = file.readline()
    found = False
    while line:
        if line.startswith('>'):
            act_id = line[1:line.find(' ')]
            if act_id == identifier:
                found = file.readline() # take next lines seq
                return found
        line = file.readline()
    file.close()
    return ""

input_path = sys.argv[1]
cds_path = sys.argv[2]
input_file = open(input_path, "r")
cds_file = open(cds_path, "r")
output_file = open("uORF_" + input_path.split(".")[0] + ".txt", "w")
line = input_file.readline()
identifier = ""
N_uORF = 0
while line:
    if line.startswith('>'):
        identifier = line[1:line.find(' ')]
        output_file.write(line)
    else:
        N_uORF = 0
        UTR5 = line
        CDS = getCDS(identifier, cds_file)
        SEQ = UTR5 + CDS#[0:100]
        SEQ = SEQ.replace("\n", "")
        ind_open = -1
        i=19 #uORFlight count even this
        while i <= len(UTR5)-3:
            #if ind_open < 0: # maybe uniportant now
            if UTR5[i:i+3]=="ATG":
                ind_open = i
                j = 1
                while i+j <= len(SEQ)-3:
                    if SEQ[(i+j):(i+j)+3]=="TAG" or SEQ[(i+j):(i+j)+3]=="TAA" or SEQ[(i+j):(i+j)+3]=="TGA":
                        if ((i+j) - ind_open) % 3 == 0:
                            # uORFlight count even this small ones
                            #if ((i+j) - ind_open) / 3 < 2:
                            #    i = ind_open + 1
                            #    ind_open = -1 # close but to small to count
                            #    break
                            N_uORF += 1
                            pos_stop = "@UTR5"
                            uorf_type = 1
                            if (i+j) >= len(UTR5)-3:
                                pos_stop = "@CDS"
                                uorf_type = 2
                            if (i+j) == len(SEQ)-3:
                                uorf_type = 3
                            output_file.write("uORF_" + str(N_uORF) + "_SEQ:" + SEQ[ind_open:(i+j)+3] + "\n")
                            output_file.write("uORF_" + str(N_uORF) + "_START:" + str(ind_open+1) + "@UTR5" + "\n")
                            output_file.write("uORF_" + str(N_uORF) + "_STOP:" + str((i+j)+3) + pos_stop + "\n")
                            output_file.write("uORF_" + str(N_uORF) + "_LENGTH:" + str(int(((i+j) - ind_open)/3)+1) + "\n")
                            output_file.write("uORF_" + str(N_uORF) + "_TYPE:" + str(uorf_type) + "\n")
                            i = ind_open + 1
                            ind_open = -1 # close uorf
                            break
                    j += 1
            i+=1
    line = input_file.readline()
input_file.close()
output_file.close()
cds_file.close()