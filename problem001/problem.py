# My solution, simple.
def simpleSolution():
	return sum([i for i in range(1000) if i % 3 == 0 or i % 5 == 0])

if __name__ == "__main__":
	print simpleSolution()

#Optimal solution given by project euler
