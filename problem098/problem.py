from string import replace
from math import sqrt

def genSquares(maxLen):
	squares = []
	i = 1
	while True:
		squares.append(pow(i,2))
		if len(str(squares[len(squares)-1])) > maxLen:
			squares.remove(squares[len(squares)-1])
			break
		i += 1
	return squares

def sortWordsOnLength(wordList):
	lastWord = wordList[0]
	thisList = []
	wordListList = []
	for i in wordList:
		if len(i) == len(lastWord):
			thisList.append(i)
		else:
			wordListList.append(thisList)
			thisList = [i]

		lastWord = i

	return wordListList

def sortChars(word):
	letterList = list(word)
	letterList.sort()
	return letterList

def checkForNonAnagrams(wordList):
	charSortedWordList = list(wordList)
	charSortedWordList = map(lambda x: sortChars(x), charSortedWordList)
	for i in xrange(len(charSortedWordList)-1,-1,-1):
		if charSortedWordList.count(charSortedWordList[i]) == 1:
			wordList.remove(wordList[i])
	return wordList

def verifyAnagrams(wordListList):
	for i in xrange(len(wordListList)):
		wordListList[i] = checkForNonAnagrams(wordListList[i])

	return wordListList

def compileWordLists(wordListList):
	wordList = []
	for i in wordListList:
		wordList.extend(i)

	return wordList

def filterNonAnagrams(wordList):
	wordListList = sortWordsOnLength(wordList)
	wordListList = verifyAnagrams(wordListList)
	return compileWordLists(wordListList)

def areAnagrams(word1, word2):
	word1CharsSort = list(word1)
	word1CharsSort.sort()
	word2CharsSort = list(word2)
	word2CharsSort.sort()
	return word1CharsSort == word2CharsSort

def noDoubles(squareNum, word1):
	squareNumStr = str(squareNum)
	letterMap = {}
	for a in xrange(len(word1)):
		if word1[a] not in letterMap:
			letterMap[word1[a]] = squareNumStr[a]
		else:
			if letterMap[word1[a]] != squareNumStr[a]:
				return False

		if squareNumStr[a] not in letterMap:
			letterMap[squareNumStr[a]] = word1[a]
		else:
			if letterMap[squareNumStr[a]] != word1[a]:
				return False

	return True

def rearrange(squareNum, word1, word2):
	letterMap = {}
	for a in xrange(len(word1)):
		letterMap[word1[a]] = str(squareNum)[a]

	possibleSquare = ""
	for a in word2:
		possibleSquare += letterMap[a]

	return int(possibleSquare)


f = open('words.txt', 'r')
wordList = sorted(replace(f.read(), '"', '').split(","), key = lambda x: -len(x)) 
wordList = filterNonAnagrams(wordList)
squares = genSquares(len(wordList[0]))
squares.sort(key = lambda x: -x)
# print squares
# print wordList
tempWordList = []
tempWordList2 = []
flag = False
for i in squares:
	tempWordList = filter(lambda x: len(x) == len(str(i)), wordList)
	for a in tempWordList:
		tempWordList2 = [x for x in tempWordList if x != a]
		for b in tempWordList2:
			if areAnagrams(a, b) and noDoubles(i, a):
				possibleSquare = rearrange(i, a, b)
				if possibleSquare == pow(round(sqrt(possibleSquare)), 2) and \
				str(possibleSquare)[0] != 0 and \
				len(str(possibleSquare)) == len(str(i)):
					print "Answer:", i, "Other square:", possibleSquare
					print "Word:", a, "Anagram:", b
					flag = True
					break

		if flag:
			break
	
	if flag:
		break


