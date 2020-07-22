Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # DICTIONARIES
>>> 
>>> D = { 'name':'anil', 'age': 35, 'salary': '150000$' }
>>> type(D)
<class 'dict'>
>>> 
>>> 
>>> D['name']
'anil'
>>> D['age']
35
>>> D['salary']
'150000$'
>>> D['company']
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    D['company']
KeyError: 'company'
>>> D['company'] = 'Oracle'
>>> D
{'name': 'anil', 'age': 35, 'salary': '150000$', 'company': 'Oracle'}
>>> D['name'] = 'Sunil'
>>> D
{'name': 'Sunil', 'age': 35, 'salary': '150000$', 'company': 'Oracle'}
>>> D.pop('age')
35
>>> D
{'name': 'Sunil', 'salary': '150000$', 'company': 'Oracle'}
>>> 
>>> 
>>> D.setdefault('age', 36)
36
>>> D
{'name': 'Sunil', 'salary': '150000$', 'company': 'Oracle', 'age': 36}
>>> 
>>> 'name' in D
True
>>> 
>>> # --------------------- functions
>>> 
>>> D.keys()
dict_keys(['name', 'salary', 'company', 'age'])
>>> D.value()
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    D.value()
AttributeError: 'dict' object has no attribute 'value'
>>> D.values()
dict_values(['Sunil', '150000$', 'Oracle', 36])
>>> D.items()
dict_items([('name', 'Sunil'), ('salary', '150000$'), ('company', 'Oracle'), ('age', 36)])
>>> 'Oracle' in D.values()
True
>>> 'Infosys' in D.values()
False
>>> 
>>> 
>>> D
{'name': 'Sunil', 'salary': '150000$', 'company': 'Oracle', 'age': 36}
>>> D.setdefault('name')
'Sunil'
>>> D
{'name': 'Sunil', 'salary': '150000$', 'company': 'Oracle', 'age': 36}
>>> D.setdefault('name', 'Anil')
'Sunil'
>>> D
{'name': 'Sunil', 'salary': '150000$', 'company': 'Oracle', 'age': 36}
>>> D['name'] = 'Anil'
>>> D
{'name': 'Anil', 'salary': '150000$', 'company': 'Oracle', 'age': 36}
>>> 
>>> 
>>> # --------------------------- operators
>>> 
>>> D1 = {'addr':'Bengaluru', 'phone':'+917865636528' }
>>> D
{'name': 'Anil', 'salary': '150000$', 'company': 'Oracle', 'age': 36}
>>> D + D1
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    D + D1
TypeError: unsupported operand type(s) for +: 'dict' and 'dict'
>>> D.update(D1)
>>> D
{'name': 'Anil', 'salary': '150000$', 'company': 'Oracle', 'age': 36, 'addr': 'Bengaluru', 'phone': '+917865636528'}
>>> 
>>> del d['age']
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    del d['age']
NameError: name 'd' is not defined
>>> del D['age']
>>> D
{'name': 'Anil', 'salary': '150000$', 'company': 'Oracle', 'addr': 'Bengaluru', 'phone': '+917865636528'}
>>> len(D)
5
>>> 'name' in D
True
>>> 
