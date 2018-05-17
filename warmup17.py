#Daniel Bandler
#5/17/18
#warmup17.py - checks for letters of name in dictionart

file = open("engmix.txt")

for line in file:
    line = line.strip()
    if "b" in line and "a" in line and "n" in line and "d" in line and "l" in line and "e" in line and "r" in line:
        print(line)
