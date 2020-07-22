# Keyword and Default parameters
# RULE: write default arguments after the non-default arguments

def apply( params, coeff = 0.5 ):
    '''
      Documentation space
    '''
    data = []
    for elem in params:
        data.append(coeff * elem)
    return data

# ------------------------------------

res = apply([100, 200, 300, 400])
res2 = apply(coeff = 0.97, params = [1, 2, 3, 4])

print('RESULT: ', res2)
