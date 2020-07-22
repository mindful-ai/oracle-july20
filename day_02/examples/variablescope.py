# Scope of variables

coeff = 1.0

def apply(params):
    data = []
    for elem in params:
        data.append(coeff * elem)
    return data

def apply2(params):
    coeff = 0.8
    data = []
    for elem in params:
        data.append(coeff * elem)
    return data

def apply3(params):
    global coeff
    data = []
    for elem in params:
        data.append(coeff * elem)
    return data

def apply4(params):
    coeff = 0.8
    
    def change(p):
        #coeff = 0.6
        nonlocal coeff
        #global coeff
        data = []
        for elem in p:
            data.append(coeff * elem)
        return data
    
    return change(params)
        

# ------------------------------------

res = apply4([100, 200, 300, 400])

print('RESULT: ', res)
