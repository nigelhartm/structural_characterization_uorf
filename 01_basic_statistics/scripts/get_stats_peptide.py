import sys
input_paths = sys.argv[1]
input_paths = input_paths.split("+")

stats_peptides = open("stats_peptides.txt", "w")
stats_peptides.write("# Datatype;absolute/relative; Overall; A; G; L; V; I; F; Y; R; K; H; E; D; W; P; Q; N; S; T; C; M; _;\n")

for input_path in input_paths:
    input_file = open(input_path, "r")
    buf_count = [0] * 21
    line = input_file.readline()
    while line:
        if line.startswith(">"):
            pass
        else:
            if not line.startswith("uORF"):
                buf_count[0] += line.count("A")
                buf_count[1] += line.count("G")
                buf_count[2] += line.count("L")
                buf_count[3] += line.count("V")
                buf_count[4] += line.count("I")
                buf_count[5] += line.count("F")
                buf_count[6] += line.count("Y")
                buf_count[7] += line.count("R")
                buf_count[8] += line.count("K")
                buf_count[9] += line.count("H")
                buf_count[10] += line.count("E")
                buf_count[11] += line.count("D")
                buf_count[12] += line.count("W")
                buf_count[13] += line.count("P")
                buf_count[14] += line.count("Q")
                buf_count[15] += line.count("N")
                buf_count[16] += line.count("S")
                buf_count[17] += line.count("T")
                buf_count[18] += line.count("C")
                buf_count[19] += line.count("M")
                buf_count[20] += line.count("_")
            else:
                if line.find("SEQ") >= 0:
                    line = str(line.split(":")[1]) # attetniton overwriting line here
                    buf_count[0] += line.count("A")
                    buf_count[1] += line.count("G")
                    buf_count[2] += line.count("L")
                    buf_count[3] += line.count("V")
                    buf_count[4] += line.count("I")
                    buf_count[5] += line.count("F")
                    buf_count[6] += line.count("Y")
                    buf_count[7] += line.count("R")
                    buf_count[8] += line.count("K")
                    buf_count[9] += line.count("H")
                    buf_count[10] += line.count("E")
                    buf_count[11] += line.count("D")
                    buf_count[12] += line.count("W")
                    buf_count[13] += line.count("P")
                    buf_count[14] += line.count("Q")
                    buf_count[15] += line.count("N")
                    buf_count[16] += line.count("S")
                    buf_count[17] += line.count("T")
                    buf_count[18] += line.count("C")
                    buf_count[19] += line.count("M")
                    buf_count[20] += line.count("_")
        line = input_file.readline()
    if input_path.find("uORF")>=0 and input_path.find("random")<0:
        stats_peptides.write("original[uORF];")
    elif input_path.find("uORF")>=0 and input_path.find("random")>=0:
        stats_peptides.write("random[uORF];")
    elif input_path.find("uORF")<0 and input_path.find("random")<0:
        stats_peptides.write("original;")
    else:
        stats_peptides.write("random;")
    stats_peptides.write("absolute;")
    stats_peptides.write(str(sum(buf_count)) + ";" + str(buf_count[0]) + ";" + str(buf_count[1]) + ";" + str(buf_count[2]) + ";" + str(buf_count[3]) + ";" + str(buf_count[4]) + ";" + str(buf_count[5]) + ";" + str(buf_count[6]) + ";" + str(buf_count[7]) + ";" + str(buf_count[8]) + ";" + str(buf_count[9]) + ";" + str(buf_count[10]) + ";" + str(buf_count[11]) + ";" + str(buf_count[12]) + ";" + str(buf_count[13]) + ";" + str(buf_count[14]) + ";" + str(buf_count[15]) + ";" + str(buf_count[16]) + ";" + str(buf_count[17]) + ";" + str(buf_count[18]) + ";" + str(buf_count[19]) + ";" + str(buf_count[20]) + ";")
    stats_peptides.write("\n")
    if input_path.find("uORF")>=0 and input_path.find("random")<0:
        stats_peptides.write("original[uORF];")
    elif input_path.find("uORF")>=0 and input_path.find("random")>=0:
        stats_peptides.write("random[uORF];")
    elif input_path.find("uORF")<0 and input_path.find("random")<0:
        stats_peptides.write("original;")
    else:
        stats_peptides.write("random;")
    stats_peptides.write("relative;")
    stats_peptides.write(str(sum(buf_count)) + ";" + str(float(round(buf_count[0]/sum(buf_count)*100,2))) + ";" + str(float(round(buf_count[1]/sum(buf_count)*100,2))) + ";" + str(float(round(buf_count[2]/sum(buf_count)*100,2))) + ";" + str(float(round(buf_count[3]/sum(buf_count)*100,2))) + ";" + str(float(round(buf_count[4]/sum(buf_count)*100,2))) + ";" + str(float(round(buf_count[5]/sum(buf_count)*100,2))) + ";" + str(float(round(buf_count[6]/sum(buf_count)*100,2))) + ";" + str(float(round(buf_count[7]/sum(buf_count)*100,2))) + ";" + str(float(round(buf_count[8]/sum(buf_count)*100,2))) + ";" + str(float(round(buf_count[9]/sum(buf_count)*100,2))) + ";" + str(float(round(buf_count[10]/sum(buf_count)*100,2))) + ";" + str(float(round(buf_count[11]/sum(buf_count)*100,2))) + ";" + str(float(round(buf_count[12]/sum(buf_count)*100,2))) + ";" + str(float(round(buf_count[13]/sum(buf_count)*100,2))) + ";" + str(float(round(buf_count[14]/sum(buf_count)*100,2))) + ";" + str(float(round(buf_count[15]/sum(buf_count)*100,2))) + ";" + str(float(round(buf_count[16]/sum(buf_count)*100,2))) + ";" + str(float(round(buf_count[17]/sum(buf_count)*100,2))) + ";" + str(float(round(buf_count[18]/sum(buf_count)*100,2))) + ";" + str(float(round(buf_count[19]/sum(buf_count)*100,2))) + ";" + str(float(round(buf_count[20]/sum(buf_count)*100,2))) + ";")
    stats_peptides.write("\n")  
stats_peptides.close()
input_file.close()