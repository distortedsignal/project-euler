from decimal import Decimal, getcontext
from fractions import Fraction

fractionList = [Decimal(1.0/2.0)]

print fractionList

while len(fractionList) < 1000:
	fractionList.append(Decimal(1 / (2 + fractionList[len(fractionList) - 1])))
	fractionList[len(fractionList) - 2] = Decimal(1 + fractionList[len(fractionList) - 2])

print fractionList

for i in range(len(fractionList)):
	fractionList[i] = Fraction(fractionList[i]).limit_denominator()

print fractionList
