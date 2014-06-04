from copy import deepcopy
from time import time

def strToList(foo):
	rtrnLst = []
	for i in foo:
		if i != '0':
			rtrnLst.append(int(i))
		else:
			rtrnLst.append(list(range(1,10)))

	return rtrnLst

def workSet(sudokuSet):
	takenList = []
	for a in sudokuSet:
		# If this is a number, we can't modify it, and we can only say that nothing else can be this number
		if isinstance(a, int):
			takenList.append(a)

	# After collecting everything that can't be changed, we can start changing things
	for a in range(len(sudokuSet)):
		# If this is a list, we should see if anything can be eliminated
		if isinstance(sudokuSet[a], list):
			for i in takenList:
				# If we can rule out a number, we do
				if sudokuSet[a].count(i) == 1:
					sudokuSet[a].remove(i)

			# If there is only one possible thing this could be, assume that it is that thing.
			if len(sudokuSet[a]) == 1:
				sudokuSet[a] = sudokuSet[a][0]

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

		# Re-insert into columns
		rtrnTempSet = workSet(tempSet)
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

		rtrnTempSet = workSet(tempSet)
		index = 0
		for add in startingIndices:
			# I should REALLY check that the assumptions I'm making here are valid.
			puzzle[start[1] * 3 + add[1]][start[0] * 3 + add[0]] = rtrnTempSet[index]
			index += 1

	return puzzle

def deduct(puzzle):
	oldPuzzle = []
	while True:
		oldPuzzle = deepcopy(puzzle)
		puzzle = workRows(puzzle)
		puzzle = workCols(puzzle)
		puzzle = workSqrs(puzzle)
		
		if puzzle == oldPuzzle:
			break

	return puzzle

def induct(puzzle):
	# print puzzle
	return puzzle

def solveSudoku(puzzle):
	# Solve the puzzle using deductive reasoning - if this is true, then this must be true
	puzzle = deduct(puzzle)
	# Solve the puzzle using inductive reasoning - if I do this, what does that imply?
	puzzle = induct(puzzle)
	return puzzle

def readInData(f):
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

#Read in data for sudokus
sudokuDict = readInData(f)
time0 = 0
timeDict = {}
for a in sudokuDict:
	# Change sudokus from strings into ints or lists of ints
	rows = range(len(sudokuDict[a]))
	for i in rows:
		sudokuDict[a][i] = strToList(sudokuDict[a][i])

	time0 = time()
	sudokuDict[a] = solveSudoku(sudokuDict[a])
	timeDict[a] = time() - time0

print timeDict
print sudokuDict
	




# Other things


