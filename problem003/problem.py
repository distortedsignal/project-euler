from mathLib.mathLib import isPrime as p
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
#Optimal solution, given by Project Euler (not my work)
tmpBigConst = 0
lastFactor = 0
if bigConst % 2 == 0:
	lastFactor = 2
	tmpBigConst = bigConst / 2
	while tmpBigConst % 2 == 0:
		tmpBigConst = tmpBigConst / 2
else:
	lastFactor = 1
	tmpBigConst = bigConst
maxFactor = sqrt(tmpBigConst)
factor = 3
while tmpBigConst > 1 and factor<=maxFactor:
	if tmpBigConst % factor == 0:
		tmpBigConst = tmpBigConst / factor
		lastFactor = factor
		while tmpBigConst % factor == 0:
			tmpBigConst = tmpBigConst / factor
		maxFactor = sqrt(tmpBigConst)
	factor = factor + 2
if tmpBigConst == 1:
	print lastFactor
else:
	print tmpBigConst

print c() - startTime