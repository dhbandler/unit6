#Daniel Bandler
#5/10/18
#longestDictionaryWOrd.py prints out longest word in dictionary


file = open("engmix.txt")

longestWord = []

for line in file:
    if len(line) > len(longestWord):
        longestWord = line

    
print(longestWord)
