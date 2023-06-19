#no condition
print([i for i in range(11)])

# one if condition
print([i for i in range(11) if i%2==0])
# if else condition
print([i if i%2==0 else 'odd' for i in range(11)])
# elif statements
print([i if i%2==0 or i%3==0 else 'not divisible 2 and 3' for i in range(11)])
# prime numbers
n=int(input('enter your number:'))
for x in range(n):
      for i in (2,n):
         if x%2==0:
            print(x,'not a prime number')
            break
      else:
            print(x,'is prime number')
# at a time you seperate even odd numbers
n=int(input('enter your number:'))
odd=[]
even=[]
for i in range(n):
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
print(even,'even numbers')
print(odd,'odd numbers')



