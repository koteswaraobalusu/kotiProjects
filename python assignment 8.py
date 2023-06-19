#1
lst=[10,11,13,14,9,8]
print([i for i in lst if i%2==0])
#2
lst=[10,'a',True,'b',False]
print([i for i in lst if type(i)==str])
#3
lst=[12,15,27,20,5]
print([i for i in lst if i%5==0])
#5
lst='python language'
print(len(lst))
#4
lst=[10,'a',20,True,30,'b',40]
print(len([i for i in lst if type(i)==int]))
#6
lst='python narayana tech house hyderabad'
print(len(lst.split(' ')))
#7
lst='python language'
print([i for i in lst if i in 'aeiou'])

#8
lst='python narayana'
print(len([i for i in lst if i in 'aeiou']))
#9
lst='python is a simple language'
print(len([i for i in lst.replace(' ','')]))
#10
lst='python language'
print(len([i for i in lst.replace(' ','') if i not in 'aeiou']))
#11
lst='python is simple and easy language'
print([i for i in lst.split(' ') if i[0] in 'aeiou'])
#12
lst='python is simple and easy language'
print([i for i in lst.split(' ') if i[-1] not in 'aeiou'])

#13
lst='python is simple and easy language'
print([i for i in lst.split(' ') if i.count('a')>=2])
#4
lst='python language'
print(len([i for i in lst]))
#14
lst='python is simple and easy language'
print([len(i) for i in lst.split(' ')])
#15
lst='python is simple and easy language'
print([i[0]+i[-1]for i in lst.split(' ')])
#16
lst='python is simple and easy language'
print([i for i in lst.split(' ') if 'a' in i])
#17
lst='python is simple and easy language'
print([i for i in lst.split(' ') if 'e' not in i])
#18
lst='python is simple and easy language'
print([i for i in lst.split(' ') if len(i)<=4])
#19
lst='python is simple and easy language'
print([i for i in lst.split(' ') if len(i)%2==1])
#20
lst='python is number one language'
print([i for i in lst.split(' ') if i[0] in 'aeiou' and i[-1] in 'aeiou'])
#21
lst=['madam','python','dad','language','eye','malayalam']
print([i for i in lst if i==i[-1::-1]])
#22
lst=['madam','python','dad','language','eye','malayalam']
print([i for i in lst if i!=i[-1::-1]])
#23
lst=['madam','python','dad','language','eye','malayalam']
print([i for i in lst if i==i[-1::-1] and i[0]=='m'])
#24
lst=['madam','python','dad','language','eye','malayalam']
print([i for i in lst if i==i[-1::-1] and len(i)>3])
#25
lst=['madam','python','dad','language','eye','malayalam']
x=[len(i) for i in lst if i==i[-1::-1]]
print([i for i in lst if len(i)==max(x)])































