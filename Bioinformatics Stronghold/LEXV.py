import itertools


def createKmerDict(n, lang): #creates an index of all kmers "lexicographically" using custom language
    unsort_list = []
    temp_list = []
    kmer_dict = []

    for i in range(1,n+1): #creates all kmers of length n
        temp_list = list(itertools.product(lang, repeat=i))
        unsort_list += temp_list

    temp_kmer = ""
    for kmer in unsort_list: #appends as words in list
        for nt in kmer:
            temp_kmer += nt
        kmer_dict.append(temp_kmer)
        temp_kmer = ""

    return(kmer_dict) #returns list of n length kmers, ordered according to lang

def sortKmers(kmer_list, lang): #sorts the kmers in the list lexicographically with regards to word length using custome language
    sorted_list = []
    sorted_list = sorted(kmer_list, key=lambda word: [lang.index(c) for c in word])
    
    return sorted_list

def formatOutput(res_list): #formats to fit rosalind output
    output_str = ""
    for word in res_list:
        output_str += word
        output_str += "\n"
        
    return output_str
	
