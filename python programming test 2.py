'''#1
lst=[]
st=input('enter any string:')
for i in st.split():
    i=i[0].upper()+i[1::]
    print(i,end=' ')
            
            
    
        
#2
st1='Python narayana tech house hyderabad'
print(' '.join([i[-1::-1] for i in st1.split()]))
#3
st2='Python narayana tech house HYDERABAD'
print(''.join([i.upper()if i in 'aeiouAEIOU'else i.lower() for i in st2 ]))
#4
a=[]
st4='Python narayana'
for i in st4:
    if i in 'aeiou':
        a.append(i)
for i in st4:
    if i not in 'aeiou':
        a.append(i)
print(''.join(a))
#5
st5='pyTHON NaRaYaNa'
a=[]
st4='Python narayana'
for i in st5:
    if i.isupper():
        a.append(i)
for i in st5:
    if i.islower()or i==' ':
        a.append(i)

print(''.join(a))
#6
a=[]
b=[]
st6='python narayana'
for i in st6:
    if i in 'aeiou':
        a.append(i)
    else:
        b.append(i)
print('Vowels Are:',len(a))
print('Consonants Are:',len(b))
#7

lst=[10,45,30,67,23,43]
for i in lst:
     if i>=lst[3]:
         print(i)
#8
lst=[10,True,11,'Python',False,12]
print([i for i in lst if type(i) is int])'''
#9
lst=[100,200,300,150,'NTH''Python']
print(lst)
i=eval(input('Enter Any Element:'))
if i in lst:
    print('{} is availabale in ',lst.index(i),'rd index position'.format(i))
'''#10
i=input('Enter Any String:')
for i in i.split():
    print(i[0].upper(),end='')
#11
a=int(input('Enter Any Number:'))
b=int(input('Enter Any Number:'))
c=int(input('Enter Any  Number:'))
if a>b:
 if a>c:
    print(a)
 else:
   print(c)
else:
    if b>c:
        print(b)
    else:
        print(c)
#12
a=[]
b=[]
st=input('Enter Any String:')
for i in st:
    if i in 'aeiouAEIOU':
        a.append(i)
    else:
        b.append(i)
if len(a)>len(b):
    print('Vowels Are Dominating String')
elif len(a)==len(b):
    print('EqualVowelsConsonantsError')
else:
    print('Consonants Are Dominating String')
#13
st=input('Enter Any String:')
st1='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
for i in st:
    a=st1.index(i)
    a=a+1
    print(st1[a],end='')'''

#set 2
'''#1. Write a program to fetch all odd elements into one list and even elements into another lis?
lst = [10,20,30,40,50,60,70,80,90,100]
a=[]
b=[]
for i in lst:
    if lst.index(i)%2==0:
        a.append(i)
    else:
        b.append(i)
print(a)
print(b)

#2. Write a program to fetch all words which has more than 5 characters?
a=input('enter any one line string:')
for i in a.split():
    if len(i)==5:
        print(i,end=' ')
#3. Write a program to fetch all numbers which are divisible by 3 and 5?
lst=[5,9,15,20,25,30,35,40]
for i in lst:
    if i%3==0:
        if i%5==0:
            print(i)
#4. Take one dict with 3 pairs, write a program to add new pair into that existing dict?
koti={'name':'ko','sal':10,'c':'w'}
print(koti)
koti['emi']=500
print(koti)
#5. Take a dict with 3 pairs, write a program to update any one value?
koti={'name':'ko','sal':10,'c':'w','emi':200}
koti['emi']=500
print(koti)
#6. Write a function called hi_bye() that takes a number given by user.
#-If the number is divisible by 3, it should return “Hi”.
#-If it is divisible by 5, it should return “Bye”.
#-If it is divisible by both 3 and 5, it should return “HiBye”.
#-Otherwise, it should return the same number
a=int(input('enter any number:'))
def hi_bye(b):
    if b%3==0 and b%5==0:
        print('hibye')
    else:
        if b%3==0:
            print('hi')
        elif b%5==0:
            print('bye')
        else:
            print(b)
hi_bye(a)

        
#7. WAP to insert * in place of every vowels in the string.
#Input: Python Narayana Tech House
#Output: Pyth*n N*r*y*n* T*ch H**s*
a=input('enter any string:')
b=a.replace('a','*').replace('e','*').replace('i','*').replace('o','*').replace('u','*')
print(b)
#8. Take one dict with 3 pairs, write a program to add new pair into that existing dict?
koti={'name':'ko','sal':10,'c':'w'}
print(koti)
koti['emi']=500
print(koti)

#9. Take a dict with 3 pairs, write a program to update any one value?
koti={'name':'ko','sal':10,'c':'w','emi':200}
koti['emi']=500
print(koti)

#10. Write A Python function to get first letter of each word of complete string given by user?
Note: Do not use pre-defined functions
Eg:
input: "python narayana tech house"
output: "Python Narayana Tech House"
lst=[]
st=input('enter any string:')
for i in st.split():
    i=i[0].upper()+i[1::]
    print(i,end=' ')'''
            
    


'''Set-1

Python Programming Test - 2
NTH – Python Job Oriented Batch

Narayana Tech House

9010607010, 8179817681 narayanatechhouse@gmail.com
A program on Moonlighting'''
emps = {
'emp1':{'name':'Rajesh', 'salaries':{'TCS':30000,'Wipro':40000,'Infosys':55000}, 'age':25,
'location':'Hyderabad'},
'emp2':{'name':'Kumar', 'salaries':{'CTS':40000,'NTH':60000,'Infosys':90000}, 'age':35,
'location':'Hyderabad'},
'emp3':{'name':'Satya', 'salaries':{'DeepCompute':20000,'Wipro':40000,'Infosys':50000},
'age':22, 'location':'Bangalore'},
'emp4':{'name':'Saroj', 'salaries':{'AXA':30000,'Infosys':40000,'Ignify':60000, 'Atos':65000},
'age':30, 'location':'Chennai'},
}
'''#11. Write a program to fetch all employees names who is working in Hyderabad?
for i in emps:
    if emps[i]['location']=='Hyderabad':
        print(emps[i]['name'])
    
#12. Write a program to fetch all employees who age is more then 30 years?
for i in emps:
    if emps[i]['age']>30:
        print(emps[i]['name'])'''


#13. Write a program to fetch all employees names who is working in Infosys?
lst=[]
for i in emps:
    for j in emps[i]['salaries']:
        if j=='Infosys':
            print(emps[i]['name'])
   

#14. Write a program to count total number of employees in Infosys?
lst=[]
c=0
for i in emps:
    if 'Infosys' in emps[i]['salaries']:
        c=c+1
print(c)
            
#15. Write a program to count total number of employees working in Bangalore?
c=0
for i in emps:
    if emps[i]['location']=='Bnglore':
        c=c+1
print(c)
'''16. Write a program to display employee name who is working in NTH company?'''
#17. Write a program to update the salary of Saroj in Axa company to 35000?
for i in emps:
    emps[i]['salaries']['AXA']=35000
print(emps)
#18. Write a program to display all employees names who is working in more then 3
for i in emps:
    if len(emps[i]['salaries'])>3:
        print(emps[i]['name'])
    
    

    






     
      


   

    
