from mathLib import isPrime

def addLayer(grid):
	assert len(grid) % 2 == 1
	assert len(grid[0]) % 2 == 1
	seed = grid[len(grid)-1][len(grid[len(grid)-1])-1]
	grid.insert(0,[])
	grid.append([])

	# Populate most of right column
	for i in range(len(grid)-1,0,-1):
		seed += 1
		grid[i-1].append(seed)

	# Populate top row
	for i in range(len(grid)-2,0,-1):
		seed += 1
		grid[0].insert(0, seed)

	# Populate left column
	for i in range(len(grid)):
		seed += 1
		grid[i].insert(0, seed)

	# Populate bottom row
	for i in range(len(grid)-1):
		seed += 1
		grid[len(grid)-1].append(seed)

	return grid

grid = [[1]]
primeCount = 0
while True:
	grid = addLayer(grid)
	primeCount = 0
	for i in len(grid):
		if isPrime(grid[i][i]):
			primeCount += 1
		if isPrime(grid[i][-i]):
			primeCount += 1
	if (float(primeCount) / float((len(grid) * 2) - 1)) < .1:
		break
print len(grid)

