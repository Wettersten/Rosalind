from Bio import SeqIO
from operator import ne

# Read the input data.
with open('rosalind_subo.txt') as input_data:
    dna = [fasta.seq for fasta in SeqIO.parse(input_data, 'fasta')]

# Run LALIGN with +4/-8 Matrix, -8 Gap Open/Extend, and pick the 100% match.
r = "AGCGGCGAGCAATAATCCCGGACGCCTAATGGATCGA"

def HammingDistance(seq1, seq2):
    'Returns the Hamming distance between equal-length sequences.'
    if len(seq1) != len(seq2):
        raise ValueError('Undefined for sequences of unequal length.')
    return sum(map(ne, seq1, seq2))

# Count the number of occurences in each sequence.
count = [sum([HammingDistance(dna[seq_num][i:i+len(r)], r) <= 3 for i in range(len(dna[seq_num]) - len(r) + 1)]) for seq_num in range(2)]

# Print and save the answer.
print(' '.join(map(str, count)))