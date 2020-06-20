from itertools import permutations, product

perm = 2
plist = list(range(1,perm+1,1)) #creates a list of 1,2,...x


def plusAndMinusPermutations(items):
    for p in permutations(items): #creates all permutations of plist, (1,2), (2,1)
        for signs in product([-1,1], repeat=len(items)): #creates all permutations of positive, negative 1, with length of plist, (-1,1), (-1,-1).. etc
            yield [a*sign for a,sign in zip(p,signs)] #permutions are multiplied with the +/- list, yielding only uniques
reslist = list(plusAndMinusPermutations(plist))

f = open("sign.txt","w+")
f.write(str(len(reslist))+"\n")
for i in reslist:
    f.write(str(i)+"\n")
    
f.close() #the output will be in the format:
#38
#[1, 2, 3] etc
#need to ctrl-f remove "[", "," and "]" to get 1, 2, 3 format for rosalind


##explaining the loop
#https://stackoverflow.com/questions/11178061/print-list-without-brackets-in-a-single-row
#print(list(permutations(plist))) 
#print(list(product([-1,1], repeat=len(plist)))) 