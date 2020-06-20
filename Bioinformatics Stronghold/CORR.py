def readGenome(filename):
    genome = ''
    seqs = []
    with open(filename, 'r') as f:
        f.readline()
        for line in f:
            # ignore header line with genome information
            if line[0] == '>' and len(genome) > 0:
                seqs.append(genome)
                genome = ''
            if not line[0] == '>':
                genome += line.rstrip()
    if len(genome) > 0:
        seqs.append(genome)
    return seqs
    
r_seqs = readGenome('rosalind_corr.txt')

def reverseComplement(s):
    complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
    t = ''
    for base in s:
        t = complement[base] + t
    return t
    
#print(reverseComplement(r_seqs[0]))
corr_seqs = []
incorr_seqs = []
for seq in r_seqs:
    if seq not in incorr_seqs:
        incorr_seqs.append(seq)
    elif seq in incorr_seqs:
        if seq not in corr_seqs:
            corr_seqs.append(seq)
            
for seq in corr_seqs:
    if seq in incorr_seqs:
        incorr_seqs.remove(seq)
    elif reverseComplement(seq) in incorr_seqs:
        incorr_seqs.remove(reverseComplement(seq))

#print(incorr_seqs)
#print(corr_seqs)

dict_seqs = dict()
for seq in r_seqs:
    if seq not in dict_seqs:
        dict_seqs[seq] = 1
    #elif reverseComplement(seq) not in dict_seqs:
        #dict_seqs[reverseComplement(seq)] = 1    
    
    elif seq in dict_seqs:
        dict_seqs[seq] += 1
        
for seq in dict_seqs:
    if dict_seqs[seq] == 1:
        if reverseComplement(seq) in dict_seqs:
            dict_seqs[seq] += 1
            dict_seqs[reverseComplement(seq)] += 1
    
temp_list = []    
for seq in dict_seqs:
    if dict_seqs[seq] > 1 and reverseComplement(seq) not in dict_seqs:
        temp_list.append(reverseComplement(seq))
        
for temp in temp_list:
    dict_seqs[temp] = 2

dict_list = []
for seq in dict_seqs:
    if dict_seqs[seq] > 1:
        dict_list.append(seq)
    
print(dict_seqs)
#print(dict_list)

def editDistance(x, y):
    D = [] #array of length x, y
    for i in range(len(x)+1):
        D.append([0]* (len(y)+1))
        
    for i in range(len(x)+1): # fills in first row with 0, 1, 2...
        D[i][0] = i
    for i in range(len(y)+1): # fills in first column with 0, 1, 2...
        D[0][i] = i    
        
    for i in range(1, len(x)+1): #every row (skipping first)
        for j in range(1, len(y)+1): #every column (skipping first)
            distHor = D[i][j-1] + 1
            distVer = D[i-1][j] + 1
            if x[i-1] == y[j-1]:
                distDiag = D[i-1][j-1]
            else:
                distDiag = D[i-1][j-1] + 1
            D[i][j] = min(distHor, distVer, distDiag)
    return D[-1][-1] #returns very bottom value
    
corr_output = []
incorr_output = []
for seq in dict_seqs:
    if dict_seqs[seq] == 1:
        for corr in dict_list:
            if editDistance(seq, corr) == 1:
                incorr_output.append(seq)
                corr_output.append(corr)


for i in range(len(incorr_output)):                
    print('%s->%s' %(incorr_output[i], corr_output[i]))

                
#print(editDistance(dict_seqs[0], dict_seqs[1]))
#for every seq that has value 1 in dict_seqs:
    #aprrox match seq or rc(seq), 1 mismatch
    #save seq and match in list
    #printout list match->correction, repeat