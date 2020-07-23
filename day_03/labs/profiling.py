# Objective:
# How much time does it take to create 1000 random numbers
# between the range 1, 100

# import all the modules required
from datetime import datetime
import random


# Crete an empty list
L = []

# timestamp
t1 = datetime.now()

# Loop for 1000 times
# Each time produce a random number and store in the list
'''
for i in range(1000):
    L.append(random.randint(1, 100))

for i in range(1000):
    n = random.randint(1, 100)
    L.append(n)

i = 0
while i < 1000:
    L.append(random.randint(1, 100))
    i += 1
'''
i = 0
while i < 1000:
    n = random.randint(1, 100)
    L.append(n)
    i += 1

# timestamp
t2 = datetime.now()

# Print the difference in time
print("The process took ", t2-t1)
