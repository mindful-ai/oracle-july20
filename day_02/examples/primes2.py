'''
Syntax and usage:
    
def <funtionname>(<inA>, <inB>, <inC>...):
    <Logic>
    return expression/value

capture_variable = functionname(10, 20, 30)
'''

# ----------------------------------------------

def checkprime(n):
    for i in range(2, n):
        if( n % i == 0 ):
            return False
    return True

def printmsg(msg):
    print(msg)
    

# ----------------------------------------------

print("primes2.py __name__ contains ", __name__)

if __name__ == "__main__":
    
    # Input

    x = int(input('Enter a number: '))

    # Output

    if(checkprime(x)): 
        print('The number is prime')
    else:
        print('The number is not prime')
