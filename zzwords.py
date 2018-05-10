#Daniel Bandler
#5/10/18
#zzwords.py prints out all words in dictionay with zz

file = open("engmix.txt")

for line in file:
    if "zz" in line:
        print(line)
