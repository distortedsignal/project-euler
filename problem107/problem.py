class Node:
	def __init__(self, name):
		self.name = name
		self.connectedTo = list([])

def traverses(start, end, visited):
	if start == end:
		return True

	for node in start.connectedTo:
		if visited.count(node) == 0:
			visited.append(node)
			if traverses(node, end, visited):
				return True
	return False

def simpleSolution(filePath):
	# Read in file
	f = open(filePath, "r")
	ignoreIndex = 0
	nodeList = list([])
	first = True
	for line in f:
		weightList = line.split(",")
		if first:
			first = False
			for i in range(len(weightList)):
				nodeList.append(Node(str(i)))
		print weightList

if __name__ == "__main__":
	print simpleSolution("network.txt")
