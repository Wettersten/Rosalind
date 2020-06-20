#Generate the Frequency Array of a String
import itertools


def createKmerDict(n, lang): #creates an index of all kmers lexicographically
    unsort_list = []
    temp_list = []
    kmer_dict = []

    for i in range(n,n+1): #creates all kmers of length n, lexicographicaly using lang as language
        temp_list = list(itertools.product(lang, repeat=i))
        unsort_list += temp_list

    temp_kmer = ""
    for kmer in unsort_list:
        for nt in kmer:
            temp_kmer += nt
        kmer_dict.append(temp_kmer)
        temp_kmer = ""

    return(kmer_dict) #returns list of n length kmers, ordered according to lang

def createKmerResults(kmer_list, seq):
    kmer_count_list = []
    for kmer in kmer_list:
        kmer_count_list.append(0)
    for i in range(len(seq)-n+1):
        temp_kmer = seq[i:i+n]
        for j in range(len(kmer_list)):
            if temp_kmer == kmer_list[j]:
                kmer_count_list[j] += 1

    return(kmer_count_list)

def listCompare(list_res, ros_str):
    ros_list = []
    for res in ros_str:
        if res != " ":
            ros_list.append(int(res))
    equals = True
    for i in range(len(list1)):
        if list_res[i] != ros_list[i]:
            equals = False
    
    return equals

def formatOutput(res_list):
    output_str = ""
    for res in res_list:
        output_str += " "
        output_str += str(res)
        
    return output_str