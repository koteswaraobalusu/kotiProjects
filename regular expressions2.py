'''#1 to find all numbers in string
import re
a=input('enter a string:')
m=re.findall('\d+',a)
print(m)'''
'''#2 find all words in string
import re
a=input('enter a string:')
m=re.findall('\w+',a)
print(m)'''

'''import re
 
s = 'GeeksforGeeks: A computer science portal for geeks'
 
match = re.search('p', s)
 
print('Start Index:', match.start())
print('End Index:', match.end())'''
'''import re
 
string = "Hello World!"
pattern="hello$"
 
match = re.search(pattern, string)
if match:
    print("Match found!")
else:
    print("Match not found.")'''
'''import re
 
string = "The quick brown!fox jumps over the lazy dog."
pattern = "[A-Za-z]"
 
match = re.findall(pattern, string)
print(match)
if match:
    print("Match found!")
else:
    print("Match not found.")'''


