def increment(dice, top):
	dice[len(dice) - 1] += 1
	for idx in range(len(dice) - 1, -1, -1):
		if dice[idx] > top:
			dice[idx] = 1
			dice[idx - 1] += 1

	return dice

def calcDiceProb(dice, top):
	prob = {}
	prob[sum(dice)] = 1
	while True:
		if dice == [top] * len(dice):
			break

		dice = increment(dice, top)
		diceSum = sum(dice)
		if diceSum in prob:
			prob[diceSum] += 1
		else:
			prob[diceSum] = 1

	return prob

peteProb = calcDiceProb([1, 1, 1, 1, 1, 1, 1, 1, 1], 4)
colinProb = calcDiceProb([1, 1, 1, 1, 1, 1], 6)

peteTotal = sum(peteProb.values())
colinTotal = sum(colinProb.values())

for a in peteProb:
	peteProb[a] = float(peteProb[a])/float(peteTotal)

for a in colinProb:
	colinProb[a] = float(colinProb[a])/float(colinTotal)

winOdds = 0.0
colinOdds = 0.0

for a in peteProb:
	for b in colinProb:
		if b >= a:
			break
		colinOdds += colinProb[b]

	winOdds += peteProb[a] * colinOdds
	colinOdds = 0.0

print "Pete's odds:", winOdds
