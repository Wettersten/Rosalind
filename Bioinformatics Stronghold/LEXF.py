temp = open('input.txt','r')
parsl = temp.readline().strip().replace(" ","")
gen = ""
for k in range(len(parsl)):	
	gen += parsl[k]

k = 0
parsl = temp.readline().strip()
k = int(parsl)

print gen, k
	
for aPos in range(len(gen)): #gör en gång per bokstav i gen
	kmer = gen[aPos]
	bPos = 0
	for bPos in range(len(gen)): #för varje bokstav i gen så ska det finnas x antal permutationer, där x är antal bokstäver i gen
		ind = bPos
		while len(kmer) < k: #permutationslängd, index + så man kan ta nästa bokstav i gen
			kmer += gen[ind]
			ind += 1
		print kmer
	
