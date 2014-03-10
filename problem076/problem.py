def sumDown(sumTo, sumList, prevNum = ""):
	print "Summing down", sumTo, "with", sumList
	if sumTo == 1:
		return 1

	sums = 0
	for i in sumList:
		print prevNum + ", " + str(i)
		sums += sumDown(sumTo - i, filter(lambda x: x <= sumTo - i, sumList), prevNum + ", " + str(i))

	print "For", sumTo, "summed", sums
	return sums

sumNum = 5
l = range(1,sumNum)
l.sort(key = lambda x: -x)
print sumDown(sumNum, l)