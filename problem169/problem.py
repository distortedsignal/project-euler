from time import time

# Code for investigation of patterns that this problem uses
def tobi(target):
	return list(str(bin(target))[2:])

def countOptions(bitristring, options):
	options.add(tuple(bitristring))
	for i in range(len(bitristring)):
		if bitristring[i] == '0':
			continue

		if i == (len(bitristring) - 1):
			break

		if bitristring[i+1] != '0':
			continue

		bitristring[i] = str(int(bitristring[i]) - 1)
		bitristring[i+1] = '2'
		if not (tuple(bitristring) in options):
			options = countOptions(bitristring, options)

		bitristring[i] = str(int(bitristring[i]) + 1)
		bitristring[i+1] = '0'

	return options

target = 6
bts = tobi(target)
start = time()
options = countOptions(bts, set([]))
end = time()
print "\nTarget:", target, "\n\tBTS:", "".join(bts), "\n\tAnswer:", len(options), "\n\tTime:", end - start

# From the previous code, some observations:
#	The patterns in this problem are symmetric - this was expected.
#		All numbers that follow the pattern of 2^n have n+1 was of being represented.
#			Eg. n = 3: 8: 1000, 0200, 0120, 0112
#		All numbers that follow the pattern ((2^n) - 2) have n ways of being represented.
#			Eg. n = 3: 6: 110, 102, 022
#		All numbers that follow the pattern ((2^n) - 1) have exactly one way to be represented. 
#			Eg. n = 3: 7: 111
#		All numbers that follow the pattern ((2^(n+1) - 1) + ((2^n) - 1)) / 2 have exactly two ways to be represented.
#			Eg. n = 3: 7 + 15 / 2: 11: 1011, 0211
#		All numbers in a set can be "rotated" around this "2-point" to form the numbers in the upper/lower half.
#	It is relatively striaghtforward to find some points in these sets
#		For the "top" points in the series:
#			The point these are at are defined by a "Tick-tock" series:
#				Start with the numbers 4 and 6
#				Start with the word tick
#				If the word is tick,
#					Replace the first number with (1 + firstnumber) * 2
#					Replace the second number with secondnumber * 2
#					Replace the word with tock
#				Else
#					Replace the first number with firstnumber * 2
#					Replace the second number with (1 + secondnumber) * 2
#					Replace the word with tick
#				Iterate on this sequence
#		The top values can be defined as a Fibonacci series:
#			2/2 = 2
#			4/6 = 3
#			10/12 = 5
#			etc.

