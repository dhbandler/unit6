#Daniel Bandler
#5/16/18
#E_Coli.py gives you explosive bowel problems

genome = open("E_coli_genome.txt")

for i in genome:
    genome.replace("T","U")
print(genome)

