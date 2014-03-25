def simpleSolution():
	from mathLib.generators import fibGen as f
	return sum(filter(lambda i: i % 2 == 0, f(4000000)))
	