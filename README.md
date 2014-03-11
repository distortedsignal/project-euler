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

2. The second is searching downward from the square root of the large number and will print the first factor that it finds that is also prime.

3. The third was pulled from the Project Euler site and is the best of the three since it is the most optimized. I don't really want to go into it here, since it is quite intricate.



### Non-problem files
###### And why they're interesting

| File Name | Contents | Comments |
| :---------: | :--------: | :-------- |
| mathLib.py | | |
| | ```fibGen``` | Takes an integer as an argument and returns all Fibonacci numbers less or equal to than that number. |
| | ```getPrimes``` | Return all prime numbers less than or equal to the upperBound parameter using the Sieve of Ere. This is very slow for values over 40k. |
| | ```isPrime``` | Returns whether a number is prime or not. |
| | ```isPalindrome``` | Returns whether a variable is a palindrome or not using a passed-in equals function. The passed-in palindrome must be array-index-able. |
| | ```factor``` | Returns the list of prime factors for the provided number. |

### Problems to do
###### And badges to do them for
Badge: Problem #'s
Unlucky Squares: 64, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400, 441, 484 (Need 5)

Prime Obsession: 61, 71, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457 (Need lots)

Fibonacci Fever: 144, 233

Triangle Trophy: 66, 78, 91, 105, 120, 136, 153, 171, 190, 210, 231, 253, 276, 300, 325

Lucky Numbers: 51, 69, 75, 93, 105, 111, 115, 127, 129, 133, 135, 141, 151, 159, 163, 169, 171, 189, 193, 195, 201, 205, 211, 219, 223, 231, 235, 237, 241, 259, 261, 267, 273, 283, 285, 289, 297, 303, 307, 319, 321, 327, 331, 339, 349, 357, 361, 367, 385, 391, 393, 399, 409, 415, 421, 427, 429, 433, 451, 463 (Need lots)
