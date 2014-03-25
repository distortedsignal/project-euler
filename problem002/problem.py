def simpleSolution():
	from mathLib.mathLib import fibGen as f
	return sum(filter(lambda i: i % 2 == 0, f(4000000)))

if __name__ == "__main__":
	print simpleSolution()
	