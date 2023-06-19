'''#print all names in the file?
import re
x=open('nthadata1.txt','r').read().replace('\n',',')
n=re.findall('[A-Z][a-z]+\.[A-Z][a-z]+\s?[A-Za-z]*',x)
print(n)
lst=[]
for i in open('nthadata1.txt','r').read().replace('\n',',').split(','):
    n=re.fullmatch('[A-Z][a-z]+\.[A-Z][a-z]+\s?[A-Za-z]*',i)
    if n!=None:
        lst.append(i)
print(lst)

#print all aadhar numbers in the file?
x=open('nthadata1.txt','r').read().replace('\n',',')
n=re.findall('[A-Z][a-z]+\.[A-Z][a-z]+\s?[A-Za-z]*',x)
m=re.findall('[0-9]{4}\s[0-9]{4}\s[0-9]{4}',x)
print('names',n,'=','aadhar',m)
#print all  numbers in the file?
x=open('nthadata1.txt','r').read().replace('\n',',')
n=re.findall('[A-Z][a-z]+\.[A-Z][a-z]+\s?[A-Za-z]*',x)
m=re.findall('[0-9]{4}\s[0-9]{4}\s[0-9]{4}',x)
o=re.findall('[A-Za-z]+\s?\.?[0-9]*\.?[a-z]*[0-9]*\@[a-z]+\.[a-z]+',x)
print('names',n,'=','aadhar',m,'=email',o)
#print all aadhar numbers in the file?
import re
x=open('nthadata1.txt','r').read().replace('\n',',')
n=re.findall('[A-Z][a-z]+\.[A-Z][a-z]+\s?[A-Za-z]*',x)
m=re.findall('[0-9]{4}\s[0-9]{4}\s[0-9]{4}',x)
o=re.findall('[A-Za-z]+\s?\.?[0-9]*\.?[a-z]*[0-9]*\@[a-z]+\.[a-z]+',x)
p=re.findall('[A-Z]{5}[0-9]{4}[A-Z]',x)
print('names',n,'=','aadhar',m,'=email',o,'=PAN',p)
#print mobile number ofMR.Jagan?
import re
x=open('nthadata1.txt','r').read().split('\n')
for i in x:
    if 'Mr.Jagan' in i:
        n=re.search('[6-9][0-9]{9}',i)
        print(n)'''
# print names of Andhra Pradesh?
import re
x=open('nthadata1.txt','r').read().split('\n')
print(x)
for i in x:
    if 'Andhra Pradesh' in i:
        n=re.findall('[A-Z][a-z]+\.[A-Z][a-z]+\s?[A-Z]*[a-z]*',i)
        if n!=None:
            print(n)

        
    





