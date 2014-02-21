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
	primes = []
	for i in range(2,upperBound):
		if isPrime(i):
			primes.append(i)
	return primes

def isPrime(prime):
	'''Returns whether a number is prime or not.'''
	return factor(prime) == [prime]

def isPalindrome(palindrome, eq=lambda x,y: x==y):
	'''Returns whether a variable is a palindrome or not using a passed-in equals function.'''
	'''The passed-in palindrome must be array-index-able.'''
	length = len(palindrome)
	for i in range(length/2):
		if not eq(palindrome[i], palindrome[length-(i+1)]):
			return False
	return True

def factor(number):
	'''Returns the list of prime factors for the provided number.'''
	factors = []
	lastFactor = 1

	while number % 2 == 0:
		lastFactor = 2
		factors.append(2)
		number /= 2

	maxFactor = int(ceil(sqrt(number)))
	factor = 3

	while number > 1 and factor <= maxFactor:
		while number % factor == 0:
			lastFactor = factor
			factors.append(factor)
			number /= factor
		factor += 2

	if number != 1:
		factors.append(number)

	return factors
