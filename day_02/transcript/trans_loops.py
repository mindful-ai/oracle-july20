Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # LOOPS
>>> 
>>> # ----------------------- iteration in a for loop
>>> 
>>> s = "python"
>>> L = ["red", "green", "blue", "yellow"]
>>> T = ('a', 'e', 'i', 'o', 'u')
>>> S = set('abcdefg')
>>> S
{'b', 'd', 'g', 'f', 'c', 'a', 'e'}
>>> D = { 'name':'anil', 'age':35, 'company':'Oracle' }
>>> 
>>> for ch in s:
	print('Hello Oracle')

	
Hello Oracle
Hello Oracle
Hello Oracle
Hello Oracle
Hello Oracle
Hello Oracle
>>> for ch in s:
	print(ch, ' Hello ORacle')

	
p  Hello ORacle
y  Hello ORacle
t  Hello ORacle
h  Hello ORacle
o  Hello ORacle
n  Hello ORacle
>>> 
>>> for x in s:
	print(ch, end='-')

	
n-n-n-n-n-n-
>>> for x in s:
	print(x, end='-')

	
p-y-t-h-o-n-
>>> for x in s:
	print(x.upper(), end='')

	
PYTHON
>>> for x in s:
	print(x.upper(), end=' ')

	
P Y T H O N 
>>> for item in L:
	print(item.capitalize(), len(item))

	
Red 3
Green 5
Blue 4
Yellow 6
>>> L
['red', 'green', 'blue', 'yellow']
>>> for item in T:
	print(item)

	
a
e
i
o
u
>>> for item in T:
	print(item, end='')

	
aeiou
>>> for item in T:
	print(item, end='-->')

	
a-->e-->i-->o-->u-->
>>> for item in "Python":
	print('Python')

	
Python
Python
Python
Python
Python
Python
>>> for item in "oracle":
	print(s)

	
python
python
python
python
python
python
>>> for elem in S:
	print(elem.upper())

	
B
D
G
F
C
A
E
>>> for k in D:
	print(k)

	
name
age
company
>>> for v in D.values():
	print(v)

	
anil
35
Oracle
>>> for k in D.keys():
	print(v)

	
Oracle
Oracle
Oracle
>>> for k in D.keys():
	print(k)

	
name
age
company
>>> for item in D.items():
	print(items)

	
Traceback (most recent call last):
  File "<pyshell#61>", line 2, in <module>
    print(items)
NameError: name 'items' is not defined
>>> for item in D.items():
	print(item)

	
('name', 'anil')
('age', 35)
('company', 'Oracle')
>>> D.items()
dict_items([('name', 'anil'), ('age', 35), ('company', 'Oracle')])
>>> k, v = ('name', 'anil')
>>> k
'name'
>>> v
'anil'
>>> for k, v in D.items():
	print(k, v)

	
name anil
age 35
company Oracle
>>> D
{'name': 'anil', 'age': 35, 'company': 'Oracle'}
>>> D1 = {}
>>> for k, v in D.items():
	D1.setdefault(v, k)

	
'name'
'age'
'company'
>>> D1
{'anil': 'name', 35: 'age', 'Oracle': 'company'}
>>> # -------------------------------------- Working with numbers in for loop
>>> 
>>> 
>>> 
>>> N = [0, 1, 2, 3, 4]
>>> for i in N:
	print(i, i**2, i**3)

	
