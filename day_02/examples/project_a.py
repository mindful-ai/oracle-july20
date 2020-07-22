# Project A
# Extract all the prime numbers between the user given range

import primes2

# inputs

start = int(input('Enter a start point: '))
end = int(input('Enter a end point: '))

# process

primes = []
for n in range(start, end + 1):
    if(primes2.checkprime(n)):
        primes.append(n)


'''
# ------------------- Deeptiman


for n in range(start, end + 1):
    for i in range(2, n):
        if( n % i == 0):
            break
    primes.append(n)
'''

# output

print('-'*40)
print('PRIMES: ')
print(primes)
        
