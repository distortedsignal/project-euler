from math import sqrt, atan, tan
from copy import deepcopy

def reflect(beamSlope, beamDir, wallSlope):
	'''Return the slope (as a float) of a reflected beam given the incident 
		beam slope (as a float), the beam direction (as 1 for moving in the positive x, 0 for 
		infinite slope, or -1 for moving in the negative x direction), and the 
		slope of the wall (as a float).'''

	assert type(beamSlope) is float, "beamSlope " + str(beamSlope) + " must be a float."
	assert type(beamDir) is int and beamDir in [-1, 0, 1], "beamDir " + str(beamDir) + \
		" must be in [-1, 0, 1]."
	assert type(wallSlope) is float, "wallSlope" + str(wallSlope) + "must be a float."
	if beamSlope in [float("inf"), float("-inf")]:
		assert beamDir == 0, "If the beam slope is infinite, the direction should be zero."
	else:
		assert beamDir in [1, -1], "If the beam slope is non-infinate, there must be a " + \
			"direction associated with the beam."

	wallNormal = 0
	if wallSlope == 0:
		wallNormal = float("inf")
	elif abs(wallSlope) == float("inf"):
		wallNormal = 0
	else:
		wallNormal = -1/wallSlope
	innerAngle = atan((beamSlope - wallNormal)/(1 + (beamSlope*wallNormal)))
	return tan(atan(wallSlope) - innerAngle)

oldSpot = [0, 10.1]
newSpot = [1.4, -9.6]
bounce = 0

while (newSpot[0] < -0.01 or newSpot[0] > 0.01) and newSpot[1] < 9:
	wallSlope = 0
	beamSlope = 0
	beamDir = 0

	if newSpot[1] == 0.0:
		wallSlope = float("inf")
	else:
		wallSlope = -4*newSpot[0]/newSpot[1]

	beamSlope = float(newSpot[1] - oldSpot[1])/float(newSpot[0] - oldSpot[0])
	beamDir = round(float(newSpot[0] - oldSpot[0])/float(abs(newSpot[0] - oldSpot[0])))

	reflectedSlope = reflect(beamSlope, int(round(beamDir)), wallSlope)
	print reflectedSlope
	bounce += 1
	oldSpot = deepcopy(newSpot)
	newSpot = calcNewSpot()
print bounce
