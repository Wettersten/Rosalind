from Bio.Seq import Seq
from Bio.Alphabet import IUPAC
from Bio import SeqIO

input_file = SeqIO.parse("rosalind_bphr.txt", "fastq") #input file and its format
sequences = [record for record in input_file] #reads all from file, stored as sequencerecord
qual_lim = 26


hits = 0
for i in range(len(sequences[0].seq)):
    curr_qual = 0
    for k in range(len(sequences)):
        print
        curr_qual += sequences[k].letter_annotations["phred_quality"][i]
    if(curr_qual/len(sequences) < qual):
        hits += 1
    #print(curr_qual/len(sequences))
            
#print(hits)