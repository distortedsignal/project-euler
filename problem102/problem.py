from math import atan

def polarOrder(pointA, pointB):
	if pointA[1] == pointB[1]:
		if pointA[0] > pointB[0]:
			print "Got polar order", pointA, pointB, "Returning negative infinity."
			return float("-inf")
		else:
			print "Got polar order", pointA, pointB, "Returning positive infinity."
			return float("inf")
	print "Got polar order", pointA, pointB, "Returning", str(float(pointB[0]-pointA[0])/float(pointB[1]-pointA[1])) + "."
	return float(pointB[0]-pointA[0])/float(pointB[1]-pointA[1])

def convex(points):
	# Sort by y axis to get lowest point in plane
	points.sort(key = lambda x: x[1])
	lowPoint = list(points[0])
	points.remove(lowPoint)
	# TODO Sort by polar angle
	points.sort(key = lambda x: -polarOrder(lowPoint, x))
	# Walk the points from the first, adding each point to a stack if we think it's in the hull
	print lowPoint, points

	points.append(lowPoint)
	return points

f = open("triangles.txt", "r")

triangles = []

for line in f:
	# For each line, take off the newline at the end, split on the comma, map all items to 
	# integers, and then append the created list to triangles.
	# Complexity: I'm going to assume N
	triangles.append(map(int,line.strip().split(",")))

trianglesContainingOrigin = 0

# Treating this as a convex hull problem (http://en.wikipedia.org/wiki/Convex_hull)
for triangle in triangles:
	points = [[triangle[0],triangle[1]],[triangle[2],triangle[3]],[triangle[4],triangle[5]],[0,0]]

	convexPoints = convex(points)

	if convexPoints.count([0,0]) == 0:
		trianglesContainingOrigin += 1

print trianglesContainingOrigin
