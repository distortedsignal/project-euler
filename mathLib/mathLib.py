from math import sqrt, ceil

def fibGen(upperBound, a=1, b=2):
	'''Return all Fibonacci numbers less than or equal to the upperBound parameter.'''
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

def getPrimes(upperBound):
	'''Return all prime numbers less than or equal to the upperBound parameter.'''
	'''This is very slow for values over 40k.'''
	primeOptions = range(2,upperBound+1)
	for i in primeOptions:
		j = 2
		while i * j <= upperBound:
			try:
				primeOptions.remove(i * j)
			except ValueError, e:
				pass
			j += 1
	return primeOptions

def isPrime(prime):
	'''Returns whether a number is prime or not.'''
	r = range(2,int(ceil(sqrt(prime))))
	for i in r:
		if prime % i == 0:
			return False
	return True

def isPalindrome(palindrome, eq=lambda x,y: x==y):
	'''Returns whether a variable is a palindrome or not using a passed-in equals function.'''
	length = len(palindrome)
	for i in range(length/2):
		if not eq(palindrome[i], palindrome[length-(i+1)]):
			return False
	return True