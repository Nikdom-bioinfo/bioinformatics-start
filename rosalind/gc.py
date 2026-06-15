# Rosalind - Computing GC Content (GC)
# https://rosalind.info/problems/gc/
#
# Problem: given several DNA strings in FASTA format, find the
# one with the highest GC-content (percentage of G and C bases)
# and print its ID and that percentage.
#
# Status: needed help with the overall approach (splitting the
# FASTA file into records, tracking a running maximum) 

with open("rosalind_gc.txt", "r") as file:
    # FASTA records are separated by '>', so splitting on it
    # gives us one chunk of text per sequence
    samples = file.read().strip().split('>')

highest_id = ""
highest_gc = 0.0

for sample in samples:
    if not sample:
        continue  # the first split chunk is empty, skip it

    # first line is the sequence ID, the rest is the DNA,
    # possibly spread across multiple lines
    lines = sample.splitlines()
    sample_id = lines[0]
    dna = "".join(lines[1:])

    g_count = dna.count('G')
    c_count = dna.count('C')
    gc_percentage = ((g_count + c_count) / len(dna)) * 100

    if gc_percentage > highest_gc:
        highest_gc = gc_percentage
        highest_id = sample_id

print(highest_id)
print(f"{highest_gc:.6f}")
