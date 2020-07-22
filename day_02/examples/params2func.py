# Passing different parameters into a function

def apply(coeff, params):
    '''
      Documentation space
    '''
    data = []
    for elem in params:
        data.append(coeff * elem)
    return data

# ------------------------------------

res = apply(0.7, [100, 200, 300, 400])

print('RESULT: ', res)
        
