from mathLib.mathLib import isPrime
from time import clock as cl

startTime = cl()
lastNum = 1
sideLen = 1
primes = 0
while True:

	# Add 2 to sideLen to simulate that we're adding a new layer
	sideLen += 2

	# Find corners and test if they are prime
	for i in range(4):
		lastNum += sideLen - 1
		if isPrime(lastNum):
			primes += 1

	# Check if we got there
	if (float(primes)/float((2*sideLen)-1)) < .1:
		break

print sideLen, cl() - startTime
