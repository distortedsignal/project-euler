from math import sqrt

# def hlen(hyp, sde):
# 	return sqrt(pow(hyp, 2) - pow(sde, 2) / 4)

# def areassl(shortside, longside):
# 	return hlen(shortside, longside) * longside / 2

# def areasll(shortside, longside):
# 	return hlen(longside, shortside) * shortside / 2

# perimiter = 0
# for i in xrange(2,(1000000000/3) + 1):
# 	if areassl(i,i+1) % 1 == 0.0:
# 		perimiter += (2*i) + (i+1)

# 	if areasll(i,i+1) % 1 == 0.0:
# 		perimiter += i + (2*(i+1))

# print perimiter

def areasll(x):
	sqr = (3 * pow(x, 2)) + (8 * x) + 4
	return pow(sqrt(sqr), 2) == sqr and sqrt(sqr) % 1 == 0

def areassl(x):
	sqr = (3 * pow(x, 2)) - (2 * x) - 1
	return pow(sqrt(sqr), 2) == sqr and sqrt(sqr) % 1 == 0

limit = 1000000000
perimiterSum = 0

for x in xrange(4, limit, 4):
	area = areasll(x)
	perim = (x * 3) + 2
	if area and perim < limit:
		print "SLL:", x, x+1
		perimiterSum += perim

	if perim > limit:
		print "Found limit with x =", x
		break

print "Done with even numbers"

for x in xrange(5, limit, 4):
	area = areassl(x)
	perim = (x * 3) + 1
	if area and perim < limit:
		print "SSL:", x, x+1
		perimiterSum += perim

	if perim > limit:
		print "Found limit with x =", x
		break

print "Perimiter Sum:", perimiterSum
