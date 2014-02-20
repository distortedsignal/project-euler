def fibGen(upperBound, a=1, b=2):
	'''Return all Fibonacci numbers less than or equal to the upperBound parameter'''
	newA = a + b
	newB = b + newA

	if newA > upperBound:
		return [a,b]

	if newB > upperBound:
		return [a,b,newA]

	fibList = fibGen(upperBound, newA, newB)
	fibList.insert(0,b)
	fibList.insert(0,a)
	return fibList