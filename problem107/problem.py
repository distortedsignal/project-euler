class Node:
	def __init__(self, name):
		self.name = name
		self.connectedTo = list([])

	def addLink(self, linkTuple):
		self.connectedTo.append(linkTuple)

	def removeLink(self, linkTuple):
		self.connectedTo.remove(linkTuple)

def traverses(start, end, visited):
	if start == end:
		return True
	if len(start.connectedTo) == 0:
		return False

	for link in start.connectedTo:
		node = link[0]
		if visited.count(node) == 0:
			visited.append(node)
			if traverses(node, end, visited):
				return True
	return False

def simpleSolution(filePath):
	# Read in file
	f = open(filePath, "r")
	index = 0
	nodeList = list([])
	edgeList = list([])
	originalSum = 0
	first = True
	for line in f:
		weightList = map(lambda x: x.strip(), line.split(","))
		if first:
			first = False
			for i in range(len(weightList)):
				nodeList.append(Node(str(i)))
		for i in range(len(weightList)):
			if weightList[i] != '-':
				nodeList[index].addLink((nodeList[i],int(weightList[i])))
				if edgeList.count((i, index, int(weightList[i]))) == 0:
					edgeList.append((index, i, int(weightList[i])))
					originalSum += int(weightList[i])
		index += 1

	edgeList.sort(key = lambda x: -x[2])

	goodEdges = list([])

	for i in edgeList:
		nodeList[i[0]].removeLink((nodeList[i[1]], i[2]))
		if traverses(nodeList[i[0]], nodeList[i[1]], [nodeList[i[0]]]):
			nodeList[i[1]].removeLink((nodeList[i[0]], i[2]))
		else:
			nodeList[i[0]].addLink((nodeList[i[1]], i[2]))
			goodEdges.append(i[2])


	print goodEdges

	return originalSum - sum(goodEdges)

if __name__ == "__main__":
	print simpleSolution("network.txt")
