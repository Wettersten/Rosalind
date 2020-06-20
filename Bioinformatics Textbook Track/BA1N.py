#Generate the d-Neighborhood of a String
import import_ipynb
import itertools
from basics import hamming_distance, kmer_list

def read_file(filename):
    with open(filename, 'r') as file:
        dna = file.readline().strip()
        d = file.readline().strip()
        
        return str(dna), int(d)

""" #recursive code attempt
def neighbors(pattern, d):
    if d == 0:
        return pattern
    if len(pattern) == 1:
        return ["A", "C", "G", "T"]
    neighborhood = []
    suffix_neighbors = neighbors(pattern[1:], d)
    
    for text in suffix_neighbors:
        if hamming_distance() 
"""

def neighbors(pattern, d):
    kmers = kmer_list(len(pattern))
    neighborhood = []
    
    for i in range(len(kmers)):
        if hamming_distance(pattern, kmers[i]) <= d:
            neighborhood.append(kmers[i])
    
    file = open('res_ba1n.txt', 'w+')
    for hit in neighborhood:
        file.writelines(str(hit) + "\n")
    
    return neighborhood

dna, d = read_file("rosalind_ba1n.txt")
neighbors(dna, d)