from mathLib.mathLib import fibGen as f

print sum(filter(lambda i: i % 2 == 0, f(4000000)))