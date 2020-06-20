#requires manualf ormating of FASTA before using the readlins(), can be fixed using while to check for new ">"
tempIn = open('input.txt','r')
tempLine = " "
genome = []
ASum = []
TSum = []
CSum = []
GSum = []
allSum = []
cons = ""


while tempLine[0] != '*': #strips a line to genome, requires 1 pure line of all the necleutides, not split lines
	tempLine = tempIn.readline().strip()
	if tempLine[0] != '>' and tempLine[0] != '*':
		genome.append(tempLine)

		
for a in range(len(genome[0])): #counts ACGT and appends to lists in order of appearence
	ACount = 0
	TCount = 0
	CCount = 0 
	GCount = 0
	for b in range(len(genome)):
		if genome[b][a] == 'A':
			ACount += 1
		elif genome[b][a] == 'T':		
			TCount += 1
		elif genome[b][a] == 'C':	
			CCount += 1
		elif genome[b][a] == 'G':	
			GCount += 1
			
	ASum.append(ACount)
	TSum.append(TCount)
	CSum.append(CCount)
	GSum.append(GCount)
	
allSum.append(ASum)
allSum.append(TSum)
allSum.append(CSum)
allSum.append(GSum)

tempIn.close()	

for c in range(len(ASum)): #goes through x times where x is len of the dna strings, checks which ACGT is highest, appends highest in a string
	highest = 0
	nucleotide = ""
	for d in range(4):
		if allSum[d][c] >= highest:
			highest = allSum[d][c]
			if d == 0:
				nucleotide = 'A'
			elif d == 1:
				nucleotide = 'T'
			elif d == 2:
				nucleotide = 'C'
			elif d == 3:
				nucleotide = 'G'
	cons += nucleotide
	
aP = ""
cP = ""
gP = ""
tP = ""

for aTal in ASum: #formats to matrix for print
	aP += " " + str(aTal)
for cTal in CSum:
	cP += " " + str(cTal)
for gTal in GSum:
	gP += " " + str(gTal)
for tTal in TSum:
	tP += " " + str(tTal)	
tempOut = open('output.txt', 'w')
	
tempOut.write(cons+"\n")
tempOut.write("A: "+aP+"\n")
tempOut.write("C: "+cP+"\n")
tempOut.write("G: "+gP+"\n")
tempOut.write("T: "+tP)
tempOut.close()