dna_s = input()
dna_t = input()

def hamming(s,t):
    """Calculate hamming distance between two strings, assumed to be of equal length"""
    dist = 0 
    for (i,j) in zip(s,t):
        if i != j: 
            dist += 1
    return dist

print(hamming(dna_s, dna_t))


