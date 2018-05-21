#Daniel Bandler
#5/21/18
#quiz6.py --- tests brains

"""
#Program #1:
file = open("engmix.txt")

let = input("Type a letter")

letInLine = 0

for line in file:
    line = line.strip()
    for ch in line:
        if ch == let:
            letInLine += 1
        if letInLine == 4:
            print(line)
    letInLine = 0
"""
"""
#Program 2
file = open("engmix.txt")

word = []

for line in file:
    line = line.strip()
    for ch in line:
        word.append(ch)
    if len(word) >= 9:
        if word[0] == word[4] and word[0] == word[8]:
            print(line)
            break
    word = []
"""

"""
#Program 3
numLength =int(input("Input a number "))
firstLet = input("type a letter ")
file = open("engmix.txt")
word = []

for line in file:
    line = line.strip()
    if len(line) == numLength:
            for ch in line:
                word.append(ch)
            if word[0] == firstLet:
                print(line)
            word = []

"""
"""
#Program 4

file = open("engmix.txt")
totalNum = 0

for line in file:
    line = line.strip()
    if len(line) >= 10:
        totalNum += 1
    if totalNum == 8000:
        print(line)
        break
"""
"""
#Program 5 (Not working; please disregard):
file = open("engmix.txt")

vowelCount = 0
vowelMax = 0
longestWord = " "


for line in file:
    line = line.strip()
    break
    vowelCount = line.count("a") + line.count("e") + line.count("i") + line.count("o") + line.count("u")
    if vowelCount > vowelMax:
        vowelMax = vowelCount
        longestWord = line
    vowelCount = 0
print(line)
print(vowelCount)

"""

    
    
    
    


        