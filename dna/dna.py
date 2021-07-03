#!/usr/bin/env python3
from numpy import zeros

#dna = "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"
f = open("rosalind_dna.txt", "r")
dna = f.read()
nucs = ['A', 'C', 'G', 'T']
counts = zeros(len(nucs),dtype=int)
for i, nuc in enumerate(nucs):
    counts[i] += dna.count(nuc)
    print(counts[i],end=' ')
print("")
