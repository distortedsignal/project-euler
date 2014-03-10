cacheDict = {}
# TODO Move this to mathLib
def sumBetter(final, sumList = [], top = False):
	if final == 0:
		return 1
	if final < 0:
		return 0
	global cacheDict
	if sumList == []:
		sumList = range(1, final)
	strSumList = ",".join(map(str, sumList))
	if cacheDict.has_key(final):
		if cacheDict[final].has_key(strSumList):
			return cacheDict[final][strSumList]
	else:
		cacheDict[final] = dict({})
	# print "Calling sumBetter with " + str(final) + " and " + str(sumList)

	sums = 0
	for i in sumList:
		newSumList = filter(lambda x: x <= i, sumList)
		strNewSumList = ",".join(map(str, newSumList))
		if top:
			# Dead code
			print i
		sums += sumBetter(final - i, newSumList)
	cacheDict[final][strSumList] = sums
	return sums

for i in range(2,40):
	print str(i), ":", str(sumBetter(i))

print "sumBetter for 100:", str(sumBetter(100))

print cacheDict
