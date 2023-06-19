'''#1. Write a program to generate all 5 divisibles from 10 to 50?
i=10
while i<51:
    if i%5==0:
        print('{} is divisible by 5'.format(i))
    i=i+1
    #or
for i in range(10,51):
    if i%5==0:
        print('{} is divisible by 5'.format(i))
#2. Write a program to generate all 10 divisibles from 100 to 10?
for i in range(100,10,-1):
    if i%10==0:
        print('{} is divisible by 10'.format(i))
# 3. Write a program to generate all odd numbers from 11 to 25?
for i in range(11,25):
    if i%2!=0:
         print('{} is odd number'.format(i))
#4. Write a program to generate all even numbers from -2 to -22?
for i in range(-2,-23,-1):
    if i%2==0:
        print('{} is even number'.format(i))
#5. Write a program to generate all numbers from -3 to 5?
for i in range(-3,5):
    print('{} is number'.format(i))
#6. Write a program to generate all 7 divisibles from -21 to 21?
for i in range(-21,22):
    if i%7==0:
         print('{} is number divisible by 7'.format(i))
#7.write a program to print numbers 1 to 11 except 2 and 6?
for i in range(1,11):
    if i==2:
        continue
    elif i==6:
        continue
    print('{} is a number'.format(i))
#8. Write a program to generate all numbers from 15 to 1 except 3,6,9 and 12?
for i in range(15,0,-1):
    if i%3==0:
        continue
    print('{} is a number'.format(i))
#9. Write a program to generate all numbers from -2 to 2 except -1 and 1?
for i in range(-2,2,1):
    if i==-1:
        continue
    elif i==1:
        continue
    print('{} is a number'.format(i))
   
#10. Write a program to generate all 3 divisibles from 15 to -15 except even numbers?
for i in range(15,-15,-1):
    if i%3==0:
        continue
    print('{} is a number'.format(i))
#1
i=10
while i<51:
    if i%5==0:
        print('{} is divisible by 5'.format(i))
    i=i+1
#2
i=100
while i<101 and i>9:
    if i%10==0:
        print('{} is divisible by 10'.format(i))
    i=i-1
#3
i=11
while i<26:
    if i%2!=0:
        print('{} is odd number'.format(i))
    i=i+1
#4
i=-2
while i>-23:
    if i%2==0:
         print('{} is even number'.format(i))
    i=i-1
#5
i=-3
while i<6:
    print('{} is a number'.format(i))
    i=i+1
#6
i=-21
while i<22:
    if i%7==0:
        print("{} is divisible by 7".format(i))
    i=i+1
#7
i=1
while i<11:
    if i!=2 and i!=6:
        print(i)
    i=i+1
#8
i=15
while i<16 and i>=1:
    if i%3!=0:
        print(i)
    i=i-1
#9
i=-2
while i<2:
    if i!=-1 and i!=1:
        print(i)
    i=i+1
#10
i=-15
while i<15:
    if i%3!=0:
        print(i)
    i=i+1'''








    
     
    
    
    
   
    
