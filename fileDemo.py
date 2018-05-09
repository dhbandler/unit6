#Daniel Bandler
#5/9/18
#fileDemo.py finding file

file = open("engmix.txt")

numWords = 0
for line in file:
    if "dan" in line:
        print(line.strip())
    numWords += 1
    
print(numWords)
