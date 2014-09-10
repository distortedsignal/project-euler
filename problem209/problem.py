from time import time

def fibGen(x, y):
	fibGen.lower, fibGen.higher, fibGen.count = x, y, 2
	def g():
		fibGen.lower, fibGen.higher = fibGen.higher, fibGen.lower + fibGen.higher
		fibGen.count += 1
		return (fibGen.higher, fibGen.count)
	return g

def countOptions(digits):
	# The realization that this is a Fibonacci sequence came from David "Plasma" Paul.
	# And I honestly don't know how this works. If anyone can explain this to me
	# mathematically, please shoot me a message.
	if digits == 1:
		return 1

	if digits == 2:
		return 3

	gen = fibGen(1,3)

	while True:
		fibTuple = gen()
		if fibTuple[1] == digits:
			return fibTuple[0]

def generateShift(idx):
	binaryString = '{0:06b}'.format(idx)
	result = int(binaryString[0]) ^ (int(binaryString[1]) & int(binaryString[2]))
	return ((idx << 1) + result) % 64

if __name__ == "__main__":
	generatedMap = {}
	cycles = []
	t = time()
	for i in range(64):
		generatedMap[i] = generateShift(i)

	# If you can't write the code for it, you don't know what you're doing
	cycles = []

	inserted = False

	for i in generatedMap:
		inserted = False
		for a in cycles:
			if a.count(i) > 0:
				inserted = True
				break

		if not inserted:
			holder = i
			newCycle = []
			while True:
				if newCycle.count(holder) == 0:
					newCycle.append(holder)
					holder = generatedMap[holder]
				else:
					break
					
			cycles.append(newCycle)

	prod = 1

	for i in cycles:
		prod *= countOptions(len(i))

	print prod
