total_generations = 85
lifespan_rabbits = 17
total_pairs = 0

pairs_gen = [1] # temp -> newborns


#for #generations append 0. 0 = newborn, lifespan_rabbits = death
for i in range(lifespan_rabbits):
	pairs_gen.append(0)



	
#-1 since gen 1 = 1,0,0...
for x in range(total_generations-1):

	#adds all values between [1]->[lifespan-1] as newborns
	i = 1
	pairs_temp = 0
	while(i<lifespan_rabbits): 
		pairs_temp = pairs_temp + pairs_gen[i]
		i = i + 1
	
	#each generation is moved one step up
	for y in range(lifespan_rabbits):
		pairs_gen[lifespan_rabbits-y] = pairs_gen[lifespan_rabbits-(y+1)]

	#newborn is added	
	pairs_gen[0] = pairs_temp
		

#adds each index in array to total (not last which is dead)
for a in range((len(pairs_gen))-1):
	total_pairs = total_pairs + pairs_gen[a]

print(total_pairs, "\nPrinted to output.txt")

tempW = open('output_FIBD.txt','w')
tempW.write(str(total_pairs))
tempW.close()