Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
 RESTART: C:/Users/Purushotham/Desktop/oracle_july/day_02/examples/primes.py 
Enter a number: 12
The number is not prime
>>> 
 RESTART: C:/Users/Purushotham/Desktop/oracle_july/day_02/examples/primes.py 
Enter a number: 13
The number is prime
>>> list(range(2, 1))
[]
>>> 
 RESTART: C:/Users/Purushotham/Desktop/oracle_july/day_02/examples/primes.py 
Enter a number: 1
The number is prime
>>> 
 RESTART: C:/Users/Purushotham/Desktop/oracle_july/day_02/examples/primes.py 
Enter a number: 2
The number is prime
>>> list(range(2, 1, -1))
[2]
>>> list(range(2, 0, -1))
[2, 1]
>>> 
 RESTART: C:/Users/Purushotham/Desktop/oracle_july/day_02/examples/primes2.py 
Enter a number: 12
The number is not prime
>>> 
 RESTART: C:/Users/Purushotham/Desktop/oracle_july/day_02/examples/primes2.py 
Enter a number: 47
The number is prime
>>> import primes2
Enter a number: 12
The number is not prime
>>> primes2.checkprime(100)
False
>>> primes2.checkprime(1)
True
>>> for n in range(10):
	primes2.checkprime(n)

	
True
True
True
True
False
True
False
True
False
False
>>> 
 RESTART: C:/Users/Purushotham/Desktop/oracle_july/day_02/examples/project_a.py 
Enter a number: 3
The number is prime
Enter a start point: 10
Enter a end point: 100
----------------------------------------
PRIMES: 
[11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
>>> 
 RESTART: C:/Users/Purushotham/Desktop/oracle_july/day_02/examples/primes2.py 
Enter a number: 12
The number is not prime
>>> 
 RESTART: C:/Users/Purushotham/Desktop/oracle_july/day_02/examples/project_a.py 
Enter a start point: 10
Enter a end point: 100
----------------------------------------
PRIMES: 
[11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
>>> 
 RESTART: C:/Users/Purushotham/Desktop/oracle_july/day_02/examples/project_b.py 
(q to quit)--> 12
(q to quit)--> 34
(q to quit)--> 45
(q to quit)--> 56
(q to quit)--> 67
(q to quit)--> dd
(q to quit)--> ff
(q to quit)--> gg
(q to quit)--> hh
(q to quit)--> 56
(q to quit)--> 67
(q to quit)--> 78
(q to quit)--> q
------------------------------------------------------------
[12, 34, 45, 56, 67, 56, 67, 78]
>>> 
 RESTART: C:/Users/Purushotham/Desktop/oracle_july/day_02/examples/project_b.py 
(q to quit)--> 12
(q to quit)--> 23
(q to quit)--> 34
(q to quit)--> 45
(q to quit)--> 56
(q to quit)--> 67
(q to quit)--> 78
(q to quit)--> 89
(q to quit)--> 45
(q to quit)--> 56
(q to quit)--> 67
(q to quit)--> 45
(q to quit)--> 34
(q to quit)--> 23
(q to quit)--> fsda
(q to quit)--> dfg
(q to quit)--> xcbv
(q to quit)--> asdgf
(q to quit)--> asdf
(q to quit)--> wer
(q to quit)--> asdf
(q to quit)--> 23
(q to quit)--> 45
(q to quit)--> q
--------------------------------------------------------------------------------
MAXIMUM   :  89
MINIMUM   :  12
AVERAGE   :  46.375
MEDIAN    :  45.0
PRIMES    :  6
--------------------------------------------------------------------------------
>>> import primes2
>>> 
