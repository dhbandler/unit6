#Daniel Bandler
#5/21/18
#quiz6.py --- tests brains

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
