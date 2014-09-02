from math import factorial as f

def factorialize(fact):
	factSum = 0
	factStr = str(fact)
	for i in factStr:
		factSum += f(int(i))
	return factSum


factorialSet = set([])
fact = 0
sixtyCycles = 0

for i in range(1,1000000):
	if i % 100000 == 0:
		print i

	factorialSet.add(i)
	fact = factorialize(i)

	while fact not in factorialSet:
		factorialSet.add(fact)
		if len(factorialSet) > 60:
			break
		fact = factorialize(fact)

	if len(factorialSet) == 60:

		sixtyCycles += 1

	factorialSet = set([])
	fact = 0

print "Cycles below 1,000,000:", sixtyCycles