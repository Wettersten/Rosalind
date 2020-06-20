#Implement MotifEnumeration
"""
Implement MotifEnumeration (shown above) to find all (k, d)-motifs in a collection of strings.
Given: Integers k and d, followed by a collection of strings Dna.
Return: All (k, d)-motifs in Dna.
"""

import import_ipynb
import itertools
from basics import hamming_distance, kmer_list

def read_file(filename):
    with open(filename, 'r') as file:
        k,d = file.readline().strip().split()
        dna = []
        for item in file:
            dna.append(str(item.strip()))
        
        return int(k), int(d), dna
    
def neighbors(pattern, d): #creates all kmers from pattern with at most d mismatches
    kmers = kmer_list(len(pattern))
    neighborhood = []
    
    for i in range(len(kmers)):
        if hamming_distance(pattern, kmers[i]) <= d:
            neighborhood.append(kmers[i])
    
    """
    file = open('res_ba1n.txt', 'w+')
    for hit in neighborhood:
        file.writelines(str(hit) + "\n")
    """
    
    return neighborhood

def motif_enumeration(dna, k, d):
    patterns = []
    for i in range(len(dna[0])-k+1):
        sub_dna = dna[0][i:i+k]
        neighborhood = neighbors(sub_dna, d)
        for neigh in neighborhood:
            hit = 1
            for l in range(len(dna)):
                if not pattern_in_dna_mismatches(neigh, dna[l], d):
                    hit = 0
                    break
            if hit == 1:
                patterns.append(neigh)
    
    clean_patterns = []
    for pattern in patterns:
        if pattern not in clean_patterns:
            clean_patterns.append(pattern)
    
    str_patterns = ""
    for patt in clean_patterns:
        str_patterns += patt + " "
        
        
    return str_patterns

def pattern_in_dna_mismatches(pattern, dna, d):
    k = len(pattern)
    for i in range(len(dna)-k+1):
        sub_dna = dna[i:i+k]
        if hamming_distance(pattern, sub_dna) <= d:
            return True
            break
    return False
        


k, d, dna_list = read_file('rosalind_ba2a.txt')

print(motif_enumeration(dna_list, k, d))
