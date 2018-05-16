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


file = open("engmix.txt")

word = input("guess a word ")
for line in file:
    line = line.strip()
    if word == line:
        print("in dictionary")
        inD = True
        break
    
if not inD:
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
"""
file = open("warmup16.py")
for line in file:
    print(line.strip(), "!")
"""

file = open("engmix.txt")
letter = input("Type a letter here.  ")
mostLetters = []
letterCount = 0

for letter in "abcdefghijklmnopqrstuvwxyz"

for line in file:
    lineLetter = line.count(letter)
    if lineLetter > letterCount:
        letterCount = lineLetter
        mostLetters = line.strip()
            
print(mostLetters)




    
    
  
