f = open("matrix.txt", "r")

matrix = []
for line in f:
	# For each line, take off the newline at the end, split on the comma, map all items to 
	# integers, and then append the created list to matrix.
	matrix.append(map(int,line.strip().split(",")))

for i in range(1, len(matrix)): # The x component
	for j in range(len(matrix)): # The y component
		matrix[j][i] += matrix[j][i-1]


	# optimal = False
	# while not(optimal):

for i in range(len(matrix)):
	print matrix[i]