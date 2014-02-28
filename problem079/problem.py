f = open("keylog.txt", "r")

key = []
for line in f:
	key.append(line.strip())

print key.

# firstFreq = {'0': 0, '1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0}
# for a in key:
# 	firstFreq[a[0]] += 1

# print firstFreq