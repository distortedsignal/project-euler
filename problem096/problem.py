from copy import deepcopy
from time import time

def strToList(foo):
	'''Split strings into a list, with a list of range(1, 10) being substituted for each "0"'''
	returnList = []
	for i in foo:
		if i != '0':
			returnList.append(int(i))
		else:
			returnList.append(list(range(1,10)))

	return returnList

def removeFromLists(sudokuSet):
	'''This is where some of the magic happens
	The first part of this function is how to eliminate numbers from being possibilities in cells
	If the number is already in the set, add it to the taken list'''
	
	# Start with an empty taken list
	takenList = filter(lambda x: isinstance(x, int), sudokuSet)

	for index in range(len(sudokuSet)):
		# If this is a list, we should see if anything can be eliminated
		if isinstance(sudokuSet[index], list):
			for element in takenList:
				# If we can rule out a number, we do
				if sudokuSet[index].count(element) == 1:
					sudokuSet[index].remove(element)

			# If there is only one possible thing this could be, assume that it is that thing.
			if len(sudokuSet[index]) == 1:
				sudokuSet[index] = sudokuSet[index][0]

	return sudokuSet

def reduceLists(sudokuSet):
	'''More magic. This is assuming that if all other items in the set DON'T have the possibility
	to be a specific number, and a given cell DOES have that possibility, then that cell MUST
	be that number. An example:
			[3, 4, [5,6], [1, 2, 6], [1, 2, 6], 7, [6, 8, 9], [6, 8, 9], [1, 2, 6, 8, 9]]
	In the above example, because 5 is only in the third square, we know that 5 must be in the
	third square'''

	# Set up a cardinality dictionary of how many times a specific number appears in this block
	cardDict = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0}
	for element in sudokuSet:
		# If it's an int, we just add one to that thing's counter (this is necessary due to some weird
		# corner cases of dealing with the int/list dichotomy)
		if isinstance(element, int):
			cardDict[element] += 1
		# If it's a list, add one to the number of times each item in the list appears in this set
		elif isinstance(element, list):
			for item in element:
				cardDict[item] += 1
		# If it's neither of those things, then we have a problem
		else:
			raise ValueError(element + " is neither a list or an int. Please fix this.")

	# For each number in the cardinality dictionary
	for number in cardDict:
		# If the cardinality of that number is one and the set doesn't already contain that number
		if cardDict[number] == 1 and sudokuSet.count(number) != 1:
			# Check each item that is a list. If that item contains the number we're looking for,
			# change it to that number
			for index in range(len(sudokuSet)):
				if isinstance(sudokuSet[index], list):
					if sudokuSet[index].count(number) == 1:
						sudokuSet[index] = number
						break

	return sudokuSet

def repeatUntilStable(func, numberSet):
	oldSet = []
	while True:
		oldSet = deepcopy(numberSet)
		numberSet = func(numberSet)

		if oldSet == numberSet:
			break

	return numberSet

def workSet(sudokuSet):
	sudokuSet = repeatUntilStable(removeFromLists, sudokuSet)
	sudokuSet = repeatUntilStable(reduceLists, sudokuSet)
	return sudokuSet

def workRows(puzzle):
	for rowNum in range(len(puzzle)):
		newRow = workSet(puzzle[rowNum])
		puzzle[rowNum] = newRow

	return puzzle

def workCols(puzzle):
	# Here we have to assume the puzzle is a square
	tempSet = []
	for colNum in range(len(puzzle)):
		tempSet = []
		# Process the temp set to be columns
		for rowNum in range(len(puzzle)):
			tempSet.append(puzzle[rowNum][colNum])

		# Work the set like we did with rows
		rtrnTempSet = workSet(tempSet)
		# Re-insert into columns
		for rowNum in range(len(puzzle)):
			puzzle[rowNum][colNum] = rtrnTempSet[rowNum]

	return puzzle

