'''a=[]
b=[]
x=[a.append(i)if i%2==0 else b.append(i)for i in range(100)]
print(a)
print(b)'''
'''for i in range(100):
    if i%2==0:
        pass
    elif i%3==0 and 0>i>9:
        pass
    elif i%5==0 and 0>i<9:
        pass
    elif i%4==0:
        pass
    else:
        print(i)'''
'''num=int(input('enter a number:'))
for i in range(2,num):
    count=0
    for j in range(2,(i//2)+1):
        if i%j==0:
            count=count+1
    if count==0 and i!=1:
        print(i)'''
'''#1 Write a Python Code to Check if a Number is Odd or Even.
num=int(input('Enter your number:'))
if num%2==0:
    print('{} is even'.format(num))
else:
    print('{} is odd'.format(num))'''
'''#2 Write a Python code to find the maximum of two numbers.
num=int(input('Enter your number:'))
num1=int(input('enter your number:'))
if num>num1:
    print('{} is maximum'.format(num))
else:
    print('{} is maximum'.format(num1))'''
'''#3 Write a Python code to check prime numbers.
num=int(input('enter your number:'))
c=0
for i in range(2,(num//2)+1):
    if num%i==0:
        c=c+1
if c==0:
    print('{} is prime number'.format(num))
else:
    print('{} is not a prime number'.format(num))'''
'''#4 Write a Python factorial program without using if-else, for, and ternary operators.
num=int(input('enter your number:'))
c=1
for j in range(1,num+1):
    c=c*j
print(c)'''
'''#5 Write a Python code to calculate the square root of a given number.
num=int(input('entr your number:'))
print('{} square root is'.format(num),num**2)'''
'''#6 Write a Python code to calculate the area of a triangle.
b=float(input('enter your breadth:'))
h=float(input('enter your height:'))
print('area of the triangle is',1/2*b*h)'''
'''#7 Write a Python code to check the armstrong number.
num=int(input('enter your number:'))
c=0
temp=num
while temp>0:
    j=temp%10
    c=c+j**3
    temp=temp//10
if c==num:
    print('{} is a armstrong number'.format(num))
else:
    print('{} is not a armstrong number'.format(num))'''
'''#8 Write a Python code to display a multiplication table using for loop.
num=int(input('enter your number:'))
for i in range(num,num+1):
    for j in range(1,21):
        print('{}*{} ='.format(i,j),i*j)'''
'''#9 Write a Python code to swap two variables.
a=10
b=20
c=a
a=b
b=c
print(a)
print(b)'''
'''#10 wap to print factorial in number?
import math
num=int(input('enter your number:'))
print(math.factorial(num))'''
'''#11 write a python program to check given year is leap year or not?
num=int(input('enter your year:'))
if num%100!=0:
    if num%4==0:
        print('{} year is a leap year'.format(num))
else:
    print('{} year is not a leap year'.format(num))'''
#12) Write a Python program to check if a given number is a Fibonacci number or not.
'''lst=[0,1]
l=lst
num=int(input('enter your number:'))
for i in range(num):
    if i>1:
        k=l[-1]+l[-2]
        l.append(k)
print(l)
if num in l:
    print('{} is fibonacci series number'.format(num))
else:
    print('{} is not a fibonacci series number'.format(num))'''
'''#13) Write a Python program to find the area of a circle.
import math
radius=float(input('enter your radius:'))
print('area of the circle is',math.pi*radius*radius)'''
'''#14) Write a Python program to display the calendar.
import calendar
year=int(input('enter your year:'))
month=int(input('enter your month:'))
print(calendar.month(year,month))
import calendar
year=int(input('enter your year:'))
print(calendar.calendar(year))'''
'''#15) Write a Python program to print all prime numbers in an interval.
num=int(input('enter your number:'))
num1=int(input('enter your number:'))
for i in range(num,num1):
    c=0
    for j in range(2,(i//2)+1):
        if i%j==0:
            c=c+1
    if c==0 and i!=1:
        print(i)'''
'''#16) Write a Python Program to Find Vowels From a String.
a=input('enter your string:')
print([i for i in a if i in'aeiou'])'''
'''#17 Write a Python Program to Convert Comma Separated List to a String.
lst=['koti','kotesh','kotes']
print(','.join(lst))'''
'''def outer_function():
    num = 20

    def inner_function():
        num = 30
        print('num =', num)

    inner_function()
    print('num =', num)


num = 10
outer_function()
print('num =', num)
num=30
num=20
num=10'''








       




