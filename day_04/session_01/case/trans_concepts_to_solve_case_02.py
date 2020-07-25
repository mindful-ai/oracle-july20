Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> D = {'name': 'Ankita', 'age': '14', 'regid': 'INF007', 'phy': '99', 'chem': '99', 'math': '99', 'bio': '99', 'avg': 99.0, 'rank': 2}
>>> D
{'name': 'Ankita', 'age': '14', 'regid': 'INF007', 'phy': '99', 'chem': '99', 'math': '99', 'bio': '99', 'avg': 99.0, 'rank': 2}
>>> D.items()
dict_items([('name', 'Ankita'), ('age', '14'), ('regid', 'INF007'), ('phy', '99'), ('chem', '99'), ('math', '99'), ('bio', '99'), ('avg', 99.0), ('rank', 2)])
>>> list(zip(*D.items()))
[('name', 'age', 'regid', 'phy', 'chem', 'math', 'bio', 'avg', 'rank'), ('Ankita', '14', 'INF007', '99', '99', '99', '99', 99.0, 2)]
>>> r = list(zip(*D.items()))[1]
>>> r
('Ankita', '14', 'INF007', '99', '99', '99', '99', 99.0, 2)
>>> ','.join(r)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    ','.join(r)
TypeError: sequence item 7: expected str instance, float found
>>> ','.join([str(s) for s in r])
'Ankita,14,INF007,99,99,99,99,99.0,2'
>>> [str(s) for s in r]
['Ankita', '14', 'INF007', '99', '99', '99', '99', '99.0', '2']
>>> 
>>> 
>>> 
>>> # ---------------------------------------------------------
>>> 
>>> 
>>> # String format() function
>>> 
>>> name = 'Ram'
>>> age = 35
>>> print('My name is ', name, ' age is ', age)
My name is  Ram  age is  35
>>> print('My name is ' + str(name) + ' age is ' + str(age))
My name is Ram age is 35
>>> print('My name is %s and age is %d' % (name, age))
My name is Ram and age is 35
>>> print('My name is {} and age is {}'.format(name, age))
My name is Ram and age is 35
>>> print('My name is {0} and age is {1}'.format(name, age))
My name is Ram and age is 35
>>> print('My name is {0:10} and age is {1:5}'.format(name, age))
My name is Ram        and age is    35
>>> print('My name is {0:>10} and age is {1:<5}'.format(name, age))
My name is        Ram and age is 35   
>>> print('My name is {0:^10} and age is {1:^5}'.format(name, age))
My name is    Ram     and age is  35  
>>> print('My name is {0:>10} and age is {1:<5}'.format(name, age))
My name is        Ram and age is 35   
>>> print('My name is {n:10} and age is {a:5}'.format(n=name, a=age))
My name is Ram        and age is    35
>>> D = {'raj':35, 'ram':36, 'ravi': 37 }
>>> template = 'My name is {n:10} and age is {a:5}'
>>> for k,v in D.items():
	print(template.format(n=k, a=v))

	
My name is raj        and age is    35
My name is ram        and age is    36
My name is ravi       and age is    37
>>> 
