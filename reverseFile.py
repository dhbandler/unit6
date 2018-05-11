#Daniel Bandler
#5/10/18
#reverseFile.py prints out palindrome

fileForOpen = input("enter a file name here")
file = open(fileForOpen) 

lines = []
for line in file:
    lines.append(line.split())

print(lines.reverse())


"""
ask for file
open file
make empty list
for loop that goes through each line
    add each line to list
reverse list
print out each line in list
"""
