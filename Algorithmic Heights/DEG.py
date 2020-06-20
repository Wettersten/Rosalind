def readInput(filename):
    vertice_list = []
    with open(filename) as fh:
        for line in fh:
            temp_list = []
            temp_line = line.rstrip()
            temp_list.append(temp_line.split(' ')[0])
            temp_list.append(temp_line.split(' ')[1])
            vertice_list.append(temp_list)  
            
    vertice_list_pruned = vertice_list[1:] #keeps rest of rows
    vertices = vertice_list[0][0] #first row is #vertices, #edges
    return vertice_list_pruned, int(vertices) 

full_list, vertices = readInput('rosalind_deg.txt')
#print(full_list, vertices)

degree_list = []
degree_list = [0]*vertices #creates a list of 0's, 
#print(degree_list)

for edge in full_list:
    degree_list[int(edge[0])-1] += 1
    degree_list[int(edge[1])-1] += 1
    
#print(degree_list)

result_str = ""
for i in range(len(degree_list)):
    result_str += str(degree_list[i]) + " "
    
print(result_str) #prints result as a string with values seperated by space