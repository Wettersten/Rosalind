#Find the Most Frequent Words with Mismatches in a String
#using earlier created hamming_distance
#need hamming distance, a list of kmers and a function to find kmer-mismatches in dna

import import_ipynb #used to import ipynb notebooks - pip install import_ipynb (anaconda)
from BA1G import hamming_distance
import itertools



def read_file(filename):
    with open(filename, 'r') as file:
        dna = file.readline().strip()
        k,d = file.readline().strip().split()
        
        return str(dna), int(k), int(d)
    
def kmer_dict(k): #create dictionary for all kmers possible, with values 0 at start
    kmer_dict = {} #dictionary
    kmers = map(''.join,itertools.product('ACGT', repeat=k)) #creates all kmers, ACGT, ACGG...
    
    for kmer in kmers:
        kmer_dict[kmer] = 0 #adds all kmers into dictionary with a start value of 0
        
    return kmer_dict
    
def most_frequent_mismatches(dna,k,d):
    kmers = kmer_dict(k)

    for i in range(len(dna)-k+1):
        curr = (dna[i:i+k])
        for kmer in kmers:
            if hamming_distance(kmer, curr) <= d:
                kmers[kmer] += 1

    counts = kmers.values()
    highest = max(counts)

    highest_kmers = ""
    for kmer in kmers:
        if kmers[kmer] == highest:
            highest_kmers += str(kmer) + " "

    return highest_kmers

dna, k, d = read_file("rosalind_ba1i.txt")
print(most_frequent_mismatches(dna,k,d))