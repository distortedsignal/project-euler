from mathLib.mathLib import isPrime as p, factor as f
from time import clock as c
from math import sqrt, ceil

bigConst = 600851475143

startTime = c()
#First attempt, not bad, but not optimal (~6.7 seconds)
for i in xrange(2,bigConst):
	if bigConst % i == 0:
		if p(int(bigConst/i)):
			print int(bigConst/i)
			break

print c() - startTime

startTime = c()
#Second attempt, better, but still not great (~0.07 seconds)
for i in range(int(ceil(sqrt(bigConst))),1, -1):
	if bigConst % i == 0:
		if p(i):
			print i
			break

print c() - startTime

startTime = c()
#Optimal solution, given by Project Euler (not my work) and broken out into a different file.
print f(bigConst)[-1]

print c() - startTime