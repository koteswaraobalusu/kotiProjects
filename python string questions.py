#Basic String Programs
#_________________________
'''#1Python program to check whether the string is Symmetrical or Palindrome
a=input('enter a polindrome:')
if a==a[-1::-1]:
    print('{} is polindrome'.format(a))
else:
    print('{} is not a polindrome'.format(a))'''
'''#2Reverse words in a given String in Python
a=input('enter a string:')
print('{} reverse is'.format(a),a[-1::-1])'''
'''#Ways to remove i’th character from string in Python
a=input('enter a string:')
print(a.replace('i',''))'''

'''#Find length of a string in python (4 ways)
a=input('enter a string:')
print(len(a))'''
'''#Python – Avoid Spaces in string length
a=input('enter a string:').replace(' ','')
print(len(a))'''
'''#Python program to print even length words in a string
a=input('enter a string:').split()
for i in a:
    if a.index(i)%2==0:
        print(i)'''
'''#Python – Uppercase Half String
a=input('enter a string:')
b=len(a)//2
c=[]
for i in range(len(a)):
    if i<b:
        c.append(a[i].upper())
    else:
        c.append(a[i].lower())
print(''.join(c))'''
        
        
'''#Python program to capitalize the first and last character of each word in a string
a=input('enter a string:').split()
b=[]
for i in a:
    x=i[0].upper()+i[1:-1]+i[-1].upper()
    b.append(x)
print(b)'''

    


'''#Python program to check if a string has at least one letter and one number
a=input('enter a string:')
print(a.isalnum())'''
'''#Python | Program to accept the strings which contains all vowels
myStr =  input('Enter the string : ')
myStr = myStr.lower()
allVowels = set("aeiou")

for char in myStr :
    if char in allVowels :
        allVowels.remove(char)

print("Entered String is ", myStr)
if len(allVowels) == 0:
    print("The string contains all vowels")
else :
    print("The string does not contain all vowels")'''
'''#Python | Count the Number of matching characters in a pair of string
a=input('enter a string:')
for i in a:
    ifa.count(i)>=2:
        print(i)'''
'''#Python program to count number of vowels using sets in given string
a=input('enter a string:')
count=0
for i in a:
    if i in 'aeiouAEIOU'"
    count=count+1
print(count)'''
'''#Python Program to remove all duplicates from a given string
a=input('enter a string:')
print(set(a))'''
'''#Python – Least Frequent Character in String
a=input('enter a string:').replace(' ','')
b=set(a)
d={}.fromkeys(b,0)
print(d)
for i in a:
    if i in d:
        d[i]=d[i]+1
print(min(d.values()))
for i in d:
    if d[i]==min(d.values()):
        print(i)'''
    
'''#Python | Maximum frequency character in String
a= input('enter a string:')
b=set(a)
d={}.fromkeys(b,0)
print(d)
for i in a:
    if i in d:
        d[i]=d[i]+1
print(d)
for i in d:
    if d[i]==max(d.values()):
        print(i)'''
'''#Python – Odd Frequency Characters
a=input('enter a string:')
print(a[0::2])
print(a[1::2])'''
'''#Python – Specific Characters Frequency in String List
a=input('enter a string:')
b=input('enter your specific characters in frequency:')
for i in a:
    if i in b:
        print(i)'''
