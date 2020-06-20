#N-glycosylation is N{P}[ST]{P}
#[XY] = either x or y. {x} means any except x.
import re
import urllib
from urllib.request import urlopen

dataset_list = []
#tempO = open('rosalind_mprt.txt','r')
#for line in tempO:
#	dataset_list.append(str(line))
#tempO.close()

dataset_list.append("P01189_COLI_HUMAN")
dataset_list.append("P01045_KNH2_BOVIN")
dataset_list.append("P04441_HG2A_MOUSE")
dataset_list.append("P07357_CO8A_HUMAN")
dataset_list.append("P07359_GPBA_HUMAN")
dataset_list.append("P01876_ALC1_HUMAN")
dataset_list.append("P01233_CGHB_HUMAN")
dataset_list.append("P04921_GLPC_HUMAN")
dataset_list.append("Q50228")
dataset_list.append("Q4JAS3")
dataset_list.append("A4J5V5")
dataset_list.append("A6UDH9")
dataset_list.append("Q9QSP4")
dataset_list.append("P40308")


for ids in dataset_list: 
	print(ids)

	link = "http://www.uniprot.org/uniprot/%s.fasta" % ids
	f = urlopen(link)
	myfile = f.read()

	protein_id = ids
	myfile = str(myfile).replace('\\n','') #removes all newlines
	protein_dna = re.search('(?<=SV=\d)[^\]]+', str(myfile)).group(0) #searches text after SV=(1digit)
	f.close()

	len_motif = 4
	pos = ""

	for i in range(len(protein_dna)-(len_motif-1)): #makes len_motif long seq's that iterate over if follow glyco rules
		dna_test = protein_dna[i:i+len_motif]
		if dna_test[len_motif-len_motif] == "N":
			if dna_test[len_motif-(len_motif+1)] != "P":
				if (dna_test[len_motif-(len_motif+2)] == "S") or (dna_test[len_motif-(len_motif+2)] == "T"):
					if dna_test[len_motif-(len_motif+3)] != "P":
						pos = pos + str(i+1) + " " #adds +1 since location starts at 0 in python, not irl seq

						

	if pos != "":
		tempW = open('output_MRPT.txt','a')
		tempW.write(protein_id)
		tempW.write("\n" + pos[:len(pos)-1] + "\n")
		tempW.close()				