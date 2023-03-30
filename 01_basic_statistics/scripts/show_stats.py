input_file = open("formatted_Araport11_5_utr_20220914.fasta", "r")
N_SEQ = 0
line = input_file.readline()
while line:
    if line.startswith(">"):
        N_SEQ += 1
    else:
        pass
    line = input_file.readline()

input_file = open("longest_formatted_Araport11_5_utr_20220914.fasta", "r")
N_SEQ_OneV = 0
line = input_file.readline()
while line:
    if line.startswith(">"):
        N_SEQ_OneV += 1
    else:
        pass
    line = input_file.readline()

input_file = open("ids_equal0_uORF_longest_formatted_Araport11_5_utr_20220914.txt", "r")
N_0uORF = 0
line = input_file.readline()
while line:
    N_0uORF += 1
    line = input_file.readline()

input_file = open("ids_equal1_uORF_longest_formatted_Araport11_5_utr_20220914.txt", "r")
N_1uORF = 0
line = input_file.readline()
while line:
    N_1uORF += 1
    line = input_file.readline()

input_file = open("ids_equal2_uORF_longest_formatted_Araport11_5_utr_20220914.txt", "r")
N_2uORF = 0
line = input_file.readline()
while line:
    N_2uORF += 1
    line = input_file.readline()

input_file = open("ids_greater2_uORF_longest_formatted_Araport11_5_utr_20220914.txt", "r")
N_greater2uORF = 0
line = input_file.readline()
while line:
    N_greater2uORF += 1
    line = input_file.readline()

input_file = open("uORF_longest_formatted_Araport11_5_utr_20220914.txt", "r")
t1 = 0
t2 = 0
t3 = 0
N_uORF = 0
locMax = 0
globmax = 0
line = input_file.readline()
while line:
    if line.startswith(">"):
        if locMax>globmax:
            globmax=locMax
        locMax = 0
    elif line.find("TYPE")>=0:
        N_uORF += 1
        locMax += 1
        x = int(line.split(":")[1])
        if x==1:
            t1 += 1
        elif x==2:
            t2 += 1
        elif x==3:
            t3 += 1
    line = input_file.readline()

print("\nS T A T S -> \n")
print("Overall Sequences: " + str(N_SEQ))
print("One version per gene: " + str(N_SEQ_OneV))
print("0 uORF: " + str(N_0uORF))
print("1 uORF: " + str(N_1uORF))
print("2 uORF: " + str(N_2uORF))
print("3+ uORF: " + str(N_greater2uORF))
print("max uORF at one gene: " + str(globmax))
print("Overall uORFs: " + str(N_uORF))
print("Type 1 uORF: " + str(t1))
print("Type 2 uORF: " + str(t2))
print("Type 3 uORF: " + str(t3))