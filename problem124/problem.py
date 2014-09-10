def product(factorSet):
	prod = 1
	for i in factorSet:
		prod *= i
	return prod

def simpleSolution():
	from mathLib.mathLib import factor
	nums = [(i, product(set(factor(i)))) for i in range(1,100001)]
	nums.sort(key = lambda x: x[1])
	return nums[9999]


if __name__ == "__main__":
	import os, sys, inspect
	cmd_folder = os.sep.join(os.path.abspath(inspect.getfile(inspect.currentframe())).split(os.sep)[:-2])
	if cmd_folder not in sys.path:
		sys.path.insert(0, cmd_folder)
	print simpleSolution()