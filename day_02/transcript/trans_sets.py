Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # SET
>>> s = 'mississippi'
>>> L = list(s)
>>> L
['m', 'i', 's', 's', 'i', 's', 's', 'i', 'p', 'p', 'i']
>>> S = set(s)
>>> S
{'m', 's', 'i', 'p'}
>>> s1 = set('abcdefg')
>>> s1
{'a', 'b', 'f', 'g', 'e', 'd', 'c'}
>>> 'f' in s1
True
>>> 'r' in s1
False
>>> 
>>> # --------------------- operators to work on a set
>>> 
>>> s1
{'a', 'b', 'f', 'g', 'e', 'd', 'c'}
>>> s2 = { 'd', 'e', 'f', 'g', 'h', 'i', 'j' }
>>> s2
{'h', 'j', 'i', 'f', 'g', 'e', 'd'}
>>> 
>>> s1 & s2
{'d', 'f', 'g', 'e'}
>>> # intersection of sets
>>> 
>>> s1 | s2
{'h', 'j', 'a', 'i', 'b', 'f', 'g', 'e', 'd', 'c'}
>>> # Union of sets
>>> 
>>> s1 ^ s2
{'j', 'a', 'i', 'h', 'b', 'c'}
>>> # Exclusive elements
>>> 
>>> # -------------------------------- functions
>>> 
>>> s1
{'a', 'b', 'f', 'g', 'e', 'd', 'c'}
>>> s1.add('x')
>>> s1
{'x', 'a', 'b', 'f', 'g', 'e', 'd', 'c'}
>>> s3 = {'y', 'z'}
>>> s1.update(s3)
>>> s1
{'x', 'a', 'y', 'b', 'f', 'g', 'e', 'd', 'z', 'c'}
>>> s1.remove('x')
>>> s1
{'a', 'y', 'b', 'f', 'g', 'e', 'd', 'z', 'c'}
>>> 
>>> 
>>> s1.intersection(s2)
{'d', 'f', 'g', 'e'}
>>> s1.union(s2)
{'h', 'j', 'y', 'a', 'i', 'b', 'f', 'g', 'e', 'd', 'z', 'c'}
>>> 
>>> 
>>> # -------------------------------- interconversion
>>> 
>>> s4 = s1 | s2
>>> s4
{'h', 'j', 'y', 'a', 'i', 'b', 'f', 'g', 'e', 'd', 'z', 'c'}
>>> 
>>> L4 = list(s4)
>>> L4
['h', 'j', 'y', 'a', 'i', 'b', 'f', 'g', 'e', 'd', 'z', 'c']
>>> L4.sort()
>>> L4
['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'y', 'z']
>>> 
>>> str(L4)
"['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'y', 'z']"
>>> ''.join(L4)
'abcdefghijyz'
>>> 
