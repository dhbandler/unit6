#Daniel Bandler
#5/11/18
#palindromes.py


file = open("engmix.txt")


for line in file:
    line = line.split()
    if line == line.reverse():
        print(line)
