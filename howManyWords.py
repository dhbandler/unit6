#Daniel Bandler
#5/10/18
#howManyWords.py prints out how many words per number of letter

file = open("engmix.txt")

length = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

for line in file:
    length[len(line.strip())-1] += 1

times = 1
while times <= len(length):
    print(times, "-lettter words: ", length[times-1])
    times += 1

