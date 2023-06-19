'''1. Write A Python function to convert first letter of each word into uppercase of
complete string given by user?
Note: Do not use pre-defined functions
Eg:
input: "python narayana tech house"
output: "Python Narayana Tech House"
a=input('enter your string:')
print(' '.join([i[0].upper()+i[1:]for i in a.split()]))'''
'''2. Write a Python Function to reverse of each word in the string given by user?
Eg:
input: "python narayana tech house hyderabad"
output: "nohtyp anayaran hcet esuoh dabaredyh"
a=input('enter your string:')
def reverse(a):
    print(' '.join([i[-1::-1] for i in a.split()]))
reverse(a)'''

'''3. Write A Python Function to write vowels in uppercase and consonants in lowercase
of same string given by user?
Eg:
input: "python narayana tech house HYDERABAD"
output: "pythOn nArAyAnA tEch hOUsE hydErAbAd"
a=input('enter your string:')
def vowels(a):
    print(''.join([i.upper() if i in 'aeiouAEIOU' else i.lower() for i in a]))
vowels(a)'''

'''4. Write a Python Function to seperate vowels and consonants from given string
input: 'python narayana'
output:oaaaapythn nryn
a=input('enter your string:')
b=[]
c=[]
def seperate(a):
    x=[b.append(i) for i in a if  i in 'aeiouAEIOU']
    x=[b.append(i) for i in a if  i not in 'aeiouAEIOU']
        
    print(''.join(b))
seperate(a)'''
'''5. Write comprehension to count total number of characters (excluding space)?
st = 'Python Narayana Tech House Hyderabada'
print(len([i for i in st if i!=' ']))'''

'''6. Write a comprehension to longest palindrome word?
names = ['madam', 'python','dad','language','eye','malayalam']

print([len(i) for i in names if i==i[-1::-1]])'''

'''7. Write Python Function to Find The Abbreviation form of given string?
Eg1:
Enter Any String: 'NARAYANA Tech House'
Abbreviation Form is NTH.
Eg2:
Enter Any String: Integrated Development Learning Environment.
Abbreviation Form is IDLE.
a=input('enter your abbrevation fullform:')
def abbrevation(a):
     print(''.join([i[0].upper() for i in a.split()]))
abbrevation(a)'''
'''8. Write a Python Function to seperate upper case and lower case characters from
given string
input: 'pyTHON NaRaYaNa'
output:THONNRYNpy aaaa
a=input('enter your string:')
b=[]
c=[]
def upper(a):
    x=[b.append(i) for i in a if i.islower()]
    x=[b.append(i) for i in a if i.isupper()]
   
    print(''.join(b))
    
upper(a)'''
'''9. Write a function called hi_bye() that takes a number given by user.
-If the number is divisible by 3, it should return “Hi”.
-If it is divisible by 5, it should return “Bye”.
-If it is divisible by both 3 and 5, it should return “HiBye”.
-Otherwise, it should return the same number.
a=int(input('enter your number:'))
def hi_bye(a):
    if a%3==0 and a%5==0:
        print('hibye')
    else:
        if a%3==0:
            print('hii')
        elif a%5==0:
            print('bye')
        else:
            print(a)
hi_bye(a)'''
        
            
    

'''10. Write Python Program to read a string from user. Count total number of vowels and
consonants in the string.
If more vowels are there then display "Vowels Dominated String."
If more consonants are there then display "Consonants Dominated String."
If Equal number of Vowels and Consonants are then raise error
"EqualVowelsConsonantsError".
a=input('enter your string:')
c=0
b=0
for i in a:
    if a in 'aeiouAEIOU':
        c=c+1
    else:
        b=b+1
if c>b:
    print('vowels are dominating')
elif c<b:
    print('consonants are dominating')
elif c==b:
    print('EqualVowelsconsonantsError')'''
print('==========================================================================================================================================')
'''1. Write A Python Function to write vowels in uppercase and consonants in lowercase
of same string given by user?
Eg:
input: "python narayana tech house HYDERABAD"
output: "pythOn nArAyAnA tEch hOUsE hydErAbAd"
a=input('enter your string:')
def vowels(z):
    print(''.join([i.upper() if i in 'aeiouAEIOU' else i.lower() for i in z]))
vowels(a)'''
'''2. Write a Python Function to seperate vowels and consonants from given string
input: 'python narayana'
output:oaaaapythn nryn
a=input('enter your string:')
b=[]
def vowels(z):
    for i in z:
        x=[i for i in z if i in 'aeiouAEIOU']
    print(x)
    for i in z:
        x=[x.append(i) for i in z if i not in 'aeiouAEIOU']
    print(x)
    
vowels(a)'''
        
'''3. Write a Python Function to seperate upper case and lower case characters from
given string
input: 'pyTHON NaRaYaNa'
output:THONNRYNpy aaaa
4. Write a Python Function to count number of vowels and consonants from given string.
input: 'python narayana'
output:
Vowels Are: 5
Consonants Are: 10

5. Write a Python Function to reverse of each word in the string given by user?
Eg:
input: "python narayana tech house hyderabad"
output: "nohtyp anayaran hcet esuoh dabaredyh"

NTH – Python Job Oriented Batch
Python Programming Test – 3

Set-3

6. Write Python Function to remove all vowels from given string.
Eg1:
Enter Any String: Narayana
String without Viwels: Nryn
7. Write Python Program to read a string from user. Count total number of vowels and
consonants in the string.
If more vowels are there then display "Vowels Dominated String."
If more consonants are there then display "Consonants Dominated String."
If Equal number of Vowels and Consonants are then raise error
"EqualVowelsConsonantsError".'''

8. Write a comprehension to longest palindrome word?
names = ['madam', 'python','dad','language','eye','malayalam']
9. Write a comprehension to fetch the first and last character from each
word in the string?'''
st = 'Python is simple and easy language'

'''10. Write a comprehension to fetch all words which starts and ends with vowel in the string? 

st = 'Python is simple and ease language'
print([i for i in st.split() if i[0] in 'aeiouAEIOU' and i[-1] in 'aeiouAEIOU'])'''

'''6. Write a comprehension to longest palindrome word?
names = ['madam', 'python','dad','language','eye','malayalam']
print([j for j in [i for i in names if i==i[-1::-1]] if len(j)==min([len(i) for i in names if i==i[-1::-1]])])'''


