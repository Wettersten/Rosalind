temp = open('input.txt','r')

suffList = []
preList = []
k = temp.readline()
rdL = temp.readline().strip()


while rdL[0] != "x": #parser
	i = 0
	found = False
	while found == False:
		if rdL[i] == " ":
			suffList.append(rdL[0:i])
			preList.append(rdL[i+1:len(rdL)])
			found = True
			break
		i += 1
	rdL = temp.readline().strip()
	
