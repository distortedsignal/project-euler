

# Huh, this looks familiar.
# Complexity: N
f = open("matrix.txt", "r")

matrix = []
# Complexity: N^2 (but it's a small N^2, because the int function should be VERY optimized.)
for line in f:
	# For each line, take off the newline at the end, split on the comma, map all items to 
	# integers, and then append the created list to matrix.
	# Complexity: I'm going to assume N
	matrix.append(map(int,line.strip().split(",")))

print matrix