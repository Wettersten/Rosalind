"""Breadth-First Search
http://rosalind.info/problems/bfs/
The task is to use breadth-first search to compute single-source shortest 
distances in an unweighted directed graph.

Given: A simple directed graph with n=103 vertices in the edge list format.
Return: An array D[1..n] where D[i] is the length of a shortest path from the 
vertex 1 to the vertex i (D[1]=0). If i is not reachable from 1 set D[i] to -1.
"""
import time #used to calc time spent in calculation, used to debug slow original code
vertice_index = []

with open('rosalind_bfs.txt', 'r') as f:
    for read_vertice in f:
        vertice_index.append(read_vertice.rstrip().split(" "))
        
header = vertice_index[0]
vertices = int(header[0]) #number of vertices in the edge format list
edges = int(header[1])
vertice_index.remove(header) #removes header from index


def shortest(vertices, dfs_list):
    """Initialize outputlist, first value is always 0
    Start all others as -1 to ignore checking if missing.
    """
    
    shortest_path = [0]
    for z in range(0,vertices-1):
        shortest_path.append(-1)
    for b in range(1,len(dfs_list)):
        for dist in dfs_list[b]:
            shortest_path[int(dist)-1] = b
            
    return shortest_path

def dfs(vertices, vertice_index):
    """Depth first search of vertice_index, creates list of distance layers (dfs_list)
    This is used to create a shortest path list for rosalind output.
    """
    
    dfs_list = [['1']]
    i = 0
    tmp_vertices = vertice_index
    all_vertices = ['1'] #all found vertices so far, so we don't use 1 again later

    while i >= 0: #does this until breaks later
        found_vertices = []
        to_remove = []
        for vertice in tmp_vertices:
            if vertice[0] in dfs_list[i] and vertice[1] not in all_vertices:
                found_vertices.append(vertice[1])
                all_vertices.append(vertice[1])
                to_remove.append(vertice)
        if not found_vertices: #if there are no more edges to current vertice
            break
        else:
            dfs_list.append(found_vertices)
            i = i + 1
            for rmv in to_remove:
                tmp_vertices.remove(rmv) #removes already used vertices, speeds up algo
    
    """Old shortest path, replaced by new faster & simpler function
    
    for j in range(1,vertices+1):
        if [str(j)] in dfs_list: #if value in list, appends to current distance layer
            shortest_path.append(dfs_list.index([str(j)]))
        else:
            found = 0
            k = 0
            for lst in dfs_list: #used since some layers contains a list rather than one value
                if len(lst) > 1 and str(j) in lst:
                    found = 1
                    break
                k = k + 1

            if found == 0:
                shortest_path.append(-1)
            else:
                shortest_path.append(k)
    """
    
    return dfs_list, shortest(vertices, dfs_list)

start_time = time.time()
rosalind_answer = ""
ans = dfs(vertices,vertice_index)
for val in ans[1]:
    rosalind_answer += str(val) + " "
print(rosalind_answer)
print("--- %s seconds ---" % (time.time() - start_time))