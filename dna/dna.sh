for nuc in 'A' 'C' 'G' 'T'
do 
    count=$(grep -o $nuc rosalind_dna.txt | wc -l)
    echo -n "$count "
done
