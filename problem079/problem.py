from time import clock as cl

def addElementToUniqueList(uniqueList, data):
	# TODO Move this to a library that ISN'T mathLib
	if uniqueList.count(data) == 0:
		uniqueList.append(data)
	return uniqueList

f = open("keylog.txt", "r")

key = []
for line in f:
	key.append(line.strip())

print key
startTime = cl()
# Split keys into ordered digit pairs
orderedPairs = list([])
passkey = ""
for i in key:
	orderedPairs = addElementToUniqueList(orderedPairs, [i[0],i[1]])
	orderedPairs = addElementToUniqueList(orderedPairs, [i[1],i[2]])
	orderedPairs = addElementToUniqueList(orderedPairs, [i[0],i[2]])

zipped = []
while orderedPairs != []:
	# Sort into pair of lists for "numbers that come first" and "numbers that come second"
	zipped = map(lambda x: list(x),zip(*orderedPairs))

	for i in range(len(zipped)):
		zipped[i] = list(zipped[i])

	# Make it so there is only one copy of a given number in the "first" or "second" list
	for a in zipped:
		for i in a:
			while a.count(i) > 1:
				a.remove(i)

	for i in zipped[0]:
		if zipped[1].count(i) == 0:
			# This is the next number
			passkey += str(i)
			# Remove all ordered pairs with this as the first number
			for j in range(len(orderedPairs)-1,-1,-1):
				if i == orderedPairs[j][0]:
					orderedPairs.remove(orderedPairs[j])

passkey += str(zipped[1][0])



print cl()-startTime, '\n', passkey
