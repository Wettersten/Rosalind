#Find a Profile-most Probable k-mer in a String
"""
Given: A string Text, an integer k, and a 4 × k matrix Profile.
Return: A Profile-most probable k-mer in Text. (If multiple answers exist, you may return any one.)
"""

def read_file(filename):
    with open(filename, 'r') as file:
        dna = file.readline().strip()
        k = file.readline().strip()
        pmatrix = []
        for item in file:
            temp_list = []
            val_list = item.strip().split()
            for val in val_list:
                temp_list.append(float(val))
            pmatrix.append(temp_list)     
        return dna, int(k), pmatrix
    
def profile_score(profile, pmatrix): #calculates score of current profile
    #pm_dict = {0:'A', 1:'C', 2:'G', 3:'T'}
    pm_dict = {'A':0, 'C':1, 'G':2, 'T':3}
    score = 0
    for i in range(len(profile)):
        score += pmatrix[pm_dict[profile[i]]][i]
        
    
    return round(score,1)

def probable_profile(dna, k, pmatrix): #takes all kmers from dna, calculates their scores and return highest
    profile = ""
    kmers = []
    
    for i in range(len(dna)-k+1):
        kmers.append(dna[i:i+k])
    
    highest = 0
    for kmer in kmers:
        curr = profile_score(kmer, pmatrix)
        if curr > highest:
            profile = kmer
            highest = curr
    
    return profile
    
    
dna, k, pmatrix = read_file('rosalind_ba2c.txt')
print(probable_profile(dna, k, pmatrix))