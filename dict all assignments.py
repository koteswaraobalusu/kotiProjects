'''employees = {
'emp1':{'name':'Sai', 'salary':20000, 'company':['TCS','Capgemini','Infosys'], 'hTown':'Hyd'},
'emp2':{'name':'Nani','salary':30000, 'company':['Wipro','NTH'], 'hTown':'Banglore'},
'emp3':{'name':'Satya','salary':40000, 'company':['NTH','Infosys','CTS'],'hTown':'Chennai'},
'emp4':{'name':'Rohit','salary':25000, 'company':['Infosys','TCS','Defteam'], 'hTown':'Pune'},
'emp5':{'name':'Mohan','salary':22000, 'company':['NTH','HCL','DeepCompute'], 'hTown':'Hyd'},
'emp6':{'name':'Sanjay','salary':45000, 'company':['Wipro','Infosys','Defteam'], 'hTown':'Mumbai'}
}

#1. Write a program to display the salary of Sai?
print([employees [i] ['salary']for i in employees if employees [i]['name']=='Sai'])
        

#2. Write a program to display the home town of Nani?
print([employees [i]['hTown']for i in employees if employees [i]['name']=='Nani'])
#3. Write a program to display employee name who is working in Pune?'
print([employees [i] ['name'] for i in employees if employees [i]['hTown']=='Pune'])
#4. Write a program to display all companies names of Satya?
print([employees [i]['company'] for i in employees if employees [i]['name']=='Satya'])
#5. Write a program to display all employees names who worked in TCS?
print([employees [i]['name'] for i in employees if 'Wipro' in  employees [i]['company']])
#6. Write a program to display all employees names who did not work in Infosys?
print([employees [i]['name']for i in employees if 'Infosys' not in  employees [i]['company']])
#7. Write a program to display all employees names?
print([employees [i]['name'] for i in employees])
#8. Write a program to display the sum of all salaries?
x=[employees [i]['salary'] for i in employees]
print(sum(x))
#9. Write a program to display the latest company of Rohit?
x=[employees [i]['company'] for i in employees if employees [i]['name']=='Rohit']
print(x[-1])
#10. Write a program to display total companies count of Satya?
print(len([employees [i]['company'] for i in employees if employees [i]['name']=='Satya']))
#11. Write a program to display the employee name who is working in HCL?
print([employees [i]['name'] for i in employees if'HCL' in employees [i]['company']])

#12. Write a program to display employees names who are working in Hyd?
print([employees [i]['name'] for i in employees if employees [i]['hTown']=='Hyd'])
#13. Write a program to display all employees whose name starts with 'S' character?
x=[employees [i]['name'] for i in employees]
print([i for i in x if i[0]=='S'])
#14. Write a program to display all employees whose name ends with vowel?
x=[employees [i]['name'] for i in employees]
print([i for i in x if i[-1] in 'aeiou'])
#15. Write a program to display the employee name who worked only in two companies?
print([employees [i]['name'] for i in employees if len(employees [i]['company'])==2])
#16. Write a program to display employee names who worked in DeepCompute?
print([employees [i]['name'] for i in employees if 'DeepCompute' in employees [i]['company']])
#17. Write a program to display the salary of Pune employee?
print([employees [i]['salary'] for i in employees if employees [i]['hTown']=='Pune'])
#18. Write a program to display the location of employee who is taking 20000 salary?
print([employees [i]['hTown'] for i in employees if employees [i]['salary']==20000])
#19. Write a program to display the salariesof Sai and Nani?
lst=['Sai','Nani']
print([employees [i]['salary'] for i in employees if employees [i]['name']in lst])
#20. Write a program to display the name and salary of Bangalore employee?
for i in employees:
   if employees [i]['hTown']=='Banglore':
       print(employees [i] ['name'])
       print(employees [i] ['salary'] )'''
'''players = {
'player1':{'name':'Sachin', 'matches':{'test':200,'odi':463},'scores':{'test':248,'odi':200},
'wickets':{'test':46, 'odi':154}, 'age':49, 'shirt':10, 'role':'top-order','location':'Bombay'},
'player2':{'name':'Kohli', 'matches':{'test':102, 'odi':262}, 'scores':{'test':254, 'odi':183},
'wickets':{'test':0, 'odi':4}, 'age':33, 'shirt':18, 'role':'top-order','location':'Delhi'},
'player3':{'name':'Rohit', 'matches':{'test':44, 'odi':231}, 'scores':{'test':212, 'odi':264},
'wickets':{'test':2, 'odi':8}, 'age':35, 'shirt':45, 'role':'opening','location':'Nagpur'},
'player4':{'name':'Sehwag','matches':{'test':104,'odi':251}, 'scores':{'test':319, 'odi':219},
'wickets':{'test':40, 'odi':96}, 'age':43, 'shirt':44, 'role':'opening', 'location':'Delhi'},
'player5':{'name':'Zaheer Khan', 'matches':{'test':92, 'odi':200}, 'scores':{'test':75, 'odi':34},
'wickets':{'test':311, 'odi':282}, 'age':43, 'shirt':41, 'role':'Bowler','location':'Bombay'}
'player6':{'name':'Dhoni', 'matches':{'test':90, 'odi':350}, 'scores':{'test':224, 'odi':183},
'wickets':{'test':0, 'odi':1}, 'age':41,'shirt':7, 'role':'keeper','location':'Ranchi'}
}'''
#Python Programs Assignment - 5

'''#1. Write a program to display all players names?
print([players [i]['name'] for i in players]) 
#2. Write a program to display ages of players?
print([players [i]['age'] for i in players])
#3. Write a program to display the youngest player name?
x=[players [i]['age'] for i in players]
print([players [i]['name'] for i in players if players[i]['age']==max(x)])
#4. Write a program to display player name who played more test matches?
x=[players [i]['matches']['test'] for i in players]
print([players [i]['name'] for i in players if players [i]['matches']['test']==max(x)])
#5. Write a program to display player name and number of test matches who has taken 0 wickets in test matches?
for i in players if players [i]['matches']'''
'''6. Write a program to display player name who has taken more wickets in ODI?
7. Write a program to display the players’ names that played highest number of ODI matches?
8. Write a program to display the player name that has highest total score of both test and ODIs?
9. Write a program to display total number of matches of Kohli?
10. Write a program to display the age of Rohit?
11. Write a program to display the total ODI scores of all players?
12. Write a program to display total number of wickets of Zaheer Khan?
13. Write a program to display all opening batsman names?
14. Write a program to display player name that shirt number is highest number?
15. Write a program to display all Bombay players?
16. Write a program to display the shirt number of Sachin?
17. Write a program to display the role of Rohit in match?
18. What is the location of the player whose shirt number is 45?
19. Write a program to display all wickets of a player whose role is bowler?
20. Write a program to count total number opening players?
21. Write a program to display Bombay opening player name?
22. Write a program to display the roles of Delhi players?
23. Write a program to display the role and location of Rohit?
24. Write a program to display total score of Bombay top-order player?
25. Write a program to display all unique roles of players?
26 Write a program to display shirt number of Delhi top-order player?
27. Write a program to display keeper name?
28. Write a program to display the shirt number of Dhoni?
29. Write a program to display players names who played less than 100 test matches?
30. Write a program to display total wickets of Ranchi player?'''

emp={'name':'koti','sal':100}
emp.update({'com':'tcs','emi':50})
print(emp)


























