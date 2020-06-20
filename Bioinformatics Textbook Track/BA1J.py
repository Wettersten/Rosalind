#Find Frequent Words with Mismatches and Reverse Complements
#using ba1i solution with addtional check for reverse complements
import import_ipynb #imports ipython notebooks
from BA1G import hamming_distance
from BA1I import read_file, kmer_dict
import itertools
from Bio.Seq import Seq
from Bio.Alphabet import generic_dna

def most_frequent_mismatches_rev(dna,k,d):
    kmers = kmer_dict(k)

    for i in range(len(dna)-k+1):
        curr = (dna[i:i+k])
        for kmer in kmers:
            if hamming_distance(kmer, curr) <= d:
                kmers[kmer] += 1
            if hamming_distance(kmer, Seq(curr, generic_dna).reverse_complement()) <= d:
                kmers[kmer] += 1

    counts = kmers.values()
    highest = max(counts)

    highest_kmers = ""
    for kmer in kmers:
        if kmers[kmer] == highest:
            highest_kmers += str(kmer) + " "

    return highest_kmers

dna, k, d = read_file("rosalind_ba1j.txt")
print(most_frequent_mismatches(dna,k,d))