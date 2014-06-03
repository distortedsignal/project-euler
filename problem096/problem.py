def strToList(foo):
	rtrnLst = []
	for i in foo:
		if i != '0':
			rtrnLst.append(int(i))
		else:
			rtrnLst.append(list(range(1,10)))
	return rtrnLst

def solveSudoku(puzzle):
	takenList = []
	rows = range(len(puzzle))
	for row in rows:
		takenList = []
		for a in puzzle[row]:
			if isinstance(a, int):
				takenList.append(a)

		for a in puzzle[row]:
			if isinstance(a, list):
				for i in takenList:
					a.remove(i)

f = open('sudoku.txt', 'r')

sudokuDict = {}

currentGrid = ""

takenList = []

# Read in a lot of sudokus
while True:
	line = f.readline()
	if line == '':
		break
	elif line[0:4] == "Grid":
		sudokuDict[line.strip()] = []
		currentGrid = line.strip()
		continue
	else:
		sudokuDict[currentGrid].append(line.strip())

for a in sudokuDict:
	# Change sudokus from strings into ints or lists of ints
	rows = range(len(sudokuDict[a]))
	for i in rows:
		sudokuDict[a][i] = strToList(sudokuDict[a][i])

	solveSudoku(sudokuDict[a])
	




# Other things


