bigConst = 600851475143

#First attempt, not bad, but not optimal (~6.7 seconds)
def simpleSolution():
	from mathLib.mathLib import isPrime as p
	for i in xrange(2,bigConst):
		if bigConst % i == 0:
			if p(int(bigConst/i)):
				return int(bigConst/i)
				break


#Second attempt, better, but still not great (~0.07 seconds)
def nuancedSolution():
	from math import ceil, sqrt
	from mathLib.mathLib import isPrime as p
	for i in range(int(ceil(sqrt(bigConst))),1, -1):
		if bigConst % i == 0:
			if p(i):
				return i

#Optimal solution, given by Project Euler (not my work) and broken out into a different file.
def correctSolution():
	from mathLib.mathLib import factor as f
	return f(bigConst)[-1]

if __name__ == "__main__":
	import os, sys, inspect
	cmd_folder = os.sep.join(os.path.abspath(inspect.getfile(inspect.currentframe())).split(os.sep)[:-2])
	if cmd_folder not in sys.path:
		sys.path.insert(0, cmd_folder)
	from math import sqrt, ceil
	print correctSolution()
	