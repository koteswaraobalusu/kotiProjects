'''string functons
1.concatenation
2.join
3.repetation
4.packing
5.unpacking
6.len()
7.index()
8.count()
9.lower()
10.upper()
11.swapcase()
12.islower()
13.isupper()
14.startswith()
15.endswith()
16.title()
17.capitalize()
18.split()
19.replace()'''
#1 to check whether the string is symmetrical  or polindrome
st='malayalam'
print([i for i in st.split() if i==i[-1::-1]])
print(st==st[-1::-1])
#2 string reverse
st='geeks for practice code'
print(' '.join([i for i in st.split()[-1::-1]]))
#3 remove a character in string
st='malayalam telugu'
print(''.join([st[i] for i in range(len(st)) if i!=2]))
#4 length of string including space
st='python language'
print(len([i for i in st]))
#4 length of string removing space
print(len([i for i in st.replace(' ','')]))
#5print even letters in string
st='python language'
print(''.join([st[i] for i in range(len(st)) if i%2==0]))
#5print even words in string
st='python language is very powerful'
print([i for i in st.split() if st.split().index(i)%2==0])
st=st.split()
print([st[i]for i in range(len(st)) if i%2==0])
#





