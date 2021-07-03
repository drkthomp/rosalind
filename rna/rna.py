#!/usr/bin/env python3

f = open("rosalind_rna.txt", "r")
dna = f.read()
print(dna.replace('T', 'U'))
