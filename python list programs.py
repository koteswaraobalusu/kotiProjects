'''#Python program to interchange first and last elements in a list
lst=['kohli','dhoni','rohit','surya']
lst[0],lst[-1]=lst[-1],lst[0]
print(lst)'''
'''#Python program to swap two elements in a list
lst=['kohli','dhoni','rohit','surya']
lst[0],lst[2]=lst[2],lst[0]
print(lst)'''
'''#Python – Swap elements in String list
import re
lst=['kohli','dhoni','rohit','surya']
for i in lst:
    r=re.sub('o','y',re.sub('i','a',i))
    print(r)'''
'''#Python | Reversing a List
lst=['kohli','dhoni','rohit','surya']
print(lst[-1::-1])'''
#python list cloning or copying
import copy
lst=['kohli','dhoni','rohit','surya']
lst1=copy.copy(lst)
print(lst1)
