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

#Program 2
file = open("engmix.txt")

word = []

for line in file:
    for ch in line:
        word.append(ch)
    if len(word) >= 9:
        if word[0] == word[4] and word[0] == word[8]:
            print(line)
            break
    word = []
        