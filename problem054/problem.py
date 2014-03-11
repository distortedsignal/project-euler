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

def handBetter(handValue1, handValue2):
	pass

def getValue(hand):
	handValue = dict({})

	# Sort cards
	hand.sort(key = lambda x: -cardValue(x))
	print hand
	found = True
	# If there is a straight flush
	for i in range(len(hand)-1):
		if cardValue(hand[i]) == cardValue(hand[i+1]) and hand[i][1] == hand[i+1][1]:
			continue
		else:
			found = False
			break
	if found:
		handValue["StraightFlush"] = hand[0][0]
		return handValue

	found = True
	# If there is a four-of-a-kind
	if 

	# If there is a full house

	# If there is a flush

	# If there is a striaght

	# If there is a three-of-a-kind

	# If there are two-pair

	# If there is a pair

	# Fill the rest into "high cards"

	return handValue
	
f = open('poker.txt', 'r')

hand1Wins = 0

for i in f:
	# Split into two hands
	cardList = i.strip().split(' ')
	print cardList
	hand1, hand2 = cardList[:5], cardList[5:]
	print hand1, hand2

	# For both hands, figure out what hand value is
	hand1Value = getValue(hand1)
	hand2Value = getValue(hand2)

	# Compare hand value
	if handBetter(hand1Value, hand2Value):
		hand1Wins += 1

print hand1Wins