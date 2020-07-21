Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # TUPLES
>>> 
>>> L = ["red", "green", "blue"]
>>> type(L)
<class 'list'>
>>> T = ("red", "green", "blue")
>>> type(T)
<class 'tuple'>
>>> 
>>> # ------------------- Ordered collection, subscripting
>>> 
>>> T[0]
'red'
>>> T[1]
'green'
>>> T[-1]
'blue'
>>> T[::-1]
('blue', 'green', 'red')
>>> T
('red', 'green', 'blue')
>>> 
>>> # ------------------- immutable nature
>>> 
>>> T[0]
'red'
>>> T[0] = 'orange'
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    T[0] = 'orange'
TypeError: 'tuple' object does not support item assignment
>>> 
>>> # Since the tuple is immutable
>>> # adding, removing, rearranging elements are not permitted
>>> 
>>> sorted(T)
['blue', 'green', 'red']
>>> Y
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    Y
NameError: name 'Y' is not defined
>>> T
('red', 'green', 'blue')
>>> tuple(reversed(T))
('blue', 'green', 'red')
>>> T
('red', 'green', 'blue')
>>> 
>>> # -------------------- search elements
>>> 
>>> 'red' in T
True
>>> T.count('red')
1
>>> T.index('red')
0
>>> 
>>> # -------------------- operators
>>> 
>>> T1 = ('black', 'white')
>>> T + T1
('red', 'green', 'blue', 'black', 'white')
>>> T
('red', 'green', 'blue')
>>> T1
('black', 'white')
>>> T3 = T + T1
>>> T3
('red', 'green', 'blue', 'black', 'white')
>>> 
>>> T * 3
('red', 'green', 'blue', 'red', 'green', 'blue', 'red', 'green', 'blue')
>>> del T[0]
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    del T[0]
TypeError: 'tuple' object doesn't support item deletion
>>> del T1
>>> T1
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    T1
NameError: name 'T1' is not defined
>>> len(T)
3
>>> 
>>> 
>>> # ------------------------ multiple variable assigments
>>> 
>>> T
('red', 'green', 'blue')
>>> r,g,b = T
>>> r
'red'
>>> g
'green'
>>> b
'blue'
>>> r1, g1, b1 = L
>>> r1
'red'
>>> g1
'green'
>>> b1
'blue'
>>> 
>>> 
>>> r,b = T
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    r,b = T
ValueError: too many values to unpack (expected 2)
>>> r,b,*x = T
>>> r
'red'
>>> g
'green'
>>> x
['blue']
>>> T1 = ['white', 'black']
>>> r,g,b = T1
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    r,g,b = T1
ValueError: not enough values to unpack (expected 3, got 2)
>>> T1 = ('white', 'black')
>>> r,g,b = T1
Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    r,g,b = T1
ValueError: not enough values to unpack (expected 3, got 2)
>>> r,b,*x = T
>>> T
('red', 'green', 'blue')
>>> r
'red'
>>> b
'green'
>>> x
['blue']
>>> r,g,b = T1
Traceback (most recent call last):
  File "<pyshell#78>", line 1, in <module>
    r,g,b = T1
ValueError: not enough values to unpack (expected 3, got 2)
>>> r,g,*b = T1
>>> r
'white'
>>> g
'black'
>>> b
[]
>>> # ----------------------------------- interchanging tuple <> lists
>>> 
>>> T
('red', 'green', 'blue')
>>> temp = list(T)
>>> temp
['red', 'green', 'blue']
>>> temp.append('yellow')
>>> temp.insert(2, 'golden')
>>> temp
['red', 'green', 'golden', 'blue', 'yellow']
>>> T = tuple(temp)
>>> T
('red', 'green', 'golden', 'blue', 'yellow')
>>> 
