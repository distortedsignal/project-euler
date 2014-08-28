from math import sqrt

n = 0
while True:
	minus = pow(3 - (2*sqrt(2)), n)
	plus = pow(3 + (2*sqrt(2)), n)

	# This equation found by plugging "t * (t-1) = 2 * n * (n-1)" into Wolfram|Alpha.
	disks = (- minus - (sqrt(2) * minus) - plus	+ (sqrt(2) * plus) + 2) / 4
	n += 1

	if disks <= 1000000000000:
		continue

	# Again, equation from Wolfram|Alpha
	blue = round(((2 * minus) + (sqrt(2) * minus) + (2 * plus) - (sqrt(2) * plus) + 4) / 8)

	print disks, blue, n
	break
