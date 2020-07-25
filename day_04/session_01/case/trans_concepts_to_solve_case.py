Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> cols = "name,age,regid,phy,chem,math,bio,avg,rank"
>>> stud = "Vijay,14,HPE001,99,98,97,96,0,0"
>>> 
>>> cols = cols.split(',')
>>> cols
['name', 'age', 'regid', 'phy', 'chem', 'math', 'bio', 'avg', 'rank']
>>> stud = stud.split(',')
>>> dict(zip(cols, stud))
{'name': 'Vijay', 'age': '14', 'regid': 'HPE001', 'phy': '99', 'chem': '98', 'math': '97', 'bio': '96', 'avg': '0', 'rank': '0'}
>>> cd = {}
>>> sd = dict(zip(cols, stud))
>>> cd.setdefault(sd['regid'], sd)
{'name': 'Vijay', 'age': '14', 'regid': 'HPE001', 'phy': '99', 'chem': '98', 'math': '97', 'bio': '96', 'avg': '0', 'rank': '0'}
>>> cd
{'HPE001': {'name': 'Vijay', 'age': '14', 'regid': 'HPE001', 'phy': '99', 'chem': '98', 'math': '97', 'bio': '96', 'avg': '0', 'rank': '0'}}
>>> 
>>> 
>>> 
>>> # ------------- COMPREHENSION
>>> 
>>> # C = [<expr> <loop> <condition>]
>>> 
>>> 
>>> L = ['red', 'blue', 'green']
>>> L1 = []
>>> for s in L:
	L1.append(s.capitalize())

	
>>> L1
['Red', 'Blue', 'Green']
>>> LC = [s.capitalize() for s in L]
>>> LC
['Red', 'Blue', 'Green']
>>> 
>>> L = list(range(11, 99))
>>> 
>>> L
[11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98]
>>> L.insert(0, 10)
>>> L
[10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98]
>>> L.append(99)
>>> L
[10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]
>>> 
>>> L7 = [x for x in L if x % 7 == 0]
>>> L7
[14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98]
>>> T7 = (x**2 for x in L if x % 7 == 0)
>>> T7
<generator object <genexpr> at 0x0000027763597A20>
>>> list(T7)
[196, 441, 784, 1225, 1764, 2401, 3136, 3969, 4900, 5929, 7056, 8281, 9604]
>>> 
>>> L = ['red', 'blue', 'green']
>>> D = {s:{'len':len(s), 'hist':Counter(s)} for s in L}
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    D = {s:{'len':len(s), 'hist':Counter(s)} for s in L}
  File "<pyshell#43>", line 1, in <dictcomp>
    D = {s:{'len':len(s), 'hist':Counter(s)} for s in L}
NameError: name 'Counter' is not defined
>>> from collections import Counter
>>> D = {s:{'len':len(s), 'hist':Counter(s)} for s in L}
>>> D
{'red': {'len': 3, 'hist': Counter({'r': 1, 'e': 1, 'd': 1})}, 'blue': {'len': 4, 'hist': Counter({'b': 1, 'l': 1, 'u': 1, 'e': 1})}, 'green': {'len': 5, 'hist': Counter({'e': 2, 'g': 1, 'r': 1, 'n': 1})}}
>>> 
