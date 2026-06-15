# Rosalind - Counting DNA Nucleotides (DNA)
# https://rosalind.info/problems/dna/
#
# Problem: given a DNA string, count how many times each of
# A, C, G, T appears, and print the counts in that order.
#
# Status: solved independently, with a pointer toward using a
# dictionary for the second approach below.

# Approach 1: count each base individually with .count()
with open("rosalind_dna.txt", "r") as file:
    dna = file.read().strip()

a = dna.count('A')
c = dna.count('C')
g = dna.count('G')
t = dna.count('T')

print(f"{a} {c} {g} {t}")


# Approach 2: loop through the sequence once, tallying into a dict
with open("rosalind_dna.txt", "r") as file:
    dna = file.read().strip()

counts = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
for nucleotide in dna:
    if nucleotide in counts:
        counts[nucleotide] += 1

print(f"{counts['A']} {counts['C']} {counts['G']} {counts['T']}")