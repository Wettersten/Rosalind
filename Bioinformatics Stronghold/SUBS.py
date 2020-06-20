def subCheck(s,t):
	subs = []
	for i in range(len(s)):
		if s[i:i+len(t)] == t:
			subs.append(i+1)
	return subs

def parse(txt):
	s = ""
	t = ""
	temp = open(txt, 'r')
	s = temp.readline().strip()
	t = temp.readline().strip()
	temp.close()
	return s,t

f = open('output.txt','r+')	
#print len(subCheck(parse('input.txt')[0],parse('input.txt')[1])) #test length of list
for i in range(len(subCheck(parse('input.txt')[0],parse('input.txt')[1]))):
	a = subCheck(parse('input.txt')[0],parse('input.txt')[1])[i]
	f.write(str(a) + " ")
f.close()