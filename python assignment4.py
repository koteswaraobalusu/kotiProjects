'''# write a program to check if member is available or not
team=['Kohli','Dhoni','Sachin','Surya']
newlst=[]
for i in team:
    if i in team:
       newlst.append(i)
print(newlst)
'''
'''
student=input('enter course name:')
print(student)
if student=='python':
    print('learning updated skill')
else:
    print('learn python')
'''
'''
a=int(input('enter a number:'))
if a%10==0:
    print('{} is divisible by 10'.format(a))
else:
    print('{} is not divisible by 10'.format(a))
    '''
'''
b=eval(input('enter values:'))
print(type(b))
'''
'''
lst=['monday','tuesday','wednesday','thursday']
day=input('enter a day:').lower()
if day in lst:
    print('{}you can wear school uniform'.format(day))
elif day=='friday':
        print('{}you can wear white and white'.format(day))
elif day=='saturday':
              print("{} it's your choice".format(day))
else:
    print('{} invalid day)'.format(day))
'''
'''
i=0
while i==0:
 name=input('enter your name:')
 print(name)

 gender=input('enter your gender:').lower()
 if gender=='male':
    age=int(input('enter your age:'))
    if age>30:
        print('{}years.it is marraige time to marry'.format(age))
    else:
        print('{}years nothing to say'.format(age))
 elif gender=='female':
        age=int(input('enter your age:'))
        if age>25:
            print('{}years marraige time to marry'.format(age))
        else:
                print('{}years nothing to say'.format(age))
 else:
    print('{} is invalid gender'.format(gender))
i=i+0
'''
'''
i=0
while i==0:
 age=int(input('enter your age:'))
 if age>=0 and age<6:
    print('{}years.you are an infant'.format(age))
 elif age>=6 and age<17:
    print('{}years.you are school going kid'.format(age))
 elif age>=17 and age<23:
    print('{}years.you are college going kid'.format(age))
 elif age>=23 and age<31:
    print('{}years.you need to settle in life and get marry'.format(age))
 elif age>=31 and age<46:
    print('{}years.you need to work and earn money'.format(age))
 elif age>=46 and age<61:
    print('{}years.you need to take business'.format(age))
 elif age>=61:
    print('{}years.you need to take rest'.format(age))
 else:
    print('{} is invalid age'.format(age))
i=i+0    
'''

i=0
while i==0:
    h=int(input('enter your height in centimeters:'))
    height=h/100
    height=height**2
    print(height)
    weight=eval(input('enter your weight in kg:'))
    print(weight)
    bmi=weight/height
    print(bmi)
    if bmi>=0 and bmi<18.6:
        print(' bmi is {}.you are underweight'.format(bmi))
    elif bmi>=18.6 and bmi<25.0:
        print(' bmi is {}.you are normalweight'.format(bmi))
    elif bmi>=25.0 and bmi<30.0:
        print(' bmi is {}.you are pre-obesity'.format(bmi))
    elif bmi>=30.0 and bmi<40.1:
        print(' bmi is {}.you are obesite'.format(bmi))
    elif bmi>=40.1:
        print('bmi is {}.you are extremly obesity'.format(bmi))
i=i+0

'''i=0
while i==0:
    a=int(input('enter your number:'))
    if a<0 or a>=11:
            print('{} is invalid.enter number between 1 and 10'.format(a))
    elif a>0 and a<11:
        if a%2==0:
            print('{} is even number'.format(a))
        else:
                print('{} is odd number'.format(a))
i=i+0'''

        
    


