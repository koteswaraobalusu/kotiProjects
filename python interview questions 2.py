'''a=input('enter a string:')
#total string in reverse
print(a[-1::-1])
#total characters in alphabetical order
print(''.join(sorted(a)))
#each word in reverse order
print(' '.join([i[-1::-1] for i in a.split()]))
# total characters in reverse alphabetical order
print(''.join(sorted(a,reverse=True)))
# find the odd position of a string
for i in a.replace(' ',''):
    if a.index(i)%2==1:
        print(i)
#how to check starts with specified string or not by using startswith()and ends with specified substring or not by using endswith()
        
# how to remove unwanted characters by using replace()
#How to find the number of matching characters in two string
import re
b=input('enter a string:')
c=0
for i in a:
    if re.search(i,b):
        c=c+1
print(c)'''
# to convert string into list by using split()
#How to convert all string elements of list to int.
lst=['10','20','30']
print([int(i) for i in lst])
#.Count Total numbers of upper case and lower case characters in input string
#14. How to reverse a user input string
input_string = input('Please Enter the string:')
 
reversed_str =''.join(reversed(input_string))
 
print('reversed string =',reversed_str)
#15. Program to sort a string in Python
input_string = input('Please Enter the string:')
 
sortedStr = sorted(sorted(input_string), key= str.upper)
 
print('sorted String =',sortedStr)
    
