import sys
input_path = sys.argv[1]
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

input_file = open(input_path, "r")
output_file = open("aa_" + input_path, "w")
line = input_file.readline()
while line:
    if line.startswith(">"):
        output_file.write(line)
    else:
        if line.startswith("uORF"):
            if line.find("SEQ")>=0:
                buf = str(line.split(":")[1])
                peptide = get_peptideseq(buf.replace("\n", ""))
                output_file.write(peptide + "\n")
        else:
            peptide = get_peptideseq(line.replace("\n", ""))
            output_file.write(peptide + "\n")
    line = input_file.readline()
if err_flag:
    print("Error (1): not dividable by 3")
input_file.close()
output_file.close()