0 0 0
1 1 1
2 4 8
3 9 27
4 16 64
>>> 
>>> range(10)
range(0, 10)
>>> list(range(10))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> list(range(20, 30))
[20, 21, 22, 23, 24, 25, 26, 27, 28, 29]
>>> list(range(0, 100, 5))
[0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95]
>>> list(range(-100, 0, -2))
[]
>>> list(range(-9))
[]
>>> list(range(15, 0, -1))
[15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
>>> list(range(15, 0, -3))
[15, 12, 9, 6, 3]
>>> 
>>> 
>>> # Pyramid of stars
>>> 
>>> N = 10
>>> for i in range(1, N + 1):
	print('*'*i)

	
*
**
***
****
*****
******
*******
********
*********
**********
>>> range(1, N + 1)
range(1, 11)
>>> list(range(1, N + 1))
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> for i in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
	print('*')

	
*
*
*
*
*
*
*
*
*
*
>>> '*' * 5
'*****'
>>> for i in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
	print('*' * i)

	
*
**
***
****
*****
******
*******
********
*********
**********
>>> for i in range(N + 1, 1, -1):
	print('*'*i)

	
***********
**********
*********
********
*******
******
*****
****
***
**
>>> for i in range(N, 0, -1):
	print('*'*i)

	
**********
*********
********
*******
******
*****
****
***
**
*
>>> 
 RESTART: C:/Users/Purushotham/Desktop/oracle_july/day_02/examples/01_stars.py 
Traceback (most recent call last):
  File "C:/Users/Purushotham/Desktop/oracle_july/day_02/examples/01_stars.py", line 1, in <module>
    for i in range(1, N + 1):
NameError: name 'N' is not defined
>>> 
 RESTART: C:/Users/Purushotham/Desktop/oracle_july/day_02/examples/01_stars.py 
*
**
***
****
*****
******
*******
********
*********
**********
**********
*********
********
*******
******
*****
****
***
**
*
>>> 
 RESTART: C:/Users/Purushotham/Desktop/oracle_july/day_02/examples/01_stars.py 
Enter a number to create a pattern: 5
*
**
***
****
*****
*****
****
***
**
*
>>> 
 RESTART: C:/Users/Purushotham/Desktop/oracle_july/day_02/examples/01_stars.py 
Enter a number to create a pattern: 3
*
**
***
***
**
*
>>> # ---------------------- break, continue
>>> 
>>> for i in range(100):
	if(i % 7 == 0 and i % 11 == 0):
		print(i)
		break

	
0
>>> for i in range(1, 100):
	if(i % 7 == 0 and i % 11 == 0):
		print(i)
		break

	
77
>>> for i in range(1, 100):
	if(i % 7 == 0):
		continue
	print(i ** 2)

	
1
4
9
16
25
36
64
81
100
121
144
169
225
256
289
324
361
400
484
529
576
625
676
729
841
900
961
1024
1089
1156
1296
1369
1444
1521
1600
1681
1849
1936
2025
2116
2209
2304
2500
2601
2704
2809
2916
3025
3249
3364
3481
3600
3721
3844
4096
4225
4356
4489
4624
4761
5041
5184
5329
5476
5625
5776
6084
6241
6400
6561
6724
6889
7225
7396
7569
7744
7921
8100
8464
8649
8836
9025
9216
9409
9801
>>> for i in range(1, 100):
	if(i % 7 == 0):
		break
	print(i ** 2)

	
1
4
9
16
25
36
>>> # ------------------------- while loop
>>> 
>>> N = 1
>>> while N < 10:
	print(N, N**2)
	N += 1

	
1 1
2 4
3 9
4 16
5 25
6 36
7 49
8 64
9 81
>>> # continue and break can be used in while loop as well
>>> 
>>> # 5 X 1 = 5
>>> print(5, ' X ', 1, ' = ', 5*1)
5  X  1  =  5
>>> print(5, 'X', 1, '=', 5*1)
5 X 1 = 5
>>> print("Hello", "how are you?", sep="---")
Hello---how are you?
>>> print("Hello", "how are you?", sep="")
Hellohow are you?
>>> print(5, 'X', 1, '=', 5*1, sep='')
5X1=5
>>> 
>>> print(str(5) + ' X ' + str(1) + ' = ' + str(5*1))
5 X 1 = 5
>>> 
== RESTART: C:/Users/Purushotham/Desktop/oracle_july/day_02/labs/lab_01.py ==
Enter a number:13
------------------------------
13 X 1 = 13
13 X 2 = 26
13 X 3 = 39
13 X 4 = 52
13 X 5 = 65
13 X 6 = 78
13 X 7 = 91
13 X 8 = 104
13 X 9 = 117
13 X 10 = 130
>>> 
== RESTART: C:/Users/Purushotham/Desktop/oracle_july/day_02/labs/lab_01.py ==
Enter a number:13
------------------------------
Traceback (most recent call last):
  File "C:/Users/Purushotham/Desktop/oracle_july/day_02/labs/lab_01.py", line 26, in <module>
    print(N + ' X ' + str(i) + ' = ' + str(N*i))
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> 
>>> 
>>> 10 + "20"
Traceback (most recent call last):
  File "<pyshell#148>", line 1, in <module>
    10 + "20"
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> "10" + "20" + "30"
'102030'
>>> 
