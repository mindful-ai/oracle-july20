N = int(input('Enter a number to create a pattern: '))

for i in range(1, N + 1):
	print('*'*i)
for i in range(N, 0, -1):
	print('*'*i)
