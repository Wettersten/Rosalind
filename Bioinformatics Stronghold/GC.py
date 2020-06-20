temp = open('input.txt','r')

genomeList = []
labelList = []

currLine = temp.readline().strip()
currGenome = ""
newLine = False
while currLine[0] != "x":
	if currLine[0] == ">" and newLine == False:
		labelList.append(currLine[1::])
		newLine = True
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
for item in genomeList:
	print item

for label in labelList:
	print label