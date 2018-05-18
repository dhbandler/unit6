#Daniel Bandler
#5/18/18
#testreview.py

"""
#1 find all word in dictionary that have 3 letter "c"s and 2 letter "p"s

file = open("engmix.txt")


for line in file:

    if line.count("p") == 2 and line.count("c") == 3:
        print(line)

"""
#2 print out words that start with letter r    

file = open("engmix.txt")
wordList = []
wordCount = 0
for line in file:
    for let in line:
        wordList.append(let)
    if wordList[0] == "r":
        wordCount += 1  
    wordList = []
    print(wordCount)

