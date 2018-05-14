#Daniel Bandler
#5/11/18
#palindromes.py


file = open("palindromes.py")


for line in file:
    line = line.split()
    if line == line.reverse():
        print(line)
