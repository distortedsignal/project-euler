from mathLib.mathLib import convex
from time import clock as cl

f = open("triangles.txt", "r")

triangles = []

for line in f:
	# For each line, take off the newline at the end, split on the comma, map all items to 
	# integers, and then append the created list to triangles.
	# Complexity: I'm going to assume N
	triangles.append(map(int,line.strip().split(",")))
startTime = cl()
trianglesContainingOrigin = 0

# Treating this as a convex hull problem (http://en.wikipedia.org/wiki/Convex_hull)
for triangle in triangles:
	points = [[triangle[0],triangle[1]],[triangle[2],triangle[3]],[triangle[4],triangle[5]],[0,0]]

	convexPoints = convex(points)

	if convexPoints.count([0,0]) == 0:
		trianglesContainingOrigin += 1

print trianglesContainingOrigin, cl() - startTime
