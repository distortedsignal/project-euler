def simpleSolution():
	from mathLib.mathLib import fibGen as f
	return sum(filter(lambda i: i % 2 == 0, f(4000000)))

if __name__ == "__main__":
	import os, sys, inspect
	cmd_folder = os.sep.join(os.path.abspath(inspect.getfile(inspect.currentframe())).split(os.sep)[:-2])
	if cmd_folder not in sys.path:
		sys.path.insert(0, cmd_folder)
	print simpleSolution()
	