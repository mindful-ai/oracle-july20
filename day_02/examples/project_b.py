# Project B
# Input several values from the user, 
# Find the following parameters:
# Max, Min, Average, Median, Number of prime numbers


import numpy as np
from primes2 import checkprime

# inputs

data = []

while True:
    d = input('(q to quit)--> ')
    if(d.lower() == 'q'):
        break
    if(d.isdigit()):
        data.append(int(d))

# print('-' * 60)
# print(data)


# process

maximum = max(data)
minimum = min(data)
average = sum(data) / len(data)
median  = np.median(data)

primes = []
for item in data:
    if(checkprime(item)):
        primes.append(item)

nprimes  = len(primes)

# Output

print('-'*80)
print('MAXIMUM   : ', maximum)
print('MINIMUM   : ', minimum)
print('AVERAGE   : ', average)
print('MEDIAN    : ', median)
print('PRIMES    : ', nprimes)
print('-'*80)




        
