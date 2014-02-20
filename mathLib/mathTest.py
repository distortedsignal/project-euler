import mathLib
from time import clock as cl

print "Get primes below 10000"
startTime = cl()
mathLib.getPrimes(10000)
print "Elapsed time:", cl() - startTime, "\n"

print "Get primes below 20000"
startTime = cl()
mathLib.getPrimes(20000)
print "Elapsed time:", cl() - startTime, "\n"

print "Get primes below 30000"
startTime = cl()
mathLib.getPrimes(30000)
print "Elapsed time:", cl() - startTime, "\n\n"

a,b,c,d,e = 100, 199, 214, 368, 600851475143
print "Find if numbers are prime with isPrime"
startTime = cl()
mathLib.isPrime(a)
mathLib.isPrime(b)
mathLib.isPrime(c)
mathLib.isPrime(d)
mathLib.isPrime(e)
print "Elapsed time:", cl() - startTime, "\n"

print "Find if numbers have factors with factor"
startTime = cl()
mathLib.factor(a) != [a]
mathLib.factor(b) != [b]
mathLib.factor(c) != [c]
mathLib.factor(d) != [d]
mathLib.factor(e) != [e]
print "Elapsed time:", cl() - startTime, "\n"