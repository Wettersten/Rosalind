genomeList = []
temp = open('input.txt','r')

currLine = temp.readline().strip()
currGenome = ""
newLine = False
while currLine[0] != "*":
	if currLine[0] == ">" and newLine == False:		
		newLine = True
		currLine = temp.readline().strip()
	elif currLine[0] == 'x':
		genomeList.append(currGenome)
		currLine = temp.readline().strip()
	elif currLine[0] == ">" and newLine == True:
		genomeList.append(currGenome)
		currGenome = ""		
		currLine = temp.readline().strip()
	elif currLine[0] != '>' and currLine[0] != "":
		currGenome += currLine.strip()
		currLine = temp.readline().strip()
		
temp.close()

def long_substr(data):
    substr = ''
    if len(data) > 1 and len(data[0]) > 0:
        for i in range(len(data[0])):
            for j in range(len(data[0])-i+1):
                if j > len(substr) and is_substr(data[0][i:i+j], data):
                    substr = data[0][i:i+j]
    return substr

def is_substr(find, data):
    if len(data) < 1 and len(find) < 1:
        return False
    for i in range(len(data)):
        if find not in data[i]:
            return False
    return True

tempOut = open('output.txt','w')
tempOut.write(long_substr(genomeList))
