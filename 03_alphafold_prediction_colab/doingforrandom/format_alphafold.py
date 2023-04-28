import sys
err_flag = False
def get_peptideseq(seq):
    global err_flag
    table = {
        'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
        'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
        'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
        'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',                 
        'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
        'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
        'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
        'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
        'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
        'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
        'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
        'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
        'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
        'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
        'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
        'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W',
    }
    protein =""
    if len(seq)%3 == 0:
        for i in range(0, len(seq), 3):
            codon = seq[i:i + 3]
            protein += table[codon]
    else:
        for i in range(0, len(seq)-len(seq)%3, 3):
            codon = seq[i:i + 3]
            protein += table[codon]
        err_flag = True
    return protein

input_path = sys.argv[1]
input_file = open(input_path, "r")
output_file = open("out_"+input_path, "w")
head=""
seq=""
leng = 0
line = input_file.readline()
#t=0
while line:
    #if t>=3:
    #    break
    if line.startswith(">"):
        head=line
        head = head.replace("\n", "")
        head = head.split(" ")[0].replace(">", "").replace(".", "_")
    else:
        if line.find("SEQ:") >= 0:
            seq = line.split(":")[1]
        if line.find("LENGTH:") >= 0:
            leng = int(line.split(":")[1])
        if line.find("TYPE:") >= 0:
            typ = int(line.split(":")[1])
            if (typ == 1 or typ == 2) and leng >= 50 and leng <= 200:
                id = int(line.split("_")[1])
                #print("\'"+head+"_uORF_"+str(id)+"\',\'"+seq.replace("\n", "")+"\',")
                #break
                seq = get_peptideseq(seq.replace("\n", "")).replace("_", "")
                output_file.write("\'"+head+"_uORF_"+str(id)+"\',\'"+seq.replace("\n", "")+"\',\n")
                #t+=1
    line = input_file.readline()
input_file.close()
output_file.close()
