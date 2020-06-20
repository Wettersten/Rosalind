#parser exons, slicedDNA = DNA to translate, orig = in, sub(s) are substrings (inons)
temp = open('input.txt','r')
origDNA = ""
rdl = temp.readline().strip() #skip first FASTA label
rdl = temp.readline().strip()
while rdl[0] != ">": #parse origDNA
	origDNA += rdl
	rdl = temp.readline().strip()
slicedDNA = origDNA
subS = []

rdl = temp.readline().strip() #skip 2nd FASTA label
while rdl[0] != 'x': #parses substrings to subS, requires 3 lines of 'x' at the end of input.txt (jump 2 lines)
	subS.append(rdl)
	rdl = temp.readline().strip() #next label
	rdl = temp.readline().strip() #next substring

for a in range(len(subS)): #slices out all subStrings by comparing sections of the text corresponding to len(substring) and only keeping string before and after found section
	for i in range(len(slicedDNA)-len(subS[a])):
		if slicedDNA[i:i+len(subS[a])] == subS[a]:
			slicedDNA = slicedDNA[0:i] + slicedDNA[i+len(subS[a]):len(slicedDNA)]


 
#header including all dna codonlists
codonHeaderDNA = [] 

#creates all dna lists
dF, dL, dI, dM, dV, dS, dP, dT, dA, dY, dStop, dH, dQ, dN, dK, dD, dE, dC, dW, dR, dG = ([] for i in range(21))

#header including all rna codonlists
codonHeaderRNA = [] 

#creates all rna lists
rF, rL, rI, rM, rV, rS, rP, rT, rA, rY, rStop, rH, rQ, rN, rK, rD, rE, rC, rW, rR, rG = ([] for i in range(21)) 

#translate function
def translation(bp):

	base = ""
	protein = ""

	i = 0
	while i < len(bp):
		base = bp[i] + bp[i+1] + bp[i+2]

		for codonGroup in codonHeaderDNA:
			for codon in codonGroup:
				if codon == base:
					protein += codonGroup[0]            
		i += 3
		  

	return protein

