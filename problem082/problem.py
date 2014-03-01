f = open("matrix.txt", "r")
w = open("output.txt", "w+")

matrix = []
for line in f:
	# For each line, take off the newline at the end, split on the comma, map all items to 
	# integers, and then append the created list to matrix.
	matrix.append(map(int,line.strip().split(",")))

# i is x coord, j is y coord.
for i in range(1, len(matrix)):
	tmpLst = []
	for j in range(len(matrix)):
		# First item in the list is the value,
		# second item is if it was already visited
		tmpLst.append([matrix[j][i] + matrix[j][i-1], False])
	
	minIndex = tmpLst.index(min(tmpLst))

	


	# optimal = False
	# while not(optimal):

# for i in range(len(matrix)):
# 	print matrix[i]