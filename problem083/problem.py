def simpleSolution(filePath):
	from copy import deepcopy
	# Huh, this looks familiar.
	# Complexity: N
	f = open(filePath, "r")

	matrix = []
	# Complexity: N^2 (but it's a small N^2, because the int function should be VERY optimized.)
	for line in f:
		# For each line, take off the newline at the end, split on the comma, map all items to 
		# integers, and then append the created list to matrix.
		# Complexity: I'm going to assume N
		matrix.append(map(int,line.strip().split(",")))

	result = deepcopy(matrix)
	for i in range(len(matrix) - 1, -1, -1):
		for j in range(len(matrix[i]) - 1, -1, -1):
			if i == len(matrix) - 1 and j == len(matrix) - 1:
				continue
			elif i == len(matrix) - 1:
				result[i][j] = matrix[i][j] + result[i][j+1]
			elif j == len(matrix) - 1:
				result[i][j] = matrix[i][j] + result[i+1][j]
			else:
				result[i][j] = matrix[i][j] + min([result[i+1][j], result[i][j+1]])

	rebalanced = True

	while rebalanced:
		rebalanced = False

		for i in range(len(matrix) - 1, -1, -1):
			for j in range(len(matrix) - 1, -1, -1):
				if i == len(matrix) - 1 and j == len(matrix) - 1:
					# End of maze
					continue
				elif i == 0 and j == 0:
					# Origin of maze
					if result[i][j] > matrix[i][j] + min(result[i+1][j], result[i][j+1]):
						result[i][j] = matrix[i][j] + min(result[i+1][j], result[i][j+1])
						rebalanced = True
				elif i == len(matrix) - 1 and j == 0:
					# Lower left corner
					if result[i][j] > matrix[i][j] + min(result[i-1][j], result[i][j+1]):
						result[i][j] = matrix[i][j] + min(result[i-1][j], result[i][j+1])
						rebalanced = True
				elif i == 0 and j == len(matrix) - 1:
					# Upper right corner
					if result[i][j] > matrix[i][j] + min(result[i][j-1], result[i+1][j]):
						result[i][j] = matrix[i][j] + min(result[i][j-1], result[i+1][j])
						rebalanced = True
				elif i == len(matrix) - 1:
					# Bottom edge
					if result[i][j] > matrix[i][j] + min(result[i][j+1], result[i][j-1], result[i-1][j]):
						result[i][j] = matrix[i][j] + min(result[i][j+1], result[i][j-1], result[i-1][j])
						rebalanced = True
				elif i == 0:
					# Top edge
					if result[i][j] > matrix[i][j] + min(result[i][j+1], result[i][j-1], result[i+1][j]):
						result[i][j] = matrix[i][j] + min(result[i][j+1], result[i][j-1], result[i+1][j])
						rebalanced = True
				elif j == len(matrix) - 1:
					# Right edge
					if result[i][j] > matrix[i][j] + min(result[i+1][j], result[i-1][j], result[i][j-1]):
						result[i][j] = matrix[i][j] + min(result[i+1][j], result[i-1][j], result[i][j-1])
						rebalanced = True
				elif j == 0:
					# Left edge
					if result[i][j] > matrix[i][j] + min(result[i+1][j], result[i-1][j], result[i][j+1]):
						result[i][j] = matrix[i][j] + min(result[i+1][j], result[i-1][j], result[i][j+1])
						rebalanced = True
				else:
					# The creamy middles
					if result[i][j] > matrix[i][j] + min(result[i+1][j], result[i-1][j], result[i][j+1], result[i][j-1]):
						result[i][j] = matrix[i][j] + min(result[i+1][j], result[i-1][j], result[i][j+1], result[i][j-1])
						rebalanced = True

	return result[0][0]

if __name__ == "__main__":
	print simpleSolution("matrix.txt")