def workSqrs(puzzle):
	tempSet = []
	# Make a set of [[0,0],[0,1],[0,2],[1,0],[1,1],[1,2],[2,0],[2,1],[2,2]]
	startingIndices = [[x,y] for x in range(3) for y in range(3)]
	# For each item in that set, assume that a square starts at that location multiplied by 3
	for start in startingIndices:
		# Like in the columns example, set up a temp set
		tempSet = []
		# Get each item in that square, which is actually starting index * 3 + the set of starting indices
		for add in startingIndices:
			tempSet.append(puzzle[start[1] * 3 + add[1]][start[0] * 3 + add[0]])

		# Work the set, like we did in rows and columns
		rtrnTempSet = workSet(tempSet)
		index = 0
		# Copy items from the worked set back into the square
		for add in startingIndices:
			# I should REALLY check that the assumptions I'm making here are valid.
			# This assumption has been validated. I used a debugger to step through this code and I verified
			# that these will come out of the list in the same order every time
			puzzle[start[1] * 3 + add[1]][start[0] * 3 + add[0]] = rtrnTempSet[index]
			index += 1

	return puzzle

def deduct(puzzle):
	puzzle = workRows(puzzle)
	puzzle = workCols(puzzle)
	puzzle = workSqrs(puzzle)
	
	return puzzle

def minLengthListLocation(puzzle):
	# Find the item with the FEWEST possibilities (ie, the one we're most likely to guess right)
	minLen = float("inf")
	location = [-1,-1]
	for row in range(len(puzzle)):
		for element in range(len(puzzle[row])):
			if isinstance(puzzle[row][element], list):
				if minLen > len(puzzle[row][element]):
					minLen = len(puzzle[row][element])
					location = [row, element]
					# If the length is 2, we can't get a list shorter, so return early

	return location

def brokenRows(puzzle):
	tempSet = []
	for row in puzzle:
		for element in row:
			if type(element) is int:
				if tempSet.count(element) > 0:
					return True
				else:
					tempSet.append(element)

def isBroken(puzzle):
	'''Is the puzzle broken at this point?'''
	# Check for elements that cannot have any elements
	for row in puzzle:
		for element in row:
			if element == []:
				return True

	# Check that no sets have two of the same definate element
	if brokenRows(puzzle):
		return True

	return False

def isDone(puzzle):
	'''Is the puzzle done at this point?'''
	# Check for elements that are lists
	for row in puzzle:
		for element in row:
			if type(element) is not int:
				return False

	return True

def induct(puzzle):
	location = minLengthListLocation(puzzle) 

	if location == [-1,-1]:
		# No lists as elements
		return puzzle

	# Now we know there is still something left to do.
	# Now we can select an element from the shortest list and attempt to deduce the puzzle with that
	for guess in puzzle[location[0]][location[1]]:
		newPuzzle = deepcopy(puzzle)
		newPuzzle[location[0]][location[1]] = guess
		newPuzzle = repeatUntilStable(deduct, newPuzzle)

		if isBroken(newPuzzle):
			continue

		puzzle = induct(newPuzzle)

		if isDone(puzzle):
			break

	return puzzle

def solveSudoku(puzzle):
	# Solve the puzzle using deductive reasoning - if this is true, then this must be true
	puzzle = repeatUntilStable(deduct, puzzle)
	# Solve the puzzle using inductive reasoning - if I do this, what does that imply?
	# puzzle = induct(puzzle)
	# Return a solved puzzle
	return puzzle

def readInData(f):
	# Figure it out, folks
	tempDict = {}
	currentGrid = ""
	while True:
		line = f.readline()
		if line == '':
			break
		elif line[0:4] == "Grid":
			tempDict[line.strip()] = []
			currentGrid = line.strip()
			continue
		else:
			tempDict[currentGrid].append(line.strip())

	return tempDict

f = open('sudoku.txt', 'r')

# Read in data for sudokus
sudokuDict = readInData(f)
ssum, summed = 0, 0
time0 = time()
for a in sudokuDict:
	# Change sudokus from strings into ints or lists of ints
	rows = range(len(sudokuDict[a]))
	for i in rows:
		sudokuDict[a][i] = strToList(sudokuDict[a][i])

	sudokuDict[a] = solveSudoku(sudokuDict[a])
	#ssum += ((sudokuDict[a][0][0]*100) + (sudokuDict[a][0][1]*10) + (sudokuDict[a][0][2]))
	#summed += 1
	# print "After", a + ", ssum is", ssum, "and summed is", summed

print sudokuDict

#print "Found answer", ssum, "in", time() - time0, "seconds."
