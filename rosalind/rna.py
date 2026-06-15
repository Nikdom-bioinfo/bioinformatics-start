# Rosalind - Transcribing DNA into RNA (RNA)
# https://rosalind.info/problems/rna/
#
# Problem: given a DNA string, transcribe it into RNA by
# replacing every T with U.
#
# Status: solved independently, both approaches.

# Approach 1: simple string replacement
with open("rosalind_rna.txt", "r") as file:
    t = file.read().strip()

u = t.replace('T', 'U')
print(u)


# Approach 2: same thing using a regular expression
# re.sub(pattern, replacement, string) finds all matches of
# 'pattern' and swaps them for 'replacement'
import re

with open("rosalind_rna.txt", "r") as file:
    t = file.read().strip()

u = re.sub(r"T", "U", t)
print(u)