# Rosalind - Counting Point Mutations (HAMM)
# https://rosalind.info/problems/hamm/
#
# Problem: given two DNA strings of equal length, count the
# number of positions where they differ (the Hamming distance).
#
# Status: solved independently. Approach 2 (zip) written after
# a pointer toward zip() for pairing up characters.

# Approach 1: loop through positions by index, compare characters
with open("rosalind_hamm.txt", "r") as file:
    strand1 = file.readline().strip()
    strand2 = file.readline().strip()

distance = 0
for i in range(len(strand1)):
    if strand1[i] != strand2[i]:
        distance += 1

print(distance)


# Approach 2: zip(strand1, strand2) pairs up the two strings
# position by position - (s1[0], s2[0]), (s1[1], s2[1]), etc.
with open("rosalind_hamm.txt", "r") as file:
    strand1 = file.readline().strip()
    strand2 = file.readline().strip()

distance = sum(1 for b1, b2 in zip(strand1, strand2) if b1 != b2)

print(distance)
