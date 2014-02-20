project-euler
=============

Some project euler problems and libraries

### Problems that are working
###### And some interesting notes about their implementations



##### Problem 1
A Python one-liner involving a list comprehension and the ```sum``` function.

##### Problem 2
A Python one-liner involving a lambda, and the ```filter``` and ```sum``` functions. Importing and aliasing ```fibGen``` from mathLib.



### Non-problem files
###### And why they're interesting

| File Name | Contents | Comments |
| :---------: | :--------: | :-------- |
| mathLib.py | | |
| | ```fibGen``` | Takes an integer as an argument and returns all Fibonacci numbers less or equal to than that number. |
| | ```getPrimes``` | Return all prime numbers less than or equal to the upperBound parameter using the Sieve of Ere. This is very slow for values over 40k. |
| | ```isPrime``` | Returns whether a number is prime or not. |