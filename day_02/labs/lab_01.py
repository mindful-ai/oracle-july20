# Program to display the multiplication table

# Output sample

'''

5 X 1 = 5
5 X 2 = 10
5 X 3 = 15
.
.
.
5 X 10 = 50

'''

# Input
N = int(input('Enter a number:' ))

# Process

# Output

print('-'*30)
for i in range(1, 11):
    print(str(N) + ' X ' + str(i) + ' = ' + str(N*i))

