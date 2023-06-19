#write a orogram to fetch all pan  numbers in the file
lst=[]
import re
x=open('nthdata.txt','r').read().replace('\n',',')
y=re.findall('[A-Z]{5}[0-9]{4}[A-Z]',x)
print(y)
#or
lst=[]
for  i in open('nthdata.txt','r').read().replace('\n',',').split(','):
    n=re.fullmatch('[A-Z]{5}[0-9]{4}[A-Z]',i)
    if n!=None:
        lst.append(i)
print(lst)
#2 write a program to fetch all employees names in the file

lst=[]
for  i in open('nthdata.txt','r').read().replace('\n',',').split(','):
    n=re.fullmatch('[A-Za-z]{2,3}\.{1}[A-Za-z]+',i)
    if n!=None:
        lst.append(i)
print(lst)
#3 write a program to fetch all vehicle registration numbers
lst=[]
for  i in open('nthdata.txt','r').read().replace('\n',',').split(','):
    n=re.fullmatch('[A-Z]{2}\s?[0-9]{2}\s?[A-Z]{2}\s?[0-9]{4}',i)
    if n!=None:
        lst.append(i)
print(lst)
#4write a program to fetch all email ids
lst=[]
for  i in open('nthdata.txt','r').read().replace('\n',',').split(','):
    n=re.fullmatch('[a-z]+\.?[a-z]+\@[a-z]{5,7}\.[a-z]{2,4}',i)
    if n!=None:
        lst.append(i)
print(lst)
#5 write a program to fetch all company names
lst=[]
for  i in open('nthdata.txt','r').read().split('\n'):
    print(i)
    n=re.fullmatch('[A-Z]{1,}[a-z]{0,}\s[a-z]+',i)
    if n!=None:
        lst.append(i)
print(lst)
#6 write a program to fetch all mobile numbers
lst=[]
for  i in open('nthdata.txt','r').read().replace('\n',',').split(','):
    n=re.fullmatch('[6-9]{1}[0-9]{9}',i)
    if n!=None:
        lst.append(i)
print(lst)
#7 write a program to fetch a mobile number of mr.Aakash
import re
x=open('nthdata.txt','r').read().split('\n')
for i in x:
    j=i.split(',')
    for k in j:
        if k=='Mr.Aakash':
            for k in j:
                n=re.fullmatch('[6-9]{1}[0-9]{9}',k)
                if n!=None:
                    print(n)
#8 write a program to fetch a vehicle registration number of mrs.renu
import re
x=open('nthdata.txt','r').read().split('\n')
for i in x:
    j=i.split(',')
    for k in j:
        if k=='Mrs.Renu':
            for k in j:
                n=re.fullmatch('[A-Z]{2}\s?[0-9]{2}\s?[A-Z]{2}\s?[0-9]{4}',k)
                if n!=None:
                    print(n)
#9 write a program to fetch company name of an employee from ap
import re
x=open('nthdata.txt','r').read().split('\n')
print(x)
for i in x:
    m=re.search('AP',i)
    if m!=None:
        print(m)
for i in x:
    if 'AP' in i:
        n=re.search('[A-Z]{1,}[a-z]*\s[a-z]+',i)
        print(n)
#10write a program to display all male employees
import re
lst=[]
for i in open('nthdata.txt','r').read().replace('\n',',').split(','):
     m=re.fullmatch('[A-Z]{1}[r]{1}\.[A-Za-z]+',i)
     if m!=None:
         lst.append(m)
print(lst)
#11 write a program to display email id of an unmarried employee
import re
for i in open('nthdata.txt','r').read().split('\n'):
    m=re.findall('[A-Z]{1}s\.[A-Z]{1}[a-z]+',i)
    if m!=[]:
        n=m
        print(n)
for i in open('nthdata.txt','r').read().split('\n'):
    if n==re.findall('[A-Z]{1}s\.[A-Z]{1}[a-z]+',i):
         o=re.findall('[a-z]+\.?[a-z]+[\@[a-z]{5,7}\.[a-z]{2,4}',i)
         print(o)
    
#12 write a program to display employee name where email contain python
import re
lst=[]
for i in open('nthdata.txt','r').read().split('\n'):
    m=re.findall('[a-z]+\.python\@[a-z]{5,7}\.[a-z]{2,4}',i)
    if m!=[]:
        lst.append(m)
for i in open('nthdata.txt','r').read().split('\n'):
    if re.findall('[a-z]+\.?python[\@[a-z]{5,7}\.[a-z]{2,4}',i) in lst:
        n=re.findall('[A-Z][a-z]{1,2}\.{1}[A-Za-z]+',i)
        print(n)
        
        

        
    
    


        
        


    
    

        

        
    
    
        


        







    
    
    

