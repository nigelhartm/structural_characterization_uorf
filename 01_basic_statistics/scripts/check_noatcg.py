import sys
import random
input_path = sys.argv[1]
input_file = open(input_path, "r")
line = input_file.readline()
while line:
    if line.startswith('>'):
        pass
    else:
        if line.find("B")>=0:
            line.replace("B", B)
        if line.find("D")>=0:
            print("D")
        if line.find("E")>=0:
            print("E")
        if line.find("F")>=0:
            print("F")
        if line.find("H")>=0:
            print("H")
        if line.find("I")>=0:
            print("I")
        if line.find("J")>=0:
            print("J")
        if line.find("K")>=0:
            print("k")
        if line.find("L")>=0:
            print("L")
        if line.find("M")>=0:
            print("M")
        if line.find("N")>=0:
            print("N")
        if line.find("O")>=0:
            print("O")
        if line.find("P")>=0:
            print("P")
        if line.find("Q")>=0:
            print("Q")
        if line.find("R")>=0:
            print("R")
        if line.find("S")>=0:
            print("S")
        if line.find("U")>=0:
            print("U")
        if line.find("V")>=0:
            print("V")
        if line.find("W")>=0:
            print("W")
        if line.find("X")>=0:
            print("X")
        if line.find("Y")>=0:
            print("Y")
        if line.find("Z")>=0:
            print("Z")  
    line = input_file.readline()
input_file.close()