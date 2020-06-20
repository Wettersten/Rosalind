#Compute the Hamming Distance Between Two Strings

dna1 = "GGGCCGTTGGT"
dna2 = "GGACCGTTGAC"

def hamming_distance(dna1, dna2):
    return sum(ch1 != ch2 for ch1, ch2 in zip(dna1, dna2))

print(hamming_distance(dna1,dna2))