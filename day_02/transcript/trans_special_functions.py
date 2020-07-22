Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> L = ['giraffe', 'donkey', 'ant', 'cat', dog']
     
SyntaxError: EOL while scanning string literal
>>> L = ['giraffe', 'donkey', 'ant', 'cat', 'dog']
>>> L.sort()
>>> L
['ant', 'cat', 'dog', 'donkey', 'giraffe']
>>> 
>>> 
>>> # LAMBDA functions
>>> 
>>> lambda x, y : x + y
<function <lambda> at 0x00000116DE4A2620>
>>> f =  lambda x, y : x + y
>>> f
<function <lambda> at 0x00000116DE4A26A8>
>>> f(10, 20)
30
>>> f("every", "thing")
'everything'
>>> f([1,2,3], [4,5,6])
[1, 2, 3, 4, 5, 6]
>>> 
>>> 
>>> # SORTING
>>> 
>>> L = ['giraffe', 'donkey', 'ant', 'cat', 'dog']
>>> L.sort()
>>> L
['ant', 'cat', 'dog', 'donkey', 'giraffe']
>>> L.sort(key=lambda item:item[-1])
>>> L
['giraffe', 'dog', 'ant', 'cat', 'donkey']
>>> 
>>> 
>>> # map()
>>> 
>>> C = [100, 45, 56, 78, 34]
>>> F = []
>>> for t in C:
	F.append(t * 1.8 + 32)

	
>>> F
[212.0, 113.0, 132.8, 172.4, 93.2]
>>> F1 = map(lambda t : t * 1.8 + 32, C)
>>> F1
<map object at 0x00000116DE402FD0>
>>> list(F1)
[212.0, 113.0, 132.8, 172.4, 93.2]
>>> 
>>> # filter
>>> 
>>> L = []
>>> import random
>>> for i in range(100):
	L.append(random.randint(1, 100))

	
>>> L
[25, 60, 89, 91, 20, 62, 74, 61, 88, 61, 42, 16, 34, 15, 8, 42, 30, 64, 17, 42, 41, 10, 15, 30, 40, 47, 82, 57, 29, 6, 99, 57, 77, 6, 12, 83, 41, 81, 64, 39, 46, 48, 48, 43, 38, 80, 28, 31, 14, 96, 68, 23, 7, 76, 4, 48, 82, 21, 2, 82, 75, 39, 19, 8, 99, 3, 47, 26, 42, 22, 52, 91, 79, 86, 9, 51, 31, 62, 67, 50, 50, 45, 59, 64, 23, 43, 61, 98, 27, 33, 61, 36, 91, 13, 20, 72, 27, 88, 64, 52]
>>> 
>>> F = []
>>> for i in L:
	if(i % 5 == 0):
		F.append(i)

		
>>> F
[25, 60, 20, 15, 30, 10, 15, 30, 40, 80, 75, 50, 50, 45, 20]
>>> 
>>> F1 = filter(lambda e : (e % 5 == 0), L)
>>> F1
<filter object at 0x00000116DE4B35F8>
>>> list(F1)
[25, 60, 20, 15, 30, 10, 15, 30, 40, 80, 75, 50, 50, 45, 20]
>>> 
>>> 
>>> # zip
>>> 
>>> T1 = ('name', 'age', 'country')
>>> T2 = ('Rajesh', 45, 'India')
>>> 
>>> zip(T1, T2)
<zip object at 0x00000116DE210908>
>>> list(zip(T1, T2))
[('name', 'Rajesh'), ('age', 45), ('country', 'India')]
>>> dict(zip(T1, T2))
{'name': 'Rajesh', 'age': 45, 'country': 'India'}
>>> T3 = ('Anil', 35)
>>> dict(zip(T1, T3))
{'name': 'Anil', 'age': 35}
>>> 
>>> 
>>> D = {'name': 'Ramesh', 'age': 45, 'country': 'India'}
>>> D.items()
dict_items([('name', 'Ramesh'), ('age', 45), ('country', 'India')])
>>> zip(*D.items())
<zip object at 0x00000116DE210A88>
>>> list(zip(*D.items()))
[('name', 'age', 'country'), ('Ramesh', 45, 'India')]
>>> 
>>> 
>>> # reduce
>>> 
>>> L = [1, 2, 3, 4, 5]
>>> L = [1, 2, 3, 4, 5]
>>> 
>>> from functools import reduce
>>> reduce(lambda x, y : x + y, L)
15
>>> L = ['red', 'green', 'blue']
>>> reduce(lambda x, y : x + y, L)
'redgreenblue'
>>> 
