#Implement GreedyMotifSearch with Pseudocounts
"""
Given: Integers k and t, followed by a collection of strings Dna.
Return: A collection of strings BestMotifs resulting from running GreedyMotifSearch(Dna, k, t) with pseudocounts. 
    If at any step you find more than one Profile-most probable k-mer in a given string, use the one occurring first.
"""
import import_ipynb
import itertools
from basics import hamming_distance



def read_file(filename):
    with open(filename, 'r') as file:
        k, t = file.readline().strip().split()
        dna_list = []
        for dna in file:
            dna_list.append(dna.strip())
            
    return int(k), int(t), dna_list

def make_profile(kmers): #creates a profile matrix from kmers, where kmers is a list of dna
    profile = [] #the profile matrix is a list of lists, first is the float score for 'A' for all position, 2nd 'C' etc
    pm_dict = {'A':0, 'C':1, 'G':2, 'T':3}
    
    for i in range(4):
        profile.append([])
    
    for i in range(len(kmers[0])):
        temp_count = {'A':0, 'C':0, 'G':0, 'T':0}
        kmers_count = len(kmers)
        for k in range(kmers_count):
            temp_count[kmers[k][i]] += 1
            
        a_score = float(temp_count['A'] / kmers_count)
        c_score = float(temp_count['C'] / kmers_count)
        g_score = float(temp_count['G'] / kmers_count)
        t_score = float(temp_count['T'] / kmers_count)
        profile[pm_dict['A']].append(a_score)
        profile[pm_dict['C']].append(c_score)
        profile[pm_dict['G']].append(g_score)
        profile[pm_dict['T']].append(t_score) 
    
    return profile
    


def profile_score(profile, pmatrix): #calculates score of current profile
    pm_dict = {'A':0, 'C':1, 'G':2, 'T':3}
    score = 0
    for i in range(len(profile)):
        score += pmatrix[pm_dict[profile[i]]][i]
        
    
    return round(score,1)

def score(motif_list):
    pm_dict = {0:'A', 1:'C', 2:'G', 3:'T'}
    score = 0
    profile = make_profile(motif_list)
    median = ""
    for i in range(len(profile[0])):
        highest = 0
        curr = ""
        for k in range(len(profile)):
            if profile[k][i] > highest:
                highest = profile[k][i]
                curr = pm_dict[k]
        median += curr
          
    for motif in motif_list:
        score += hamming_distance(motif, median)
    
    return score




def probable_profile(dna, k, pmatrix): #takes all kmers from dna, calculates their scores and return highest
    pm_dict = {'A':0, 'C':1, 'G':2, 'T':3}
    profile = dna[0:k]
    highest = 0
    
    for i in range(1,len(dna)-k+1):
        curr_high = 1
        kmer = dna[i:i+k]
        
        for j in range(k):
            val  = pm_dict[kmer[j]]
            curr_high *= pmatrix[val][j]
        if curr_high > highest:
            profile = kmer
            highest = curr_high
    
    return profile

def greedy_motif_search(dna, k, t):
    best_motifs = []
    for i in range(len(dna)):
        best_motifs.append(dna[i][0:k])
        
    for i in range(len(dna[0])-k+1):
        motif_list = []
        motif_list.append(dna[0][i:i+k])
        
        for j in range(1,t):
            profile = make_profile(motif_list) #[0:j]?
            motif_list.append(probable_profile(dna[j], k, profile))
            
        if score(motif_list) < score(best_motifs):
            best_motifs = motif_list
    
    return best_motifs

k, t, dna_list = read_file('rosalind_ba2e.txt')
output = (greedy_motif_search(dna_list, k, t))

for item in output:
    print(item)