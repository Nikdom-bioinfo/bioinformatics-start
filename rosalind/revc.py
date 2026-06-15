# Rosalind - Complementing a Strand of DNA (REVC)
# https://rosalind.info/problems/revc/
#
# Problem: given a DNA string, return its reverse complement
# (swap A<->T and C<->G, then reverse the order).
#
# Status: Approach 1 solved independently (with a pointer toward
# the lowercase trick). Approach 2 written with AI help, understood
# and adapted to read from the input file like the others.

# Approach 1: replace each base with its complement using a
# temporary lowercase letter first, so a base isn't immediately
# re-swapped by a later replacement (e.g. A->t, then t->a would
# undo it if done in uppercase the whole time)
with open("rosalind_revc.txt", "r") as file:
    s = file.read().strip()

s = s.replace('T', 'a')
s = s.replace('A', 't')
s = s.replace('C', 'g')
s = s.replace('G', 'c')

s = s.upper()
reverse_complement = s[::-1]

print(reverse_complement)


# Approach 2: same result using a dictionary lookup for each base
with open("rosalind_revc.txt", "r") as file:
    s = file.read().strip()

complement = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}
reverse_complement = "".join(complement[base] for base in s[::-1])

print(reverse_complement)