class TruthTable:
	def __init__(self):
		self.idx = 0
		self.size = 8

	def __init__(self, idx, size):
		self.idx = idx
		self.size = size

	def eval(self, arg):
		fmtStr = '{0:0' + str(self.size) + 'b}'
		return '1' == fmtStr.format(self.idx)[arg]

def generateShift(idx):
	binaryString = '{0:06b}'.format(idx)
	result = int(binaryString[0]) ^ (int(binaryString[1]) & int(binaryString[2]))
	return ((idx << 1) + result) % 64


if __name__ == "__main__":
	flag = False
	goodTT = 0

	for i in range(4096):
		flag = False
		t = TruthTable(i, 64)
		for i in range(64):
			shift = generateShift(i)
			if (t.eval(i) and t.eval(shift)) == True:
				flag = True
				break

		if not flag:
			goodTT += 1

	print "Good Truth Tables:", goodTT
	