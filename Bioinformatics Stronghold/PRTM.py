def calcMass(txt):
	temp = open(txt, 'r')
	protein = temp.readline().strip()	
	weight = 0.00000
	
	A = 71.03711
	C = 103.00919
	D = 115.02694	   
	E = 129.04259
	F = 147.06841
	G = 57.02146
	H = 137.05891
	I = 113.08406
	K = 128.09496
	L = 113.08406
	M = 131.04049
	N = 114.04293
	P = 97.05276
	Q = 128.05858
	R = 156.10111
	S = 87.03203
	T = 101.04768
	V = 99.06841
	W = 186.07931
	Y = 163.06333 	
	
	for i in range(len(protein)):
		if protein[i] == "A":
			weight += A
		elif protein[i] == "C":
			weight += C
		elif protein[i] == "D":
			weight += D
		elif protein[i] == "E":
			weight += E		
		elif protein[i] == "F":
			weight += F	
		elif protein[i] == "G":
			weight += G
		elif protein[i] == "H":
			weight += H
		elif protein[i] == "I":
			weight += I
		elif protein[i] == "K":
			weight += K
		elif protein[i] == "L":
			weight += L
		elif protein[i] == "M":
			weight += M
		elif protein[i] == "N":
			weight += N
		elif protein[i] == "P":
			weight += P
		elif protein[i] == "Q":
			weight += Q
		elif protein[i] == "R":
			weight += R
		elif protein[i] == "S":
			weight += S
		elif protein[i] == "T":
			weight += T
		elif protein[i] == "V":
			weight += V
		elif protein[i] == "W":
			weight += W
		elif protein[i] == "Y":
			weight += Y
	
	temp.close()
	return weight

tempW = open('output.txt','w')
tempW.write(str(calcMass('input.txt')))
tempW.close()	