Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> s='missimadam'
s[s.find('isssi'):len('issi')]
s[s.find('issi'):len('issi')]

SyntaxError: multiple statements found while compiling a single statement
>>> 
>>> s= 'missimadam'
>>> s.find('isssi')
-1
>>> s.find('issi')
1
>>> len('issi')
4
>>> x = s.find('issi')  # start of 'issi'
>>> y = x + len('issi')
>>> s[x:y]
'issi'
>>> s[1:5]
'issi'
>>> 
