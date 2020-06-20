from Bio.Seq import Seq
from Bio.Alphabet import IUPAC
from Bio import SeqIO

input_file = SeqIO.parse("rosalind_rvco.txt", "fasta") #input file and its format
sequences = [record for record in input_file] #reads all from file, stored as sequencerecord


hits = 0
for seqs in sequences: #loops all sequences,
    if str((seqs.seq).reverse_complement()) == str((seqs.seq)): #if any sequence is identical to its reverse compliment
        hits += 1 #count the matches
        
print(hits)