#Python | Frequency of numbers in String
a=input('enter a string:')
'''Python | Program to check if a string contains any special character
Generating random strings until a given string is generated
Find words which are greater than given length k
Python program for removing i-th character from a string
Python program to split and join a string
Python | Check if a given string is binary string or not
Python | Find all close matches of input string from a list
Python program to find uncommon words from two Strings
Python | Swap commas and dots in a String
Python | Permutation of a given string using inbuilt function
Python | Check for URL in a String
Execute a String of Code in Python
Advance String Programs
Python | Convert numeric words to numbers
Python | Word location in String
Python | Consecutive characters frequency
String slicing in Python to rotate a string
String slicing in Python to check if a string can become empty by recursive deletion
Python Program to find minimum number of rotations to obtain actual string
Python – Words Frequency in String Shorthands
Python – Successive Characters Frequency
Python – Sort String list by K character frequency
Python – Convert Snake case to Pascal case
Python – Avoid Last occurrence of delimitter
Python program to find the character position of Kth word from a list of strings
Python – Right and Left Shift characters in String
Python | Exceptional Split in String
Python – Split String on vowels
Python – Mirror Image of String
Python – Replace multiple words with K
Python – Replace Different characters in String at Once
Python | Multiple indices Replace in String
Python – Ways to remove multiple empty spaces from string List
Python | Remove punctuation from string
Python – Similar characters Strings comparison
Python – Remove K length Duplicates from String
Python – Remove suffix from string list
Python Counter| Find all duplicate characters in string
Python – Replace duplicate Occurrence in String
Ways to convert string to dictionary
Python – Check if two strings are Rotationally Equivalent
Python | Test if string is subset of another
Python Program to Generate Random binary string
Python Program to convert binary to string
Python – Reverse Sort a String
Programs on SubString
Python | Check if a Substring is Present in a Given String
Python – Substring presence in Strings List
Python – All substrings Frequency in String
Python – Maximum Consecutive Substring Occurrence
Python – Maximum occurring Substring from list
Python – Possible Substring count from String
Python – Replace all occurrences of a substring in a string
Python – Longest Substring Length of K
Python – Extract Indices of substring matches
Python | Split by repeating substring
Python | Remove substring list from String
Python – Remove after substring in String
Python | Remove Reduntant Substrings from Strings List
Python – Test substring order
Python – String till Substring
Python – Filter Strings combination of K substrings

Last Updated : 09 Dec, 2020

42

Similar Reads
1.
Python Dictionary Exercise
2.
Python Tuple Exercise
3.
Python Set Exercise
4.
Python List Exercise
5.
Matplotlib - Practice, Exercise, and Solutions
6.
Pandas and NumPy Exercise for Data Analysis
7.
Python | Sorting string using order defined by another string
8.
String Alignment in Python f-string
9.
String to Int and Int to String in Python
10.
Pad or fill a string by a variable in Python using f-string
Related Tutorials
1.
Data Analysis Tutorial
2.
Flask Tutorial
3.
Natural Language Processing (NLP) Tutorial
4.
Data Science for Beginners
5.
Data Science With Python Tutorial
Next
Python program to check whether the string is Symmetrical or Palindrome
Article Contributed By :
https://media.geeksforgeeks.org/auth/avatar.png
GeeksforGeeks
Vote for difficulty
Current difficulty : Easy
Easy
Normal
Medium
Hard
Expert
Article Tags :
Python string-programs
python-string
Python
Practice Tags :
python
Improve Article
Report Issue
Courses
course-img
105k+ interested Geeks
Complete Machine Learning & Data Science Program
Explore
course-img
11k+ interested Geeks
Python Backend Development with Django - Live
Explore
course-img
914k+ interested Geeks
Data Structures and Algorithms - Self Paced
Explore





geeksforgeeks-footer-logo
A-143, 9th Floor, Sovereign Corporate Tower, Sector-136, Noida, Uttar Pradesh - 201305
feedback@geeksforgeeks.org
Company
About Us
Careers
In Media
Contact Us
Terms and Conditions
Privacy Policy
Copyright Policy
Third-Party Copyright Notices
Advertise with us
Explore
Job Fair For Students
POTD: Revamped
Python Backend LIVE
Android App Development
DevOps LIVE
DSA in JavaScript
Languages
Python
Java
C++
PHP
GoLang
SQL
R Language
Android Tutorial
Data Structures
Array
String
Linked List
Stack
Queue
Tree
Graph
Algorithms
Sorting
Searching
Greedy
Dynamic Programming
Pattern Searching
Recursion
Backtracking
Web Development
HTML
CSS
JavaScript
Bootstrap
ReactJS
AngularJS
NodeJS
Computer Science
GATE CS Notes
Operating Systems
Computer Network
Database Management System
Software Engineering
Digital Logic Design
Engineering Maths
Python
Python Programming Examples
Django Tutorial
Python Projects
Python Tkinter
OpenCV Python Tutorial
Python Interview Question
Data Science & ML
Data Science With Python
Data Science For Beginner
Machine Learning Tutorial
Maths For Machine Learning
Pandas Tutorial
NumPy Tutorial
NLP Tutorial
Deep Learning Tutorial
DevOps
Git
AWS
Docker
Kubernetes
Azure
GCP
Competitive Programming
Top DSA for CP
Top 50 Tree Problems
Top 50 Graph Problems
Top 50 Array Problems
Top 50 String Problems
Top 50 DP Problems
Top 15 Websites for CP
System Design
What is System Design
Monolithic and Distributed SD
Scalability in SD
Databases in SD
High Level Design or HLD
Low Level Design or LLD
Top SD Interview Questions
Interview Corner
Company Preparation
Preparation for SDE
Company Interview Corner
Experienced Interview
Internship Interview
Competitive Programming
Aptitude
GfG School
CBSE Notes for Class 8
CBSE Notes for Class 9
CBSE Notes for Class 10
CBSE Notes for Class 11
CBSE Notes for Class 12
English Grammar
Commerce
Accountancy
Business Studies
Microeconomics
Macroeconomics
Statistics for Economics
Indian Economic Development
UPSC
Polity Notes
Geography Notes
History Notes
Science and Technology Notes
Economics Notes
Important Topics in Ethics
UPSC Previous Year Papers
SSC/ BANKING
SSC CGL Syllabus
SBI PO Syllabus
SBI Clerk Syllabus
IBPS PO Syllabus
IBPS Clerk Syllabus
Aptitude Questions
SSC CGL Practice Papers
Write & Earn
Write an Article
Improve an Article
Pick Topics to Write
Write Interview Experience
Internships
Video Internship
@geeksforgeeks , Some rights reserved
We use cookies to ensure you have the best browsing experience on our website. By using our site, you acknowledge that you have read and understood our Cookie Policy & Privacy Policy
Got It !
Lightbox
Please Login To Continue
Sign InSign Up
account_circle
Username or email
lock
Password
 Remember meForgot Password'''
