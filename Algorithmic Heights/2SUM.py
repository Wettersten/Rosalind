def readInput(filename):
    temp_list = []
    with open(filename) as fh:
        for line in fh:
            temp_list.append(line.rstrip().split(' '))
        
    return temp_list

#print(readInput('input3.txt'))
res_list = []
sum_list = readInput('rosalind_2sum.txt')[1:]
#print(sum_list)


for i in range(len(sum_list)):
    hit = False
    #print(sum_list[i])
    for j in range(len(sum_list[i])-1):
        #print("j: "+sum_list[i][j])
        for k in range(j+1,len(sum_list[i])):
            #print("k: "+sum_list[i][k])
            if hit != True:
                if int(sum_list[i][j]) == -1*int(sum_list[i][k]):
                    res_list.append([j+1,k+1])
                    #print("appending j+k")
                    hit = True
                    break
                elif j == len(sum_list[i])-2:
                    #print("appending -1")
                    res_list.append([-1])
                    hit = True
                    break

#print(res_list)
for line in res_list:
    if len(line) == 1:
        print("-1")
    else:
        print(str(line[0])+" "+str(line[1]))