#appends all codons to DNA/RNA groups
def codonInit(): 
    #DNA
  codonHeaderDNA.append(dF), codonHeaderDNA.append(dL), codonHeaderDNA.append(dI), codonHeaderDNA.append(dM), codonHeaderDNA.append(dV), codonHeaderDNA.append(dS), codonHeaderDNA.append(dP), codonHeaderDNA.append(dT), codonHeaderDNA.append(dA), codonHeaderDNA.append(dY), codonHeaderDNA.append(dStop), codonHeaderDNA.append(dH), codonHeaderDNA.append(dQ), codonHeaderDNA.append(dN), codonHeaderDNA.append(dK), codonHeaderDNA.append(dD), codonHeaderDNA.append(dE), codonHeaderDNA.append(dC), codonHeaderDNA.append(dW), codonHeaderDNA.append(dR), codonHeaderDNA.append(dG)
  dF.append("F"),dF.append("TTT"),dF.append("TTC")
  dL.append("L"), dL.append("TTA"), dL.append("TTG"), dL.append("CTT"), dL.append("CTC"), dL.append("CTA"), dL.append("CTG")
  dI.append("I"), dI.append("ATT"), dI.append("ATC"), dI.append("ATA")
  dM.append("M"), dM.append("ATG")
  dV.append("V"), dV.append("GTT"), dV.append("GTC"), dV.append("GTA"), dV.append("GTG")
  dS.append("S"), dS.append("TCT"), dS.append("TCC"), dS.append("TCA"), dS.append("TCG"), dS.append("AGT"), dS.append("AGC")
  dP.append("P"), dP.append("CCT"), dP.append("CCC"), dP.append("CCA"), dP.append("CCG")
  dT.append("T"), dT.append("ACT"), dT.append("ACC"), dT.append("ACA"), dT.append("ACG")
  dA.append("A"), dA.append("GCT"), dA.append("GCC"), dA.append("GCA"), dA.append("GCG")
  dY.append("Y"), dY.append("TAT"), dY.append("TAC")
  dStop.append("*"), dStop.append("TAA"), dStop.append("TGA"), dStop.append("TAG")
  dH.append("H"), dH.append("CAT"), dH.append("CAC")
  dQ.append("Q"), dQ.append("CAA"), dQ.append("CAG")
  dN.append("N"), dN.append("AAT"), dN.append("AAC")
  dK.append("K"), dK.append("AAA"), dK.append("AAG")
  dD.append("D"), dD.append("GAT"), dD.append("GAC")
  dE.append("E"), dE.append("GAA"), dE.append("GAG")
  dC.append("C"), dC.append("TGT"), dC.append("TGC")
  dW.append("W"), dW.append("TGG")
  dR.append("R"), dR.append("CGT"), dR.append("CGC"), dR.append("CGA"), dR.append("CGG"), dR.append("AGA"), dR.append("AGG")
  dG.append("G"), dG.append("GGT"), dG.append("GGC"), dG.append("GGA"), dG.append("GGG")
  #RNA
  codonHeaderRNA.append(rF), codonHeaderRNA.append(rL), codonHeaderRNA.append(rI), codonHeaderRNA.append(rM), codonHeaderRNA.append(rV), codonHeaderRNA.append(rS), codonHeaderRNA.append(rP), codonHeaderRNA.append(rT), codonHeaderRNA.append(rA), codonHeaderRNA.append(rY), codonHeaderRNA.append(rStop), codonHeaderRNA.append(rH), codonHeaderRNA.append(rQ), codonHeaderRNA.append(rN), codonHeaderRNA.append(rK), codonHeaderRNA.append(rD), codonHeaderRNA.append(rE), codonHeaderRNA.append(rC), codonHeaderRNA.append(rW), codonHeaderRNA.append(rR), codonHeaderRNA.append(rG)
  rF.append("F")
  rF.append("UUU")
  rF.append("UUC")
  rL.append("L")
  rL.append("UUA")
  rL.append("UUG")
  rL.append("CUU")
  rL.append("CUC")
  rL.append("CUA")
  rL.append("CUG")
  rI.append("I")
  rI.append("AUU")
  rI.append("AUC")
  rI.append("AUA")
  rM.append("M")
  rM.append("AUG")
  rV.append("V")
  rV.append("GUU")
  rV.append("GUC")
  rV.append("GUA")
  rV.append("GUG")
  rS.append("S")
  rS.append("UCU")
  rS.append("UCC")
  rS.append("UCA")
  rS.append("UCG")
  rS.append("AGU")
  rS.append("AGC")
  rP.append("P")
  rP.append("CCU")
  rP.append("CCC")
  rP.append("CCA")
  rP.append("CCG")
  rT.append("T")
  rT.append("ACU")
  rT.append("ACC")
  rT.append("ACA")
  rT.append("ACG")
  rA.append("A")
  rA.append("GCU")
  rA.append("GCC")
  rA.append("GCA")
  rA.append("GCG")
  rY.append("Y")
  rY.append("UAU")
  rY.append("UAC")
  rStop.append("*")
  rStop.append("UAA")
  rStop.append("UGA")
  rStop.append("UAG")
  rH.append("H")
  rH.append("CAU")
  rH.append("CAC")
  rQ.append("Q")
  rQ.append("CAA")
  rQ.append("CAG")
  rN.append("N")
  rN.append("AAU")
  rN.append("AAC")
  rK.append("K")
  rK.append("AAA")
  rK.append("AAG")
  rD.append("D")
  rD.append("GAU")
  rD.append("GAC")
  rE.append("E")
  rE.append("GAA")
  rE.append("GAG")
  rC.append("C")
  rC.append("UGU")
  rC.append("UGC")
  rW.append("W")
  rW.append("UGG")
  rR.append("R")
  rR.append("CGU")
  rR.append("CGC")
  rR.append("CGA")
  rR.append("CGG")
  rR.append("AGA")
  rR.append("AGG")
  rG.append("G")
  rG.append("GGU")
  rG.append("GGC")
  rG.append("GGA")
  rG.append("GGG")


#cleans all codongroups
def codonClean():
  dF, dL, dI, dM, dV, dS, dP, dT, dA, dY, dStop, dH, dQ, dN, dK, dD, dE, dC, dW, dR, dG = ([] for i in range(21)) 
  rF, rL, rI, rM, rV, rS, rP, rT, rA, rY, rStop, rH, rQ, rN, rK, rD, rE, rC, rW, rR, rG = ([] for i in range(21)) 

def dnaOrRna(bp):
  loop = 0
  dna = 1
  cloop = 0
  while cloop == 0:
    if bp[loop] == "T":
      dna = 1
      cloop = 1
    elif bp[loop] == "U":
      dna = 0
      cloop = 1
    elif loop+1 == len(bp):
      dna = 1
      cloop = 1
    loop += 1
  return dna

  
codonClean()
codonInit()
tempOut = open('output.txt','w')
tempOut.write(translation(slicedDNA))




