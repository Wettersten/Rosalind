#Find a Position in a Genome Minimizing the Skew
#Skew is the diff between c and g (c-1, g+1), find the indices where the skew is minimum

#solution works but is slow, optimize finding min indices

dna = "CCTATCGGTGGATTAGCATGTCCCTGTACGTTTCGCCGCGAACTAGTTCACACGGCTTGATGGCAAATGGTTTTTCCGGCGACCGTAATCGTCCACCGAG"

def skew_problem(dna):
    skew = 0
    skew_list = []
    skew_list.append(skew)
    for nuc in dna:
        if nuc == "C":
            skew -= 1
            skew_list.append(skew)
        elif nuc == "G":
            skew += 1
            skew_list.append(skew)
        else:
            skew_list.append(skew)
    
    skew_indices = ""
    skew_min = min(skew_list)
    for i in range(len(skew_list)):
        if skew_list[i] == skew_min:
            skew_indices += " " + str(i)
        
    
    return(skew_indices)

print((skew_problem(dna)))