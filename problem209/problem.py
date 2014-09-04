def generateShift(idx):
	binaryString = '{0:06b}'.format(idx)
	result = int(binaryString[0]) ^ (int(binaryString[1]) & int(binaryString[2]))
	return ((idx << 1) + result) % 64

if __name__ == "__main__":
	generatedMap = {}
	cycles = []

	for i in range(64):
		generatedMap[i] = generateShift(i)

	print generatedMap

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

	print cycles


