f = open("matrix.txt", "r")

matrix = []
for line in f:
	# For each line, take off the newline at the end, split on the comma, map all items to 
	# integers, and then append the created list to matrix.
	matrix.append(map(int,line.strip().split(",")))

# i is x coord, j is y coord.
for i in range(1, len(matrix)):
	tempList = []
	verifiedList = []
	for j in range(len(matrix)):
		# First item in the list is the value,
		# second item is if it was already visited
		tempList.append(matrix[j][i] + matrix[j][i-1])
		verifiedList.append(False)
	
	verifiedList[tempList.index(min(tempList))] = True
	sortedTempList = tempList
	sortedTempList.sort()

	for j in sortedTempList:
		currentIndex = tempList.index(j)

	

	


	# optimal = False
	# while not(optimal):

# for i in range(len(matrix)):
# 	print matrix[i]