'''#1. Write a program to fetch all even numbers from list? lst = [10,11,13,14,9,8] #[10,14,8]
lst = [10,11,13,14,9,8]
for i in lst:
    if i%2==0:
        print(i)
#2. Write a program to fetch all string values from list? lst = [10,'a',True,'b',False] #['a', 'b']
lst = [10,'a',True,'b',False]
for i in lst:
    if type(i) is str:
        print(i)
#3. Write a program to fetch all 5 divisibles from list?
lst = [12,15,27,20,5]
for i in lst:
    if i%5==0:
        print(i)
        
#4. Write a program to count total number of int values in the list
lst = [10,'a',20,True,30,'b',40]
a=[]
for i in lst:
    if type(i) is int:
        a.append(i)
print(len(a))
#5. Write a program to count total number of characters in the string(including space)?.
st = 'Python language'
print(len(st))
#6. Write a program to count total number of words in the string.
st = 'python narayana tech house hyd'
st1=st.split()
print(len(st1))
#7. Write a program to fetch all vowels from the string?
st = 'Python language'
for i in st:
    if i in 'aeiouaAEIOU':
        print(i)
#8. Write a program to count total number of vowels
st = 'python narayana'
st1=[]
for i in st:
    if i in 'aeiouAEIOU':
       st1.append(i)
print(len(st1))
#9. Write a program to count total number of characters in the string(excluding space)?
st = 'python is a simple language'
j=0
st1=st.split()
for i in st1:
    j=j+len(i)
print(j)
#10. Write a program to count total number of consonants in the string?
st = 'python language'
j=0
for i in st:
    if i not in 'aeiou':
        j=j+len(i)
print(j)
#11. Write a program to fetch all words which starts with vowel from given string?
st = 'Python is simple and easy language'
st1=st.split()
for i in st1:
    if i[0] in 'aeiou':
        print(i,end=' ')
#12. Write a program to fetch all words which ends with consonent in the given string?
st = 'Python is simple and easy language'
st1=st.split()
for i in st1:
    if i[-1] not in 'aeiou':
        print(i,end=' ')
#13. Write a program to fetch all words which 'a' two or more then two times?
st = 'Python is simple and easy language'
st1=st.split()
print(st1)
for i in st1:
    if i.count('a')>1:
        print(i)
#14. Write a program to count number of characters of each word in the string?
st = 'Python is simple and easy language'
st1=st.split()
for i in st1:
    print(len(i))
#1515. Write a program to fetch the first and last character from each word in the string?
st = 'Python is simple and easy language'
st1=st.split()
for i in st1:
    j=i[0]+i[-1]
    print(j)
#16. Write a program to fetch all words which contains 'a' character in the string?
st = 'Python is simple and easy language'
st1=st.split()
for i in st1:
    if 'a' in i:
        print(i)
#17. Write a program to fetch all words which does not contain 'e' character in string?
st = 'Python is simple and easy language'
st1=st.split()
for i in st1:
    if 'e' not in i:
        print(i,end=' ')
#18. Write a program to fetch all words which contains only 4 or lessthen 4 characters?
st = 'Python is simple and easy language'
st1=st.split()
for i in st1:
    if len(i)<=4:
        print(i)
#19. Write a program to fetch all words which contain odd number of characters in the string?
st = 'Python is simple and easy language'
st1=st.split()
for i in st1:
    if len(i)%2==1:
        print(i)
#20. Write a program to fetch all words which starts and ends with vowel in the string?
st = 'Python is number one language'
st1=st.split()
for i in st1:
    if i[-1] in 'aeiou':
        print(i)
#21. Write a program to fetch all palindrome words from list?
names = ['madam', 'python','dad','language','eye','malayalam']
for i in names:
    if i==i[-1::-1]:
        print(i)
#22. Write a program to fetch all non-palindrome words from list?
names = ['madam', 'python','dad','language','eye','malayalam']
for i in names:
    if i!=i[-1::-1]:
        print(i)
#23. Write a program to fetch all palindrome words which starts with 'm' character?
names = ['madam', 'python','dad','language','eye','malayalam']
for i in names:
    if i==i[-1::-1]:
        if i[0]=='m' and i[-1]=='m':
            print(i)
#24. Write a program to fetch all palindrome words which more then 3 characters?
names = ['madam', 'python','dad','language','eye','malayalam']
for i in names:
    if i==i[-1::-1]:
        if len(i)>3:
            print(i)'''
#25. Write a program to longest palindrome word?
names = ['madam', 'python','dad','language','eye','malayalam']
j=[]
for i in names:
    if i==i[-1::-1]:
        j.append(i)
print(j)
k=[]
for i in j:
    k.append(len(i))
print(k)
for i in k:
    if i==max(k):
        l=i
print(l)
for i in names:
    if len(i)==l:
        print(i)

        
        
    
        








































    






    
        

    
        
 






























    
        
