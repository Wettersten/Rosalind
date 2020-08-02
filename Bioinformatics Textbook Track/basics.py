#Shared methods for rosalind textbook track.
#Legend: description of method, method, example of output
#Uses "import import_ipynb" in other file to import as normal: "import hamming_distance from basics"
#This as original files writtin in iPython
import itertools


#Hamming distance, returns the number of mismatches between two strings.
def hamming_distance(dna1, dna2):
    return sum(ch1 != ch2 for ch1, ch2 in zip(dna1, dna2))
#print(hamming_distance("ACGT", "AGCT")) #2


#Create dictionary for all kmers possible of length k, key = kmer, value = 0 at start.
def kmer_dict(k):
    kmer_dict = {} #dictionary
    kmers = map(''.join,itertools.product('ACGT', repeat=k)) #creates all kmers, ACGT, ACGG...

    for kmer in kmers:
        kmer_dict[kmer] = 0 #adds all kmers into dictionary with a start value of 0

    return kmer_dict
#print(kmer_dict(1)) #{'A': 0, 'C': 0, 'G': 0, 'T': 0}


#Same as kmer_dict but just creates a list of all kmers of length k
def kmer_list(k):
    kmer_list = []
    kmers = map(''.join,itertools.product('ACGT', repeat=k))

    for kmer in kmers:
        kmer_list.append(kmer)

    return kmer_list
#print(kmer_list(2)) #['AA', 'AC', 'AG', 'AT', 'CA', 'CC', 'CG', 'CT', 'GA', 'GC', 'GG', 'GT', 'TA', 'TC', 'TG', 'TT']"


#Creates list of all kmers from pattern with at most d mismatches
def neighbors_d(pattern, d):
    kmers = kmer_list(len(pattern))
    neighborhood = []

    for i in range(len(kmers)):
        if hamming_distance(pattern, kmers[i]) <= d:
            neighborhood.append(kmers[i])

    return neighborhood
#print(neighbors_d("AGT", 1)) #['AAT', 'ACT', 'AGA', 'AGC', 'AGG', 'AGT', 'ATT', 'CGT', 'GGT', 'TGT']


#Checks if pattern exists in dna string with at most d mismatches, true if it is found.
def pattern_in_dna_mismatches(pattern, dna, d):
    k = len(pattern)
    for i in range(len(dna)-k+1):
        sub_dna = dna[i:i+k]
        if hamming_distance(pattern, sub_dna) <= d:
            return True
            break
    return False
#print(pattern_in_dna_mismatches("ATA", "AGC", 2)) #True


def aa_to_nucl(amino):
    nucl = ''
    codon_table = {'A': ['GCU', 'GCC', 'GCA', 'GCG'],
                   'L': ['UUA', 'UUG', 'CUU', 'CUC', 'CUA', 'CUG'],
                   'R': ['CGU', 'CGC', 'CGA', 'CGG', 'AGA', 'AGG'],
                   'K': ['AAA', 'AAG'],
                   'N': ['AAU', 'AAC'],
                   'M': ['AUG'],
                   'D': ['GAU', 'GAC'],
                   'F': ['UUU', 'UUC'],
                   'C': ['UGU', 'UGC'],
                   'P': ['CCU', 'CCC', 'CCA', 'CCG'],
                   'Q': ['CAA', 'CAG'],
                   'S': ['UCU', 'UCC', 'UCA', 'UCG', 'AGU', 'AGC'],
                   'E': ['GAA', 'GAG'],
                   'T': ['ACU', 'ACC', 'ACA', 'ACG'],
                   'G': ['GGU', 'GGC', 'GGA', 'GGG'],
                   'W': ['UGG'],
                   'H': ['CAU', 'CAC'],
                   'Y': ['UAU', 'UAC'],
                   'I': ['AUU', 'AUC', 'AUA'],
                   'V': ['GUU', 'GUC', 'GUA', 'GUG'],
                   'Stop': ['UAG', 'UGA', 'UAA']}
    return codon_table[amino]


def nucl_to_aa(nucl):
    codon_table = {'GCU': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A', 'UUA': 'L',
                   'UUG': 'L', 'CUU': 'L', 'CUC': 'L', 'CUA': 'L', 'CUG': 'L',
                   'CGU': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R', 'AGA': 'R',
                   'AGG': 'R', 'AAA': 'K', 'AAG': 'K', 'AAU': 'N', 'AAC': 'N',
                   'AUG': 'M', 'GAU': 'D', 'GAC': 'D', 'UUU': 'F', 'UUC': 'F',
                   'UGU': 'C', 'UGC': 'C', 'CCU': 'P', 'CCC': 'P', 'CCA': 'P',
                   'CCG': 'P', 'CAA': 'Q', 'CAG': 'Q', 'UCU': 'S', 'UCC': 'S',
                   'UCA': 'S', 'UCG': 'S', 'AGU': 'S', 'AGC': 'S', 'GAA': 'E',
                   'GAG': 'E', 'ACU': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T',
                   'GGU': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G', 'UGG': 'W',
                   'CAU': 'H', 'CAC': 'H', 'UAU': 'Y', 'UAC': 'Y', 'AUU': 'I',
                   'AUC': 'I', 'AUA': 'I', 'GUU': 'V', 'GUC': 'V', 'GUA': 'V',
                   'GUG': 'V', 'UAG': 'Stop', 'UGA': 'Stop', 'UAA': 'Stop'}
    return codon_table[nucl]
