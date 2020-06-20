temp = open('input.txt','r')
k = 3
genomeList = []
labelList = []
adjList = []
currLine = temp.readline().strip()
currGenome = ""
newLine = False


while currLine[0] != "*":
	if currLine[0] == ">" and newLine == False:
		labelList.append(currLine[1::])
		newLine = True
		currLine = temp.readline().strip()
	elif currLine[0] == 'x':
		genomeList.append(currGenome)
		currLine = temp.readline().strip()
	elif currLine[0] == ">" and newLine == True:
		genomeList.append(currGenome)
		currGenome = ""
		labelList.append(currLine[1::])
		currLine = temp.readline().strip()
	elif currLine[0] != '>' and currLine[0] != "":
		currGenome += currLine.strip()
		currLine = temp.readline().strip()

		
temp.close()

for a in range(len(genomeList)):
	wholeSuffGen = genomeList[a]
	suffGen = wholeSuffGen[len(wholeSuffGen)-k:len(wholeSuffGen)]
	for b in range(len(genomeList)):
		wholePreGen = genomeList[b]
		preGen = wholePreGen[0:k]
		if wholeSuffGen != wholePreGen and suffGen == preGen:
			adjList.append(labelList[a] + " " + labelList[b])

tempOut = open('output.txt','w')
for adj in adjList:
	tempOut.write(adj)
	tempOut.write("\n")