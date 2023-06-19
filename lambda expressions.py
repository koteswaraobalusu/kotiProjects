x= open('nthfile.txt','r').read().replace('\n',',').split(',')
    
print(list(filter(lambda i:len(i)==4,x)))
print(list(filter(lambda i:i[0]=='s',x)))
print(list(map(lambda i:len(i),x)))
y=list(filter(lambda i:i[0] in 'aeiouAEIOU',x))
print(x)
print(list(map(lambda i:i[0],y)))
z=list(filter(lambda i:'a' in i,x))
print(list(map(lambda i:len(i),z)))
a=list(filter(lambda i:i[-1] in 'aeiouAEIOU',x))
print(list(map(lambda i:i[-1::-1],a)))





