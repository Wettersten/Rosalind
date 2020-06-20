from math import factorial

#puts in dna string, counts number of A's and C's (same as U/G)
#total number of matchins is the multiplication of #A! * #C!
#gets all possible permutations of perfect matches
def matchings(dna): 
    return factorial(dna.count("A")) * factorial(dna.count("C"))

print(matchings("GCCAUGGAGUGGGCCAGCAUAAUCCUUCGAUCCUACUAGCGCCCAUAGGGCUAAGUUCUGUGCAGGACAU"))