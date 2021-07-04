#!/usr/bin/env python3

gc = {}
with open("rosalind_gc.txt", "r") as f:
    raw_gc =  raw_at = 0
    key = ""
    for line in f:
        if line[0] == '>': # aka if its a header
            if raw_at + raw_gc > 0:  # if we've read something before
                gc[key] = raw_gc / (raw_gc + raw_at)  # store it
            key = line[1:].strip() # then proceed to the next key 
            # and reset the counts 
            raw_gc = 0 
            raw_at = 0
        else:
            raw_gc += line.count('G') + line.count('C')
            raw_at += line.count('A') + line.count('T')
    if raw_at + raw_gc > 0:  # if we've read something before
        gc[key] = raw_gc / (raw_gc + raw_at)  # store it

max_gc = max(gc, key=gc.get)
print(max_gc)
print(gc[max_gc] * 100)
