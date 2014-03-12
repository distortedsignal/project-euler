from math import sqrt, ceil, atan, acos
from types import *
import operator

def fibGen(upperBound, a=1):
	'''Return all Fibonacci numbers less than or equal to the upperBound parameter.'''
	t = type(upperBound)
	assert t in [IntType, LongType, FloatType], "Upper Bound " + str(upperBound) + \
		" is of type " + str(t) + ". It should be an int, float, or a long."
	assert upperBound > a, "Upper Bound " + upperBound + " must be greater than " + a + "."
	fibList = [a, a + a]
	while fibList[-1] <= upperBound:
		fibList.append(fibList[-1] + fibList[-2])
	fibList.pop()

	return fibList

def getPrimes(upperBound):
	primes = []
	for i in range(2,upperBound):
		if isPrime(i):
			primes.append(i)
	return primes

def isPrime(prime):
	'''Returns whether a number is prime or not.'''
	if prime < 10:
		if prime == 2 or prime == 3 or prime == 5 or prime == 7:
			return True
		if prime == 4 or prime == 6 or prime == 8 or prime == 9:
			return False
	if prime % 2 == 0:
		return False
	for i in range(3, int(ceil(sqrt(prime))), 2):
		if prime % i == 0:
			return False
	return True

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

def relativePrimes(number):
	'''Returns a list of a number\'s relative primes'''
	relPrimes = [1]
	factors = set(factor(number))
	for i in range(2, number):
		tryFactors = set(factor(i))
		if factors.intersection(tryFactors) == set():
			relPrimes.append(i)
	return relPrimes

def __polarOrder(pointA, pointB):
	if pointA[1] == pointB[1]:
		if pointA[0] > pointB[0]:
			return float("inf")
		else:
			return float("-inf")
	return -float(pointB[0]-pointA[0])/float(pointB[1]-pointA[1])

def dotProduct(rayA, rayB):
	return sum(map(operator.mul, rayA, rayB))

def magnitude(ray):
	return sqrt(sum(map(lambda x: pow(x,2), ray)))

def getRay(pointA, pointB):
	return map(operator.sub, pointB, pointA)

def getAngle(pointA, pointB, pointC):
	rayA = getRay(pointA, pointB)
	rayB = getRay(pointB, pointC)
	return acos(float(dotProduct(rayA, rayB))/float(magnitude(rayA) * magnitude(rayB)))

def counterclockwise(pointA, pointB, pointC):
	x, y = 0, 1
	return ((pointB[x]-pointA[x])*(pointC[y]-pointA[y])) - \
		((pointB[y]-pointA[y])*(pointC[x]-pointA[x]))

def convex(points):
	'''Assuming that points is a set of points, find the convex hull.'''
	# Sort by y axis to get lowest point in plane
	points.sort(key = lambda x: x[1])
	lowPoint = list(points[0])
	points.remove(lowPoint)
	hullPoints = [lowPoint]
	# TODO Sort by polar angle
	points.sort(key = lambda x: __polarOrder(lowPoint, x))
	# Walk the points from the first, adding each point to a stack if we think it's in the hull
	#print lowPoint, points
	thirdPoint = list([])
	for i in range(len(points)):
		if i == len(points) - 1:
			thirdPoint = lowPoint
		else:
			thirdPoint = points[i+1]
		if counterclockwise(hullPoints[-1], points[i], thirdPoint) > 0:
			hullPoints.append(points[i])
		else:
			while counterclockwise(hullPoints[-2], hullPoints[-1], thirdPoint) <= 0:
				hullPoints.pop()
	return hullPoints

def radical(n):
	return reduce(operator.mul, set(factor(n)))
