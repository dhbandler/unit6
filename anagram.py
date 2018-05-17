#Daniel Bandler
#5/17/18
#anagram.py prints out all anagrams of word in dictionary

file = open("engmix.txt")

word1 = input("what is the word you want to anagramize? ")

word1List = []
word2List = []

for char in word1:
    word1List.append(char)
    word1List.sort()

for line in file:
    line = line.strip()
    for let in line:
        word2List.append(let)
        word2List.sort()
    if word2List == word1List:
        print(line)
    word2List = []