from time import time as t

def makeTri(n):
	return n * (n + 1) / 2

def makeSq(n):
	return pow(n, 2)

def makePen(n):
	return n * ((3 * n) - 1) / 2

def makeHex(n):
	return n * ((2 * n) - 1)

def makeHep(n):
	return n * ((5 * n) - 3) / 2

def makeOct(n):
	return n * ((3 * n) - 2)

def makeNums(n):
	return [makeTri(n), makeSq(n), makePen(n), makeHex(n), makeHep(n), makeOct(n)]

def walkGraph(walkList, hasList, dictList):
	# Assume that we have found the chain
	hasAllFlag = True
	for i in [0,1,2,3,4,5]:
		# And then disprove the assumption
		if hasList.count(i) == 0:
			hasAllFlag = False
			break

	if hasAllFlag:
		if walkList[0][:2] == walkList[len(walkList)-1][2:]:
			return walkList

	if not walkList[len(walkList)-1] in dictList[hasList[len(hasList)-1]]:
		return False

	for a in dictList[hasList[len(hasList)-1]][walkList[len(walkList)-1]]:
		if int(a[0]) in hasList:
			continue
		walkList.append(a[1])
		hasList.append(int(a[0]))
		rtrnValue = walkGraph(walkList, hasList, dictList)
		# check for if this is the right answer
		if type(rtrnValue) is list:
			return rtrnValue
		walkList.remove(a[1])
		hasList.remove(a[0])

	return False

# tris, sqs, pens, hexs, heps, octs = [], [], [], [], [], []

numListList = [[], [], [], [], [], []]
conDictList = [{}, {}, {}, {}, {}, {}]

limit = 10000

start = t()

for i in range(limit):
	tri, sq, pen, Hex, hep, Oct = makeNums(i)
	
	if tri > 999 and tri < 10000:
		numListList[0].append(str(tri))

	if sq > 999 and sq < 10000:
		numListList[1].append(str(sq))

	if pen > 999 and pen < 10000:
		numListList[2].append(str(pen))

	if Hex > 999 and Hex < 10000:
		numListList[3].append(str(Hex))

	if hep > 999 and hep < 10000:
		numListList[4].append(str(hep))

	if Oct > 999 and Oct < 10000:
		numListList[5].append(str(Oct))

	if tri > limit and sq > limit and pen > limit and Hex > limit and hep > limit \
	and Oct > limit:
		break

for a in range(len(numListList)):
	for i in numListList[a]:
		for b in range(len(numListList)):
			if numListList[b] == numListList[a]:
				continue

			for j in numListList[b]:
				if i[2:] == j[:2]:
					if i in conDictList[a]:
						conDictList[a][i].append([b, j])
					else:
						conDictList[a][i] = [list([b, j])]

for a in conDictList[0]:
	rtrnValue = walkGraph([a], [0], conDictList)
	if type(rtrnValue) is list:
		print "Ans:", sum(map(int, rtrnValue)), rtrnValue, "in", t()-start,"seconds"
		break

