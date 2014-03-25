def simpleSolution():
	from mathLib.mathLib import isPrime
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

	return sideLen

if __name__ == "__main__":
	import os, sys, inspect
	cmd_folder = os.sep.join(os.path.abspath(inspect.getfile(inspect.currentframe())).split(os.sep)[:-2])
	if cmd_folder not in sys.path:
		sys.path.insert(0, cmd_folder)
	print simpleSolution()
