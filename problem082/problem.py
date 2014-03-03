# For Algorithmic complexity, assume a square matrix of N x N. If this is not a valid assumption,
# I would invite you to suck it.

from time import clock as cl

def getMinIndex(unsortedList, touchedList):
	# Complexity: N
	minVal = float("inf")
	index = -1
	for i in range(len(unsortedList)):
		if unsortedList[i] < minVal and touchedList[i] == False:
			minVal = unsortedList[i]
			index = i

	return index

# Complexity: N
f = open("matrix.txt", "r")

matrix = []
# Complexity: N^2 (but it's a small N^2, because the int function should be VERY optimized.)
for line in f:
	# For each line, take off the newline at the end, split on the comma, map all items to 
	# integers, and then append the created list to matrix.
	# Complexity: I'm going to assume N
	matrix.append(map(int,line.strip().split(",")))

# Starting clock
startTime = cl()

tempList = []
verifiedList = []

# Complexity: N^3 (Gah!)
# i is x coord, j is y coord.
for i in range(1, len(matrix)):
	# Complexity: N
	for j in range(len(matrix)):
		# First item in the list is the value,
		# second item is if it was already visited
		tempList.append(matrix[j][i] + matrix[j][i-1])
		verifiedList.append(False)

	# Complexity: N
	minIndex = getMinIndex(tempList, verifiedList)

	# Complexity: N^2
	while minIndex != -1:
		if minIndex == 0:
			if tempList[minIndex + 1] > tempList[minIndex] + matrix[minIndex + 1][i]:
				tempList[minIndex + 1] = tempList[minIndex] + matrix[minIndex + 1][i]
		elif minIndex == (len(tempList) - 1):
			if tempList[minIndex - 1] > tempList[minIndex] + matrix[minIndex - 1][i]:
				tempList[minIndex - 1] = tempList[minIndex] + matrix[minIndex - 1][i]
		else:
			if tempList[minIndex + 1] > tempList[minIndex] + matrix[minIndex + 1][i]:
				tempList[minIndex + 1] = tempList[minIndex] + matrix[minIndex + 1][i]
			if tempList[minIndex - 1] > tempList[minIndex] + matrix[minIndex - 1][i]:
				tempList[minIndex - 1] = tempList[minIndex] + matrix[minIndex - 1][i]

		# Complexity: 1
		verifiedList[minIndex] = True

		# Complexity: N
		minIndex = getMinIndex(tempList, verifiedList)

	# Complexity: N
	for j in range(len(matrix)):
		matrix[j][i] = tempList[j]

	# It's either reset this here or re-initialize every loop.
	tempList = []
	verifiedList = []

# Complexity: N
endScores = []
for i in range(len(matrix)):
	endScores.append(matrix[i][len(matrix[i]) - 1])

# Complexity: N
print min(endScores)

# This reports the time to finish as 0.059 seconds.
print cl() - startTime
