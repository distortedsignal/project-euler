def simpleSolution(filePath):
	f = open(filePath, 'r')

	encrypted = []

	for line in f:
		encrypted = map(lambda x: int(x), line.split(','))

	spaceXORd = map(lambda x: x^32, encrypted)

	aXORd, bXORd, cXORd = [], [], []

	for i in range(0, len(spaceXORd), 3):
		aXORd.append(spaceXORd[i])

	for i in range(1, len(spaceXORd), 3):
		bXORd.append(spaceXORd[i])

	for i in range(2, len(spaceXORd), 3):
		cXORd.append(spaceXORd[i])

	aMode, bMode, cMode = [0, 0], [0, 0], [0, 0]

	for a in aXORd:
		if aXORd.count(a) > aMode[1]:
			aMode = [a, aXORd.count(a)]

	for b in bXORd:
		if bXORd.count(b) > bMode[1]:
			bMode = [b, bXORd.count(b)]

	for c in cXORd:
		if cXORd.count(c) > cMode[1]:
			cMode = [c, cXORd.count(c)]

	message = ""

	for i in range(len(encrypted)):
		if i % 3 == 0:
			message += chr(encrypted[i]^aMode[0])
		if i % 3 == 1:
			message += chr(encrypted[i]^bMode[0])
		if i % 3 == 2:
			message += chr(encrypted[i]^cMode[0])

	return sum(map(ord, message))

if __name__ == "__main__":
	print simpleSolution('cipher1.txt')
