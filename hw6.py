#Daniel Bandler
#5/14/18
#hw6.py


"""
#Program 1
wordlist = ["dog", "cat", "hamburguesa"]
wordguess = input("Guess a word")
if wordguess in wordlist:
    print("yes")
else:
    print("no")
"""
"""
file = open("engmix.txt")

numLines = 0
for line in file:
    numLines += 1
    if numLines == 888:
        print(line.strip())
"""
file = open("palindromes.txt")
for line in file:
    print(line.strip(), "!")
