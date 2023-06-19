'''lst=[12,7,5,9.10,14]
print([i for i in lst if i%2==0])
'''
'''lst=[3,6,8,21,50,99]
print([i for i in lst if i%3==0])
'''
'''st='python narayana tech house'
print([i for i in st if i in 'aeiouAEIOU'])
'''
'''
st='python is simple and easy language'
st1=st.split()
print([i for i in st1 if len(i)==4])
'''
'''st='python is simple and easy language'
st1=st.split()
print([i for i in st1 if i[0] in 'aeiouAEIOU'])
'''
'''lst=[10,'a',True,10.5,20,False,30]
print([i for i in lst if type(i)==int])
'''
'''
names=['eyes','pen','apple','lap','elephant']
print([i for i in names if i[0] in 'aeiouAEIOU'])
'''
'''names=['eyes','pen','apple','lap','elephant']
print([i for i in names if i[-1] in 'aeiouAEIOU'])
'''
'''names=['eyes','pen','apple','lap','elephant']
print([i for i in names if i[0] not in 'aeiouAEIOU'])'''
'''
'''
'''names=['eyes','pen','apple','lap','elephant']
print([i for i in names if i[0] and i[-1] in 'aeiouAEIOU'])
'''
'''names=['eyes','pen','apple','lap','elephant']
print([i for i in names if i[-1] and i[0] not in 'aeiouAEIOU'])
'''
'''names=['eyes','pen','apple','lap','elephant']
print([i for i in names if i[0] in 'aeiouAEIOU' and i[-1] not in 'aeiouaeiou'])
'''
'''names=['eyes','pen','apple','lap','elephant']
print([i for i in names if i[0] not in 'aeiouAEIOU' and i[-1] in 'aeiouAEIOU'])
'''
'''lst=['kamal','ajay','sai','satya','narayana']
print([i for i in lst if len(i)==5])'''
'''lst=['akash','rajesh','ramya','eyes','eswar']
print([i for i in lst if len(i)>4])'''
'''
lst=['akash','ramya','narayana','python']
print([i for i in lst if i.count('a')>=3])
'''
'''
'''
'''lst=['amala','rajesh','hemanth','python']
print([i for i in lst if i[0]==i[-1]])'''
'''lst=['mom','python','madam','django','malayalam']
print([i for i in lst if i!=i[-1::-1]])'''
'''st='python is simple and easy language'
st1=len(st.split())
print(st1)'''
st='python is simple and easy language'
st1=st.split()
print([i for i in st1 if i[0] in 'aeiouAEIOU' and i[-1] not in 'aeiouAEIOU'])

















