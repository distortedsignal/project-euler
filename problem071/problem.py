def simpleSolution():
	from math import floor
	from mathLib.mathLib import factor as f, fracReduce
	numerator = 0
	value = 3.0/7.0
	bigValue = 0
	num = 0

	for newDen in range(3,1000001):
		if newDen % 10000 == 0:
			print newDen
		newFrac = fracReduce(int(floor(value * newDen)), newDen) # This is taking a LONG time
		testValue = float(newFrac[0]) / float(newFrac[1])
		if newFrac[0] > numerator and value > testValue and testValue > bigValue:
			numerator = newFrac[0]
			bigValue = float(newFrac[0]) / float(newFrac[1])
	return numerator
		

if __name__ == "__main__":
	import os, sys, inspect
	cmd_folder = os.sep.join(os.path.abspath(inspect.getfile(inspect.currentframe())).split(os.sep)[:-2])
	if cmd_folder not in sys.path:
		sys.path.insert(0, cmd_folder)
	print simpleSolution()
