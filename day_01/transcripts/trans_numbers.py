Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> print('Hello Oracle!')
Hello Oracle!
>>> a = 5
>>> b = 10
>>> print(a)
5
>>> print(b)
10
>>> print(a, b)
5 10
>>> print(a + b)
15
>>> a
5
>>> b
10
>>> a + b
15
>>> # --------------------- NUMBERS
>>> 
>>> type(a)
<class 'int'>
>>> type(b)
<class 'int'>
>>> a = "Oracle"
>>> type(a)
<class 'str'>
>>> c = "python"
>>> type(c)
<class 'str'>
>>> c = [1,2,3,4]
>>> type(c)
<class 'list'>
>>> 
>>> del a
>>> print(a)
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    print(a)
NameError: name 'a' is not defined
>>> 
>>> 
>>> # ----------------------------------------------
>>> 
>>> a = 100
>>> b = 25
>>> type(a)
<class 'int'>
>>> type(b)
<class 'int'>
>>> 
>>> # OPERATORS
>>> # Arithmetic, relational, logical
>>> 
>>> c = a + b
>>> print(c)
125
>>> a + b
125
>>> # ------ Arithmetic Operators
>>> 
>>> a + b
125
>>> a - b
75
>>> a * b
2500
>>> a / b
4.0
>>> x = a + b
>>> y = a / b
>>> type(x)
<class 'int'>
>>> type(y)
<class 'float'>
>>> 
>>> a % b   # modulus
0
>>> 5 % 3
2
>>> 5 // 3
1
>>> # / -> full division, // -> quotient, % -> reminder
>>> 
>>> 3 / 2
1.5
>>> 5 / 3
1.6666666666666667
>>> 
>>> 5 ** 2
25
>>> x = a + b
>>> y = x ** 2
>>> y
15625
>>> 
>>> # ----------------- Relational Operators
>>> 
>>> a
100
>>> b
25
>>> a > b # Is a greater than b?
True
>>> a < b
False
>>> a >= b
True
>>> a <= b
False
>>> a == b
False
>>> a != b
True
>>> a == b * (2 ** 2)
True
>>> 
>>> # ------- Logical operators
>>> 
>>> # and, or, not
>>> 
>>> a > b and a < 200
True
>>> a > b and a > 200
False
>>> a > b or a > 200
True
>>> not(a > b or a > 200)
False
>>> 
>>> m = 123
>>> n = "123"
>>> type(m)
<class 'int'>
>>> type(n)
<class 'str'>
>>> m > n
Traceback (most recent call last):
  File "<pyshell#87>", line 1, in <module>
    m > n
TypeError: '>' not supported between instances of 'int' and 'str'
>>> str(m) > n
False
>>> m > int(n)
False
>>> 
>>> m = 213
>>> n = "Oracle"
>>> m > n
Traceback (most recent call last):
  File "<pyshell#93>", line 1, in <module>
    m > n
TypeError: '>' not supported between instances of 'int' and 'str'
>>> str(m) >
SyntaxError: invalid syntax
>>> str(m) > n
False
>>> m > int(n)
Traceback (most recent call last):
  File "<pyshell#96>", line 1, in <module>
    m > int(n)
ValueError: invalid literal for int() with base 10: 'Oracle'
>>> 
>>> 
>>> # -------------------------------------------------------
>>> # --------------- In-built Functions
>>> 
>>> # --------------- Arpita
>>> 
>>> 10 + 20
30
>>> "10" + "20"
'1020'
>>> 10 + "20"
Traceback (most recent call last):
  File "<pyshell#106>", line 1, in <module>
    10 + "20"
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> # ----------------------
>>> 
>>> # abs(), bin(), hex(), float(), int()
>>> 
>>> x = 10 - 34
>>> x
-24
>>> x = 34 - 10
>>> x
24
>>> abs(10 - 34)
24
>>> abs(34 - 10)
24
>>> bin(15)
'0b1111'
>>> hex(15)
'0xf'
>>> oct(15)
'0o17'
>>> 
>>> a = "123"
>>> a + 10
Traceback (most recent call last):
  File "<pyshell#122>", line 1, in <module>
    a + 10
TypeError: can only concatenate str (not "int") to str
>>> int(a) + 10
133
>>> float(a) + 10
133.0
>>> 
>>> 
>>> # -------------------------------- In - Built Modules
>>> 
>>> 
>>> sin(90)
Traceback (most recent call last):
  File "<pyshell#130>", line 1, in <module>
    sin(90)
NameError: name 'sin' is not defined
>>> 
>>> import math
>>> math.sin(90)
0.8939966636005579
>>> math.sin(90 * 3.14/180)
0.9999996829318346
>>> math.sin(90 * 3.14159/180)
0.9999999999991198
>>> math.sin(90 * math.pi/180)
1.0
>>> math.sin(90 * math.radians(90))
1.9581969173625882e-15
>>> math.sin(math.radians(90))
1.0
>>> 
>>> import random
>>> random.randint(1, 100)
47
>>> random.randint(1, 100)
71
>>> random.randint(1, 100)
26
>>> random.randint(1, 100)
8
>>> random.randint(1, 100)
70
>>> random.randint(1, 100)
84
>>> random.randint(1, 100)
36
>>> 
== RESTART: C:/Users/Purushotham/Desktop/oracle_july/day_01/labs/lab_01.py ==
144
>>> 
== RESTART: C:/Users/Purushotham/Desktop/oracle_july/day_01/labs/lab_01.py ==
144
>>> 
== RESTART: C:/Users/Purushotham/Desktop/oracle_july/day_01/labs/lab_01.py ==
136
>>> 
== RESTART: C:/Users/Purushotham/Desktop/oracle_july/day_01/labs/lab_01.py ==
144
>>> 
