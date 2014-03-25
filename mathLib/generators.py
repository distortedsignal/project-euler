def fibGen():
	lastTwo = [0,1]
	def next():
		new = sum(lastTwo)
		lastTwo[0] = lastTwo[1]
		lastTwo[1] = new
		return new
	return next
	