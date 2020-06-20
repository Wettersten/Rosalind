def palCheck(pal):
	rPal = ""
	for i in range(len(pal)):
		if pal[len(pal)-(i+1)] == "A":
			rPal += "T"
		elif pal[len(pal)-(i+1)] == "T": 
			rPal += "A"
		elif pal[len(pal)-(i+1)] == "G": 
			rPal += "C"
		elif pal[len(pal)-(i+1)] == "C": 
			rPal += "G"
		else:
			print "error: Character not nucleotide"
			return 0
	if pal == rPal:
		return True
	else:
		return False

def FASTAParser(txt):
	parsed = ""
	temp = open(txt, 'r')
	f = temp.readlines()#.rstrip()
	for line in f:
		#print line#debug
		if line[0] != ">":
			parsed += line.strip()
	temp.close()
	return parsed

def rPalMain(txt):
	dna = FASTAParser(txt)
	print dna#debug
	pPos = []
	pLen = []
	for i in range(len(dna)):
		j = 4
		while j <= 12:
			if i+j <= len(dna):
				if palCheck(dna[i:i+j]):
					pPos.append(i+1)
					pLen.append(j)
			j += 1
	return pPos, pLen

positions = []
lengths = []

positions, lengths = rPalMain('input.txt')
tempO = open('output.txt', 'r+')
for i in range(len(positions)):
	tempO.write(str(positions[i]) + " " + str(lengths[i]) + "\n")
	
tempO.close()