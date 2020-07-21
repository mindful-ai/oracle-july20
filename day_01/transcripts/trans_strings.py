Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # STRING
>>> s = "python"
>>> type(s)
<class 'str'>
>>> 
>>> # Sub-scripting
>>> # [index]
>>> # [start:end]
>>> # [start:end:interval]
>>> s[0]
'p'
>>> s[1]
'y'
>>> s[2]
't'
>>> s[-1]
'n'
>>> s[-2]
'o'
>>> s[-3]
'h'
>>> s[1:3]
'yt'
>>> s[2:5]
'tho'
>>> s[1:4]
'yth'
>>> s[-5:-2]
'yth'
>>> s[1:5]
'ytho'
>>> s[1:5:2]
'yh'
>>> s1 = 'computer'
>>> s1[1:8]
'omputer'
>>> s1[0:8]
'computer'
>>> s1[0:8:2]
'cmue'
>>> s1[0:8:3]
'cpe'
>>> s1[0:8:1]
'computer'
>>> s[-7:5]
'pytho'
>>> 
>>> s[0:3]
'pyt'
>>> s[:3]
'pyt'
>>> s[4:6]
'on'
>>> s[4:]
'on'
>>> s[:]
'python'
>>> s[::2]
'pto'
>>> s[1::2]
'yhn'
>>> s[::-1]
'nohtyp'
>>> s[2:5:-1]
''
>>> s[2:5]
'tho'
>>> s[2:5][::-1]
'oht'
>>> 
>>> # -------------------------------- Immutable nature of strings
>>> 
>>> s
'python'
>>> s[0]
'p'
>>> s[1]
'y'
>>> s[0] = 'J'
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    s[0] = 'J'
TypeError: 'str' object does not support item assignment
>>> s = 'jython'
>>> s
'jython'
>>> 
>>> # ------------------------------- Operators defined for strings
>>> 
>>> s1 = "every"
>>> s2 = 'thing'
>>> s3 = '''
This is a
multiline
string
'''
>>> s1
'every'
>>> s2
'thing'
>>> s3
'\nThis is a\nmultiline\nstring\n'
>>> type(s1)
<class 'str'>
>>> type(s2)
<class 'str'>
>>> type(s3)
<class 'str'>
>>> 
>>> s1 + s2
'everything'
>>> s4 = s1 + ' '
>>> s4
'every '
>>> s4 * 5
'every every every every every '
>>> len(s1 + s2)
10
>>> s4
'every '
>>> del s4
>>> s4
Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    s4
NameError: name 's4' is not defined
>>> 
>>> # ----------------------- In-built functions to work with strings
>>> 
>>> # Functions related to case
>>> 
>>> s
'jython'
>>> s = "python"
>>> s.upper()
'PYTHON'
>>> s.lower()
'python'
>>> 'HELLO'.lower()
'hello'
>>> s.capitalize()
'Python'
>>> 
>>> # Functions related to checking/querying a string
>>> 
>>> s1 = "123"
>>> s2 = "123A"
>>> s3 = "$%^%$"
>>> s4 = ' '
>>> 
>>> s1.isdigit()
True
>>> t = "23"
>>> f = t * 1.8 + 32
Traceback (most recent call last):
  File "<pyshell#94>", line 1, in <module>
    f = t * 1.8 + 32
TypeError: can't multiply sequence by non-int of type 'float'
>>> f = float(t) * 1.8 + 32
>>> f
73.4
>>> f = float(S2) * 1.8 + 32
Traceback (most recent call last):
  File "<pyshell#97>", line 1, in <module>
    f = float(S2) * 1.8 + 32
NameError: name 'S2' is not defined
>>> f
73.4
>>> if(s1.isdigit()):
	f = float(s1) * 1.8 + 32

	
>>> f
253.4
>>> if(s2.isdigit()):
	f = float(s2) * 1.8 + 32

	
>>> f
253.4
>>> s2.isdigit()
False
>>> f = float(s2[0:-1]) * 1.8 + 32
>>> f
253.4
>>> s2[0:-1]
'123'
>>> s2.isdigit()
False
>>> s2.isalnum()
True
>>> s2.isalpha()
False
>>> 'abcd'.isalpha()
True
>>> 'abcd#'.isalpha()
False
>>> 'abcd#'.isalnum()
False
>>> s4.isspace()
True
>>> 
>>> site = "www.google.com"
>>> site.startswith("http")
False
>>> site.startswith("www")
True
>>> site.endswith("com")
True
>>> 
>>> s4
' '
>>> # ---------------------- Functions for searching
>>> 
>>> s = 'mississippi'
>>> s.find('issi')
1
>>> s.find('app')
-1
>>> x = s.find('ssip')
>>> x
5
>>> s[s.find('ssip'):len('ssip')]
''
>>> s[s.find('ssip'):s.find('ssip') + len('ssip')]
'ssip'
>>> s[5:5+4]
'ssip'
>>> 
>>> s.count('s')
4
>>> s.count('ss')
2
>>> s.find('ss')
2
>>> 
>>> 'issi' in s
True
>>> 
>>> # ------------------------- Functions to modify a string
>>> # Remember: strings are immutable, so when you modify
>>> # the original string is untouched
>>> 
>>> ip = '192-165-3-4'
>>> ip.replace('-', '.')
'192.165.3.4'
>>> ip
'192-165-3-4'
>>> new_ip = ip.replace('-', '.')
>>> new_ip
'192.165.3.4'
>>> ip
'192-165-3-4'
>>> 
>>> 
>>> 
>>> 
>>> 
>>> ip=ip.replace('-','.')  # ---------- Tulja
>>> ip
'192.165.3.4'
>>> 
>>> 
>>> 
>>> s = "twinkle twinkle little star"
>>> s.split()
['twinkle', 'twinkle', 'little', 'star']
>>> s
'twinkle twinkle little star'
>>> L = s.split()
>>> L
['twinkle', 'twinkle', 'little', 'star']
>>> type(L)
<class 'list'>
>>> L = s.split('n')
>>> L
['twi', 'kle twi', 'kle little star']
>>> L
['twi', 'kle twi', 'kle little star']
>>> 'N'.join(L)
'twiNkle twiNkle little star'
>>> 
