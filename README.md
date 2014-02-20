project-euler
=============

Some project euler problems and libraries

### Problems that are working
###### And some interesting notes about their implementations

##### Problem 1
A Python one-liner involving a list comprehension and the ```sum``` function.

##### Problem 2
A Python one-liner involving a lambda, and the ```filter``` and ```sum``` functions. Importing and aliasing ```fibGen``` from mathLib.

##### Problem 3
Three solutions to the problem:
1. The first is a relatively naive search for a large prime. It can be read as follows: Given a large prime, for each number less than the prime, divide the large number by the chosen number. If the result is prime, print it and stop searching.
1. The second is searching downward from the square root of the large number and will print the first factor that it finds that is also prime.
1. The third was pulled from the Project Euler site and is the best of the three since it is the most optimized. I don't really want to go into it here, since it is quite intricate.



### Non-problem files
###### And why they're interesting

| File Name | Contents | Comments |
| :---------: | :--------: | :-------- |
| mathLib.py | | |
| | ```fibGen``` | Takes an integer as an argument and returns all Fibonacci numbers less or equal to than that number. |
| | ```getPrimes``` | Return all prime numbers less than or equal to the upperBound parameter using the Sieve of Ere. This is very slow for values over 40k. |
| | ```isPrime``` | Returns whether a number is prime or not. |