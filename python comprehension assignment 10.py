#1. Write a program to fetch all data from the file.
print(open('assign10.txt','r').read())
#2. Write a program to read the first line from the file.
print(open('assign10.txt','r').readline())

#3. Write a program to read the last line from the file.
print(open('assign10.txt','r').readlines()[-1])

#4. Write a program to read the 3rd line from file
print(open('assign10.txt','r').readlines()[2])

#5. Write a program to count total number of characters in the file?
print(len(open('assign10.txt','r').read()))


#6. Write a program to count total number of commas in the file?
print(open('assign10.txt','r').read().count('a'))

#7. Write a program to count total number of words in the first line?
print(len([i for i in open('assign10.txt','r').readline().split(',')]))
#8. Write a program to count total number of lines in the file?
print(len(open('assign10.txt','r').readlines()))

#9. Write a program to count total number of 'Sai' name in the file?
print(open('assign10.txt','r').read().replace('\n',',').split(',').count('Sai'))

#10. Write a program to fetch the first word from each line in the file?
print([i.split(',')[0] for i in open('assign10.txt','r').read().split('\n')])

#11. Write a program to fetch the last word from each line?
print([i.split(',')[-1] for i in open('assign10.txt','r').read().split('\n')])


#12. Write a program to fetch all words which starts with 'a' Character?
print([i for i in open('assign10.txt','r').read().replace('\n',',').split(',') if i[0]=='A'])


#13. Write a program to fetch all words which ends with an vowel?
print([i for i in open('assign10.txt','r').read().replace('\n',',').split(',') if i[-1] in 'aeiou'])


#14. Write a program to fetch all words which has either 'a' or 'i' characters in the file?
print([i for i in open('assign10.txt','r').read().replace('\n',',').split(',') if i[0] in 'aAiI'])


#15. Write a program to fetch all words which contains only 5 characters in the file?
print([i for i in open('assign10.txt','r').read().replace('\n',',').split(',') if len(i)==5])

#16. Write a program to fetch all words which does not contains vowels except i in the file?
print([i for i in open('assign10.txt','r').read().replace('\n',',').split(',') if 'i' in i or 'I' in i])


#17. Write a program to fetch all words which ends with uppercase character in the file?
print([i for i in open('assign10.txt','r').read().replace('\n',',').split(',') if i[-1].isupper()])

#18. Write a program to count total number of characters in the file excluding commas and \ns?
print(len(open('assign10.txt','r').read().replace('\n','').replace(',','')))



#19. Write a program to count total number of words in the entire file?
print(len([i for i in open('assign10.txt','r').read().replace('\n',',').split(',')]))

#20. Write a program to fetch all even number words from from every line the file?
x=open('assign10.txt','r').read().replace('\n',',').split(',') 
print([i for i in x if x.index(i)%2==0])

#21. Write a program to fetch all words which ends with 'bha' in the file?
print([i for i in open('assign10.txt','r').read().replace('\n',',').split(',') if i.endswith('bha')])


#22. Write a program to display all TCS employees?
x=open('assign10.txt','r').read().split('\n')
print([i.split(',')[1:-1] for i in x if 'TCS' in i])

#23. Write a program to display the company name of Chinna Employee?
x=open('assign10.txt','r').read().split('\n')
print([i.split(',')[0] for i in x if 'Chinna' in i])


#24. Write a program to fetch the 2nd word from 3rd line in the file?
x=open('assign10.txt','r').read().split('\n')
print([i.split(',')[1] for i in x if x.index(i)==2])



#25. Write a program to fetch the first character from each word in the 3rd line?
x=open('assign10.txt','r').read().split('\n')[2]
print([i[0] for i in x.split(',') ])


#26. Write a program to fetch first and last character of each word in the last line?
x=open('assign10.txt','r').read().split('\n')[-1]
print([i[0]+i[-1] for i in x.split(',') ])


#27. Write a program to fetch all characters(except 1st and last chars) of each word in the 2nd line?
x=open('assign10.txt','r').read().split('\n')[1]
print([i[1:-1] for i in x.split(',') ])


#28. Write a program to count total number of words which starts with 'S' character?
print(len([i for i in open('assign10.txt','r').read().replace('\n',',').split(',') if i[0].startswith('S')]))


#29. Write a program to fetch all duplicate names in the file?
x=open('assign10.txt','r').read().replace('\n',',').split(',')
print(set([i for i in x if x.count(i)>=2]))


#30. Write a program to count all vowels in the file? (Note: output must be in dict)
v='AEIOUaeiou'
d={}.fromkeys(v,0)
for i in open('assign10.txt','r').read():
    if i in v:
        d[i]=d[i]+1
print(sum(d.values()))
'''31. Write a program to reverse all words in the file?
32. Write a program to fetch all words which contains two or more then 'a' characters?
33. Write a program to fetch all words which starts and ends with 'a' character?
34. Write a program to fetch word which has more number of 'a' characters?
35. Write a program to fetch all company names which starts with vowel?
36. Write a program to display company name which contains Saroj Employee?
37. Write a program to count all words which starts and ends with consonants?
38. Write a program to fetch all company names which does not contain Venkat employee?
39. Write a program to display company name where Narayana is working?
40. Write a program to display the first word and last word from each line in dict format?
41. Write a program to fetch all names whose name starts with 'a' in NTH company?
42. Write a program to count total number of employees in CTS company?
43. Write a program to fetch all companies where Venkat employee is working?
44. Write a program to fetch all companies names which name starts with Vowel?
45. Write a program to fetch all palindrome names from the file?
46. Write a program to fetch all companies names where palindrome named employees working?
47. Write a program to fetch the lengthiest company name?
48. Write a program to fetch the lengthiest employee name in ABC company?
49. Write a program to fetch shortest employee name in the WIPRO company?
50. Write a program count total number of employees in each company(in dict format)?'''
