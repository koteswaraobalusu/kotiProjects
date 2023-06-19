'''#1
print(open('nthfile.txt','r').read())
#2
print(open('nthfile.txt','r').readlines())
#3
print(open('nthfile.txt','r').readlines()[-1])
#4
print(open('nthfile.txt','r').readlines()[2])
#5
print(open('nthfile.txt','r').readlines()[1].split(',')[0])
#6
print(open('nthfile.txt','r').readlines()[-1].split(',')[-1])
#7
print(open('nthfile.txt','r').readlines()[2].split(',')[1][0])
#8
print(open('nthfile.txt','r').readlines()[1].replace('\n','')[-1])
#9
print([i.split(',')[0] for i in open('nthfile.txt','r').readlines()])
#10
print([i.split(',')[-1].replace('\n','') for i in open('nthfile.txt','r').readlines()])
#11
print(len(open('nthfile.txt','r').readline()))
#12
print(len(open('nthfile.txt','r').readlines()[1].split(',')[1]))
#13
print(len(open('nthfile.txt','r').read()))
#14
print([i[0] for i in open('nthfile.txt','r').readlines()[2].split(',')])
#15
print(open('nthfile.txt','r').readline().split(',')[2][-1::-1])
#16
print([open('nthfile.txt','r').read().count(',')])'''
#17
x=[i for i in open('nthfile.txt','r').read().replace('\n','').split(',') ]
print(x)
for i in x:
    if i[0] in 'aeiouAEIOU':
        print(i)
#or
lst=[]
for i in open('nthfile.txt','r').readlines():
    x=i.split(',')
    for i in x:
        if i[0] in 'aeiouAEIOU':
            lst.append(i)
print(lst)
'''
#18
lst=[]
for i in open('nthfile.txt','r').readlines():
    x=i.split(',')
    for i in x:
        if i[-1] in 'aAiI':
            lst.append(i)
print(lst)
#19
lst=[]
for i in open('nthfile.txt','r').readlines():
    i=i.replace('\n','')
    x=i.split(',')
    for i in x:
        if len(i)==5:
            lst.append(i)
print(lst)
#20
lst=[]
for i in open('nthfile.txt','r').readlines():
    i=i.replace('\n','')
    x=i.split(',')
    for i in x:
        if i==i[-1::-1]:
            lst.append(i)
print(lst)
#21
lst=[]
for i in open('nthfile.txt','r').readlines():
    i=i.replace('\n','')
    x=i.split(',')
    for i in x:
        if i not in lst:
            lst.append(i)
print(lst)
#22
lst=[]
for i in open('nthfile.txt','r').readlines():
    i=i.replace('\n','')
    x=i.split(',')
    for i in x:
        if i[0] in 'aeiouAEIOU':
            if len(i)>4:
               lst.append(i)
print(lst)
#23
for i in open('nthfile.txt','r').readlines():
    i=i.replace('\n','')
    x=i.split(',')
    for i in x:
        if i[0] in 'aeiouAEIOU':
            if i[-1] in 'aeiouAEIOU':
                lst.append(i)
print(lst)
#24
lst=[]
for i in open('nthfile.txt','r').readlines():
    i=i.replace('\n','')
    i=i.replace(' ','')
    x=i.split(',')
    for i in x:
        lst.append(len(i))
print(lst)
for i in open('nthfile.txt','r').readlines():
    i=i.replace('\n','')
    i=i.replace(' ','')
    x=i.split(',')
    for i in x:
        if len(i)==max(lst):
            print(i)

#25
lst=[]
for i in open('nthfile.txt','r').readlines():
    i=i.replace('\n','')
    i=i.replace(' ','')
    x=i.split(',')
    for i in x:
        lst.append(len(i))
print(lst)
print(min(lst))
for i in open('nthfile.txt','r').readlines():
    i=i.replace('\n','')
    i=i.replace(' ','')
    x=i.split(',')
    for i in x:
       if len(i)==min(lst):
           print(i)'''










