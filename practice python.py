'''i=0
while i==0:
    marks=int(input('enter your marks:'))
    if marks>34:
            print('you passed exam')
i=i+0'''
'''for i in range(10,1,-1):
    print(i)'''
'''i=1
while i<11:
    print(i)
    if i==6:
      break
i=i+1'''
'''i=1
while True:
    print(i)
    i=i+1'''
'''i=0
while i<11:
    print(i)
    if i==5:
        continue
    i=i+1'''
'''i=0
while i<11:
    i=i+1
    if i==5:
        continue
    print(i)'''
'''i=0
while i<11:
    print(i)
    if i==6:
        continue
    i=i+1'''
'''i=0
while i<11:
    if i==3:
        i=i+1
        continue
    print(i)
    i=i+1
    '''
#write python comprehensions for the following programs
st='narayana tech house ameerpet hyderabad'
#1'hyderabad ameerpet house tech narayana'
#2'anayara hcet esuoh tepreema dabaredeyh'
#3 'dabarehyd tepreema esuoh hcet anayara'
#4'narayana house ammerpet'
#5;ara
#10 'tech'
#9 'hyderabad'
#8[8,4,5,8,9]
#7'narayanatechhouseamerpethyderabad'
#6'narayana tec

'''#10
print([j for j in [i for i in st.split()] if len(j)==min([len(i) for i in st.split()])])
#9
print([j for j in [i for i in st.split()] if len(j)==max([len(i) for i in st.split()])])
#8
print([len(i) for i in st.split()])
#7
print([i for i in st.replace(' ','').split()])
#2
print([j[-1::-1] for j in [i for i in st.split()]])
#3
print([j[-1::-1 ] for j in [i for i in st.split()]])
#4
print([i for i in st.split() if st.split().index(i)%2==0])
#2
print([i[-1::-1] for i in st.split()[-1::-1]])
#1
print([i for i in st.split()[-1::-1]])
#6'''
'''print([i for i in st.replace('a','').replace('e','').replace('i','').replace('o','').replace('u','').split()])
#5

print(''.join ([i for i in st if i in ' AEIOuaeiou']))'''
print(st.index('a'))

    
        


'''print([j for j in [i for i in st.split()]])'''
'''print(lst)
print([i for i in st.split() 
'''
'''#1 reverse string
s='geeeks quiz practice code'
print(' '.join([i for i in s.split()[-1::-1]]))
st='narayana tech house ameerpet hyderabad'
print(' '.join([i for i in st.split()[-1::-1]]))
c='i love programming very much'
print(' '.join([i for i in c.split()[-1::-1]]))
# to find the longest prefix
lst=['geeksforgeeks','geeks','geek','geazer']
for i in lst'''
#removevowels
'''
t='geeeksforgeeks'
print(''.join([i for i in t if i not in 'aeiou']))
#
st=''
s='1.1.1.1'
for i in s:
    if i=='.':
        st='[.]'
    else:
        st=st+i
        print(st,end='')
#
   '''     


























    
