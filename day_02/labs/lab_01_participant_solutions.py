From Suvarchala Alamur to Everyone:  11:43 AM
Hi Purushotam

N=(1,2,3,4,5,6,7,8,9,10)
for i in N:
    print(5, "X", i, "=", 5*i)

o/p for the above code came as
5 X 1 = 55 X 2 = 105 X 3 = 155 X 4 = 205 X 5 = 255 X 6 = 305 X 7 = 355 X 8 = 405 X 9 = 455 X 10 = 50


From Saumya Tripathi to Me:  (Privately) 11:45 AM
#Input
c = input('Enter a number:')
#Process
int_c = int(c)
range_list = list(range(10))
#Output
for i in range_list:
    print(c,' X ', i+1,' = ', int_c*(i+1))


From mukeskuk to Everyone:  11:47 AM
#input
num = int(input("Enter number for table:"))
i = 0
#process
while i < 10:
    i=i+1
    print(num,"* " ,i, "=", num*i)


From Deeptiman Rath to Everyone:  11:47 AM
>>> x=range(1,11)
>>> y=5
>>>for N in x:
        print(y ,'*',N,'=',N*y)

5 * 1 = 5
5 * 2 = 10
5 * 3 = 15
5 * 4 = 20
5 * 5 = 25
5 * 6 = 30
5 * 7 = 35
5 * 8 = 40
5 * 9 = 45
5 * 10 = 50


From Anjani Verma to Everyone:  11:48 AM
x = int(input('Enter the number for Table: '))
for i in range(1,11,1):
    print(x, ' X ',i, ' = ' ,x*i)output:


From Munirathna G to Me:  (Privately) 11:48 AM
num = (int(input("Please enter number ")))
N=10
for i in range(1, N+1):
    print(num, "X", i ,"=", (num*i) )

From Anjani Verma to Everyone:  11:48 AM
Enter the number for Table: 55  X  1  =  55  X  2  =  105  X  3  =  155  X  4  =  205  X  5  =  255  X  6  =  305  X  7  =  355  X  8  =  405  X  9  =  455  X  10  =  50

From Biswanath Mahapatra to Everyone:  11:49 AM
N=5
for i in range(1,11):
    print(N,"X",i,"=",N*i)

From Ritesh Srivastava to Me:  (Privately) 11:51 AM
N = int(input('Enter the number for Table: '))
x = 1
while x < 11:
    multi = N * x
    print(N, 'X', x, '=', multi)
    x += 1

From Arpita Sengupta to Me:  (Privately) 11:53 AM
N=int(input("Enter user number: "))
for i in range(1,11):
    print(N,"X",i,'=', N*i)

From Munirathna G to Me:  (Privately) 11:56 AM
Hi Purushotham, I have a doubt
When I print this
x = range(1, 10)
print(type(x))
Output is <class 'range’>
So when we say for i in range(1, 10):
print(i)In the above code,
for loop is accepting data which is of type range,
which means we can datatype of iterator can be range
just like list or stringIs my understanding right
or is for loop converting this "range(1, 10)” to a list internally

From Anjani Verma to Everyone:  11:59 AM
code for diamond
line =3
k = 2 * line - 2
for i in range(0, line):
    for j in range(0, k):
        print(end=" ")
    k = k - 1
    for j in range(0, i + 1):
        print("* ", end="")
    print("")
    k = line - 2
for i in range(line, -1, -1):
    for j in range(k, 0, -1):
        print(end=" ")
    k = k + 1
    for j in range(0, i + 1):
        print("* ", end="")
    print("")

From Ritesh Srivastava to Me:  (Privately) 12:02 PM
With for loop:
N = int(input('Enter the number for Table: '))
x = 11
for x in range(1, x):
    multi = N * x
    print(N, 'X', x, '=', multi)
    x += 1

From Kaushik Rout to Everyone:  12:03 PM
# Program to display the multiplication table
# Output Sample'''5 x 1 = 55 x 2 = 10...5 x 10 = 50'''
# Input
N = int(input('Enter the number : '))
# Process
for i in range(1, 10+1):
    product = N*i
    #print (N + 'x '+ i + '= ' + product)
    print (N, 'x', i, '=', product)

# Output
