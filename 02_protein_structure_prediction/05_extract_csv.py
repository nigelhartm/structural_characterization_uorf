import pandas as pd
import sys

input_path = sys.argv[1]

df = pd.read_csv(input_path, header=None)
df.columns = ['ID', 'RES', 'AA', 'STRUCT']

print("AA:")
print("".join(df['AA'].tolist()))
print("STRUCT:")
struct_str = "".join(df['STRUCT'].tolist())

# H = α-helix
# B = residue in isolated beta-bridge
# E = extended strand, participates in beta ladder
# G = 3-helix (310 helix)
# I = 5 helix (pi-helix)
# T = hydrogen bonded turn
# S = bend 
#   = A blank in the DSSP secondary structure determination stands for loop or irregular.

#struct_str.replace("H", "H")
struct_str = struct_str.replace("G", "H")
struct_str = struct_str.replace("I", "H")
struct_str = struct_str.replace("T", "C")
struct_str = struct_str.replace("S", "C") # need to be before converting to s
struct_str = struct_str.replace(" ", "C")
struct_str = struct_str.replace("B", "S")
struct_str = struct_str.replace("E", "S")

print(struct_str)