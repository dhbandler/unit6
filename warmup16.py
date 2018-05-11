#Daniel Bandler
#5/11/18
#fileDemo.py finding file

file = open("engmix.txt")

for line in file:
    line = line.strip()
    if len(line) > 0 and line[0] == "d" and line[-1] == "b":
        print(line)

    
