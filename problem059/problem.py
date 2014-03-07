f = open('cipher1.txt', 'r')

encrypted = []

for line in f:
	encrypted = map(lambda x: int(x), line.split(','))

print encrypted