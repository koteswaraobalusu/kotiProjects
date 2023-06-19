'''#1 what is difference between local variable and global variable?
#2 what is difference between list and global tuple?
#3 print word which has 4 characters in comprehension?
students = ["Hannah", "Peter", "Luke"]
print([i for i in students if len(i)==4])
#4 swap two numbers?
a=1
b=2
a,b=b,a
print(a,b)
#5 print phclyhclthclhhclohclnhcl by using python word?
st='python'
for i in st:
    print(i+'hcl',end='')
#6 What is a lambda function? Why are they used?
#7 Write a program to reverse an integer in Python.
st='123456789'
print(st[-1::-1])
#8 Write a program in Python to check whether an integer is Armstrong number or not.

num = int(input("Enter a number: "))
sum = 0
temp = num
while temp > 0:
   digit = temp % 10
   sum += digit ** 3
   temp //= 10
if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")
#9 Write a program in Python to check given number is prime or not.
j=0
while j==0:
    num=(int(input('enter your number:')))
    if num>2:
        for i in range(2, int(num/2)+1):
            if num%i==0:
                print('{} is not a prime number'.format(num))
                break
            else:
                print('{} is a prime number'.format(num))
j=j+0
# or
num=(int(input('enter your number:')))
if num==1:
    print('{} is not a prime number'.format(num))
elif num>1:
    for i in range(2,num):
        if num%i==0:
              print('{} is not a prime number'.format(num))
              print(i,"times of",num)
              break
        else:
              print('{} is a prime number'.format(num))
else:
      print('{} is not a prime number'.format(num))
#10 Write a program in Python to print the Fibonacci series using iterative method
def fibbonci(n):
    if n<0:
        print('{} in correct input'.format(n))
    elif n==0:
        return 0
    elif n==1 or n==2:
        return 1
    else:
        return fibbonci(n-1)+fibbonci(n-2)
n=int(input('enter your number:'))
print(fibbonci(9))'''
'''#11 Write a Python factorial program without using if-else, for, and ternary operators.
import math
c=0
num=int(input('enter your number:'))
def factorial(a):
    c=(math.factorial(a))
    print(c)
factorial(num)'''
'''st='naraya'
a=[]
for i in st:
    if i.isupper():
        a.append(i.lower())
    else:
        a.append(i.upper())
print(''.join(a))
b=''.join(sorted(st))
print(b)
st1=list(st)
print(st1)
for i in st1:
    st1.sort(reverse=True)
    st2=''.join(st1)
print(st2)
print(st[-1::-1])
v='PYTHON DEVELOPER'
print(v.replace('PYTHON','ORACLE'))'''
'''num=(int(input('enter your number:')))
if num>2:
    for i in range(2, int(num/2)+1):
        if num%i==0:
            print('{} is  not a prime number'.format(num))
        else:
            print('{} is a prime number'.format(num))'''
'''s='koteswara rao'
print(''.join(sorted(s,reverse=True)))'''
l=[1,2,3,4,5]
print(sorted(l,reverse=True))


    
    
    
        
            

