# input

L = ['mango', 'grapes', 'banana', 'apple']

# process

'''
new = ['cherries', 'gauva', 'melon']
L.extend(new)
L.remove('grapes')
L.sort()
'''

L = ['mango', 'grapes', 'banana', 'apple']


L.extend(L1)

print(L)


# output

#print(L)
# ['apple', 'banana', 'cherries', 'gauva', 'mango', 'melon']