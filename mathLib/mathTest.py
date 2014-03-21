import mathLib, math
from time import clock as cl
from random import random as r

# print "Get primes below 10000"
# startTime = cl()
# mathLib.getPrimes(10000)
# print "Elapsed time:", cl() - startTime, "\n"

# print "Get primes below 20000"
# startTime = cl()
# mathLib.getPrimes(20000)
# print "Elapsed time:", cl() - startTime, "\n"

# print "Get primes below 30000"
# startTime = cl()
# mathLib.getPrimes(30000)
# print "Elapsed time:", cl() - startTime, "\n\n"

# a,b,c,d,e = 100, 199, 214, 368, 600851475143
# print "Find if numbers are prime with isPrime"
# startTime = cl()
# mathLib.isPrime(a)
# mathLib.isPrime(b)
# mathLib.isPrime(c)
# mathLib.isPrime(d)
# mathLib.isPrime(e)
# print "Elapsed time:", cl() - startTime, "\n"

# print "Find if numbers have factors with factor"
# startTime = cl()
# mathLib.factor(a) != [a]
# mathLib.factor(b) != [b]
# mathLib.factor(c) != [c]
# mathLib.factor(d) != [d]
# mathLib.factor(e) != [e]
# print "Elapsed time:", cl() - startTime, "\n"

# assert mathLib.dotProduct([0,1],[1,0]) == 0, "Dot Product returned " + \
# 	str(mathLib.dotProduct([0,1],[1,0])) + " when it should have returned zero."
# assert mathLib.dotProduct([1,0],[1,0]) == 1, "Dot Product returned " + \
# 	str(mathLib.dotProduct([0,1],[1,0])) + " when it should have returned one."
# assert mathLib.dotProduct([1,0],[1,0]) == 1, "Dot Product returned " + \
# 	str(mathLib.dotProduct([1,1],[1,0])) + " when it should have returned one."
# assert mathLib.dotProduct([1,3,-5],[4,-2,-1]) == 3, "Dot Product returned " + \
# 	str(mathLib.dotProduct([1,3,-5],[4,-2,-1])) + " when it should have returned three."

# print "Dot Product works."

# assert mathLib.magnitude([1,0]) == 1, "Magnitude returned " + mathLib.magnitude([1,0]) + \
# 	" when it should have returned one."
# assert mathLib.magnitude([1,1]) > 1.4 and mathLib.magnitude([1,1]) < 1.5, "Magnitude returned " + \
# 	mathLib.magnitude([1,1]) + " when it should have returned 1.414."
# assert mathLib.magnitude([5,0]) == 5, "Magnitude returned " + mathLib.magnitude([5,0]) + \
# 	" when it should have returned 5."
# assert mathLib.magnitude([5,5]) == 5 * math.sqrt(2), "Magnitude returned " + \
# 	mathLib.magnitude([5,0]) + " when it should have returned 5*sqrt(2)."

# print "Magnitude works."

# print mathLib.getAngle([-1,0],[0,0],[1,0])
# print mathLib.getAngle([-1,0],[0,0],[0,1])
# print mathLib.getAngle([-1,0],[0,0],[-1,0])
# print mathLib.getAngle([-1,0],[0,0],[0,-1])

# print "Get angle works."

# print mathLib.counterclockwise([-1,0],[0,0],[1,0])

# print "counterclockwise works."

# print mathLib.convex([[0,0],[1,0],[0,1],[1,1]])

# assert mathLib.convex([[0,0],[1,0],[0,1],[1,1]]) == [[0,0],[1,0],[1,1],[0,1]], "Failed test " + \
# 	"where all points are on convex hull."
# assert mathLib.convex([[0,0],[2,0],[0,2],[2,2],[1,1]]) == [[0,0],[2,0],[2,2],[0,2]], "Failed " + \
# 	"test where not all points are on convex hull."
# assert mathLib.convex([[1,1],[0,0],[2,0],[0,2],[2,2]]) == [[0,0],[2,0],[2,2],[0,2]], "Failed " + \
# 	"test where not all points are on convex hull."
	