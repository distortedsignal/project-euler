from time import clock as cl

sf, fook, fh, fl, st, took, tp, pair, hc = "StraightFlush", "FourOfAKind", "FullHouse", "Flush", \
	"Straigh", "ThreeOfAKind", "TwoPair", "Pair", "HighCards"

def cardValue(card):
	value = 0
	if card[0] in ['2', '3', '4', '5', '6', '7', '8', '9']:
		value = int(card[0])
	elif card[0] == 'T':
		value = 10
	elif card[0] == 'J':
		value = 11
	elif card[0] == 'Q':
		value = 12
	elif card[0] == 'K':
		value = 13
	elif card[0] == 'A':
		value = 14
	else:
		value = float("inf")
	return value

def scoreHand(handValue):
	keyList = handValue.keys()
	if keyList.count(sf) > 0:
		return 8
	if keyList.count(fook) > 0:
		return 7
	if keyList.count(fh) > 0:
		return 6
	if keyList.count(fl) > 0:
		return 5
	if keyList.count(st) > 0:
		return 4
	if keyList.count(took) > 0:
		return 3
	if keyList.count(tp) > 0:
		return 2
	if keyList.count(pair) > 0:
		return 1
	return 0

def handBetter(handValue1, handValue2):
	hand1Score = scoreHand(handValue1)
	hand2Score = scoreHand(handValue2)

	if hand1Score > hand2Score:
		return True

	if hand2Score > hand1Score:
		return False

	keyList = handValue1.keys()

	for scoreType in keyList:
		for i in range(len(handValue1[scoreType])):
			if handValue1[scoreType][i] > handValue2[scoreType][i]:
				return True
			if handValue1[scoreType][i] < handValue2[scoreType][i]:
				return False

	return False

def getValue(hand):
	handValue = dict({})

	# Sort cards
	hand.sort(key = lambda x: -cardValue(x))

	found = False
	# If there is a straight flush
	for i in range(len(hand)-1):
		if cardValue(hand[i]) == cardValue(hand[i+1]) + 1 and hand[i][1] == hand[i+1][1]:
			found = True
			continue
		else:
			found = False
			break
	if found:
		handValue[sf] = [cardValue(hand[0])]
		return handValue

	# If there is a four-of-a-kind
	if (hand[0][0] == hand[1][0] and hand[1][0] == hand[2][0] and hand[2][0] == hand[3][0]) \
		or (hand[4][0] == hand[1][0] and hand[1][0] == hand[2][0] and hand[2][0] == hand[3][0]):
		found = True
		if cardValue(hand[0]) == cardValue(hand[1]):
			handValue[fook] = cardValue(hand[0])
			hand = hand[4]
		else:
			handValue[fook] = [cardValue(hand[1])]
			hand = hand[0]

	# If there is a full house
	if not found:
		if (hand[0][0] == hand[1][0] and hand[1][0] == hand[2][0] and hand[3][0] == hand[4][0]) or \
			(hand[0][0] == hand[1][0] and hand[2][0] == hand[3][0] and hand[3][0] == hand[4][0]):
			if hand[1][0] == hand[2][0]:
				handValue[fh] = [cardValue(hand[0]), cardValue(hand[4])]
			else:
				handValue[fh] = [cardValue(hand[4]), cardValue(hand[0])]
			return handValue

	# If there is a flush
	if not found:
		if hand[0][1] == hand[1][1] and hand[1][1] == hand[2][1] and hand[2][1] == hand[3][1] and \
			hand[3][1] == hand[4][1]:
			handValue[fl] = map(lambda x: cardValue(x), hand)
			return handValue

	# If there is a striaght
	for i in range(len(hand)-1):
		if cardValue(hand[i]) == cardValue(hand[i+1]) + 1:
			found = True
			continue
		else:
			found = False
			break
	if found:
		handValue[fl] = [cardValue(hand[0])]
		return handValue

	# If there is a three-of-a-kind
	if not found:
		if (hand[0][0] == hand[1][0] and hand[1][0] == hand[2][0]) or \
			(hand[1][0] == hand[2][0] and hand[2][0] == hand[3][0]) or \
			(hand[2][0] == hand[3][0] and hand[3][0] == hand[4][0]):
			found = True
			if hand[2][0] == hand[1][0]:
				if hand[1][0] == hand[0][0]:
					handValue[took] = [cardValue(hand[0])]
					hand = hand[3:]
				else:
					handValue[took] = [cardValue(hand[1])]
					hand = [hand[0], hand[4]]
			else:
				handValue[took] = [cardValue(hand[2])]
				hand = hand[:2]

	# If there are two-pair
	if not found:
		if hand[0][0] == hand[1][0] and hand[2][0] == hand[3][0]:
			found = True
			handValue[tp] = [cardValue(hand[0]), cardValue(hand[2])]
			hand = hand[4]
		elif hand[0][0] == hand[1][0] and hand[3][0] == hand[4][0]:
			found = True
			handValue[tp] = [cardValue(hand[0]), cardValue(hand[3])]
			hand = hand[2]
		elif hand[1][0] == hand[2][0] and hand[3][0] == hand[4][0]:
			found = True
			handValue[tp] = [cardValue(hand[1]), cardValue(hand[3])]
			hand = hand[0]

	# If there is a pair
	if not found:
		if hand[0][0] == hand[1][0]:
			handValue[pair] = [cardValue(hand[0])]
			hand = hand[2:]
		elif hand[1][0] == hand[2][0]:
			handValue[pair] = [cardValue(hand[1])]
			hand = [hand[0], hand[3], hand[4]]
		elif hand[2][0] == hand[3][0]:
			handValue[pair] = [cardValue(hand[2])]
			hand = [hand[0], hand[1], hand[4]]
		elif hand[3][0] == hand[4][0]:
			handValue[pair] = [cardValue(hand[3])]
			hand = hand[:2]

	# Fill the rest into "high cards"
	handValue[hc] = map(lambda x: cardValue(x), hand)

	return handValue

def simpleSolution(filePath):
	f = open(filePath, 'r')
	hand1Wins = 0

	for i in f:
		# Split into two hands
		cardList = i.strip().split(' ')

		hand1, hand2 = cardList[:5], cardList[5:]

		# For both hands, figure out what hand value is
		hand1Value = getValue(hand1)
		hand2Value = getValue(hand2)

		# Compare hand value
		if handBetter(hand1Value, hand2Value):
			hand1Wins += 1

	return hand1Wins

if __name__ == "__main__":
	print simpleSolution('poker.txt')