#!/usr/bin/env python3

REVERSE = {'A':'T',
           'T':'A',
           'C':'G',
           'G':'C'}

# Open file cleanly
with open("rosalind_revc.txt", "r") as f:
    dna = f.read()
# Translate according to the dictionary
for nuc in dna[::-1]:
    if nuc in REVERSE: # guard against garbage
        print(REVERSE[nuc],end="")
