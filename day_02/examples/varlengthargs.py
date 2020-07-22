# Variable length arguments
# All required arguments should be supplied first
# Followed by *targs -> Tuple Arguments
# Followed by **kargs -> Keyword Arguments

def func(a, b, c, *targs, **kargs):
    print(a)
    print(b)
    print(c)
    print(targs)
    print(kargs)


func(1, 2, 3)
print('-'*30)
func(1, 2, 3, 4, 5, 6)
print('-'*30)

#func(1, 2)
#print('-'*30)

func(1, 2, 3, 4, 5, 6, name='anil', age=35, country='India')

func(1, 2, 3, 4, 5, d1={'name':'anil', 'age':35, 'country':'India'},  d2={'name':'sunil', 'age':35, 'country':'India'})
print('-'*30)
