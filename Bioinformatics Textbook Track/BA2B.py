#Find a Median String
import import_ipynb
from basics import hamming_distance

"""
Given: An integer k and a collection of strings Dna.
Return: A k-mer Pattern that minimizes d(Pattern, Dna) over all k-mers Pattern. 
(If multiple answers exist, you may return any one.)
"""

def read_file(filename):
    with open(filename, 'r') as file:
        k = file.readline().strip()
        dna = []
        for item in file:
            dna.append(item.strip())        
        return dna, int(k)

def kmer_dict(dna_list, k): #create dict with all possible kmers from a list of dna strings
    kmer_dict = {} #dictionary
    kmers = []
    rem_dupl = []
    for dna in dna_list:
        for i in range(len(dna)-k+1):
            kmers.append(dna[i:i+k])
        
    for dupl in kmers:
        if dupl not in rem_dupl:
            rem_dupl.append(dupl)
    
    for kmer in rem_dupl:
        kmer_dict[kmer] = 0 #adds all kmers into dictionary with a start value of 0
        
    return kmer_dict

def median_string(dna_list, k):
    kmers = kmer_dict(dna_list, k)
    
    for kmer in kmers:
        for dna in dna_list:
            curr_d = 9999
            for i in range(len(dna)-k+1):
                sub_dna  = dna[i:i+k]
                h_d = hamming_distance(sub_dna, kmer) 
                if h_d < curr_d:
                    curr_d = h_d
            kmers[kmer] = kmers[kmer] + curr_d
    
    min_hit = min(kmers.values())
    for kmer in kmers:
        if kmers[kmer] == min_hit:
            return kmer
    
    return "Error"
    
dna_list, k = read_file('rosalind_ba2b.txt')
print((median_string(dna_list, k)))
