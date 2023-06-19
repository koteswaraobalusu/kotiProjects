'''employees={'emp1':{'name':'Sai','salary':20000,'company':['TCS','Capgemini','Infosys'],'hTown':'Hyd'},
           'emp2':{'name':'Nani','salary':30000,'company':['Wipro','NTH'],'hTown':'Bangalore'},
           'emp3':{'name':'Satya','salary':40000,'company':['NTH','Infosys','CTS'],'hTown':'Chennai'},
           'emp4':{'name':'Rohit','salary':25000,'company':['Infosys','TCS','Deftteam'],'hTown':'Pune'},
           'emp5':{'name':'Mohan','salary':22000,'company':['NTH','HCL','DeapCompute'],'hTown':'Hyd'},
           'emp6':{'name':'Sanjay','salary':45000,'company':['Wipro','Infosys','Deftteam'],'hTown':'Mumbai'}
          }
print(len(employees))
#1. Write a program to display the salary of Sai?
print([employees[i]['salary'] for i in employees if employees[i]['name']=='Sai'])
print([j['salary'] for i,j in employees.items() if j['name']=='Sai'])
#2. Write a program to display the home town of Nani?
print([j['hTown'] for i,j in employees.items() if j['name']=='Nani'])
#3. Write a program to display employee name who is working in Pune?
print([j['name'] for i,j in employees.items() if j['hTown']=='Pune'])
#4. Write a program to display all companies names of Satya?
print([j['company'] for i,j in employees.items() if j['name']=='Satya'])
#5. Write a program to display all employees names who worked in TCS?
print([j['name'] for i,j in employees.items() if 'TCS' in j['company']])
#6. Write a program to display all employees names who did not work in Infosys?
print([j['name'] for i,j in employees.items() if 'Infosys' not in j['company']])
#7. Write a program to display all employees names?
print([j['name'] for i,j in employees.items()])
#8. Write a program to display the sum of all salaries?
print(sum([j['salary'] for i,j in employees.items()]))
#9. Write a program to display the latest company of Rohit?
print([j['company'][-1] for i,j in employees.items() if j['name']=='Rohit'])
#10. Write a program to display total companies count of Satya?
print([j['company']for i,j in employees.items() if j['name']=='Satya'])
#11. Write a program to display the employee name who is working in HCL?
print([j['name'] for i,j in employees.items() if 'HCL' in j['company']])
#12. Write a program to display employees names who are working in Hyd?
print([j['name'] for i,j in employees.items() if 'Hyd' in j['hTown']])
#13. Write a program to display all employees whose name starts with 'S' character?
print([j['name'] for i,j in employees.items() if j['name'].startswith('S')])
#14. Write a program to display all employees whose name ends with vowel?
print([j['name'] for i,j in employees.items() if j['name'][-1] in 'aeiouAEIOU'])
#15. Write a program to display the employee name who worked only in two companies?
print([j['name'] for i,j in employees.items() if len(j['company'])==2])
#16. Write a program to display employee names who worked in DeepCompute?
print([j['name'] for i,j in employees.items() if 'DeepCompute' in j['company']])
#17. Write a program to display the salary of Pune employee?
print([j['salary'] for i,j in employees.items() if j['hTown']=='Pune'])
#18. Write a program to display the location of employee who is taking 20000 salary?
print([j['hTown'] for i,j in employees.items() if j['salary']==20000])
#19. Write a program to display the salaries of Sai and Nani?
print([j['salary'] for i,j in employees.items() if j['name']=='Sai' or 'Nani'])
#20. Write a program to display the name and salary of Bangalore employee?
print([(j['name'],j['salary']) for i,j in employees.items()])'''
print('===========================================================================================================================================')
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
'wickets':{'test':311, 'odi':282}, 'age':43, 'shirt':41, 'role':'Bowler','location':'Bombay'},
'player6':{'name':'Dhoni', 'matches':{'test':90, 'odi':350}, 'scores':{'test':224, 'odi':183},
'wickets':{'test':0, 'odi':1}, 'age':41,'shirt':7, 'role':'keeper','location':'Ranchi'}
}
print(len(players))
#1. Write a program to display all players names?
print([j['name'] for i,j in players.items()])
#2. Write a program to display ages of players?
print([j['age'] for i,j in players.items()])
#3. Write a program to display the youngest player name?
print([j['name'] for i,j in players.items() if j['age']==min([j['age'] for i,j in players.items()])])
#4. Write a program to display player name who played more test matches?
print([j['name'] for i,j in players.items() if j['matches']['test']==max([j['matches']['test'] for i,j in players.items()])])
#5. Write a program to display player name and number of test matches who has taken 0 wickets in test matches?
print([j['name'] for i,j in players.items() if j['wickets']['test']==min([j['wickets']['test'] for i,j in players.items()])])
#6. Write a program to display player name who has taken more wickets in ODI?
print([j['name'] for i,j in players.items() if j['wickets']['odi']==min([j['wickets']['odi'] for i,j in players.items()])])
#7. Write a program to display the players’ names that played highest number of ODI matches?
print([j['name'] for i,j in players.items() if j['matches']['odi']==max([j['matches']['odi'] for i,j in players.items()])])
#8. Write a program to display the player name that has highest total score of both test and ODIs?
print([j['name'] for i,j in players.items() if j['scores']['test']==max([j['scores']['test'] for i,j in players.items()]) if j['scores']['odi']==max([j['scores']['test'] for i,j in players.items()])])
#9. Write a program to display total number of matches of Kohli?
print([j['matches']['test']+j['matches']['odi'] for i,j in players.items() if j['name']=='Kohli'])
#10. Write a program to display the age of Rohit?
print([j['age'] for i,j in players.items() if j['name']=='Rohit'])
#11. Write a program to display the total ODI scores of all players?
print(sum([j['scores']['odi'] for i,j in players.items()]))
#12. Write a program to display total number of wickets of Zaheer Khan?
print([j['wickets']['test']+j['wickets']['odi'] for i,j in players.items() if j['name']=='Zaheer Khan'])
#13. Write a program to display all opening batsman names?
print([j['name'] for i,j in players.items() if j['role']=='opening'])
#14. Write a program to display player name that shirt number is highest number?
print([j['name'] for i,j in players.items() if j['shirt']==max([j['shirt'] for i,j in players.items()])]) 
#15. Write a program to display all Bombay players?
print([j['name'] for i,j in players.items() if j['location']=='Bombay'])
#16. Write a program to display the shirt number of Sachin?
print([j['shirt'] for i,j in players.items() if j['name']=='Sachin'])
#17. Write a program to display the role of Rohit in match?
print([j['role'] for i,j in players.items() if j['name']=='Rohit'])
#18. What is the location of the player whose shirt number is 45?
print([j['location'] for i,j in players.items() if j['shirt']==45])
#19. Write a program to display all wickets of a player whose role is bowler?
print([j['wickets'] for i,j in players.items() if j['role']=='bowler'])
#20. Write a program to count total number opening players?
print(len([j['name'] for i,j in players.items() if j['role']=='opening']))
#21. Write a program to display Bombay opening player name?
print([j['name'] for i,j in players.items() if j['location']=='Bombay' and j['role']=='opening'])
#22. Write a program to display the roles of Delhi players?
print([j['role'] for i,j in players.items() if j['location']=='Delhi'])
#23. Write a program to display the role and location of Rohit?
print([(j['role'],j['location']) for i,j in players.items() if j['name']=='Rohit'])
#24. Write a program to display total score of Bombay top-order player?
print([j['scores']['test']+j['scores']['odi'] for i,j in players.items() if j['role']=='top-order' and j['location']=='Bombay'])
#25. Write a program to display all unique roles of players?
print(set([j['role'] for i,j in players.items()]))
#26 Write a program to display shirt number of Delhi top-order player?
print([j['shirt'] for i,j in players.items() if j['location']=='Delhi' and j['role']=='top-order'])
#27. Write a program to display keeper name?
print([j['name'] for i,j in players.items() if j['role']=='keeper'])
#28. Write a program to display the shirt number of Dhoni?
print([j['shirt'] for i,j in players.items() if j['name']=='Dhoni'])
#29. Write a program to display players names who played less than 100 test matches?
print([j['name'] for i,j in players.items() if j['matches']['test']<100])
#30. Write a program to display total wickets of Ranchi player?
print([j['wickets']['test']+j['wickets']['odi'] for i,j in players.items() if j['location']=='Ranchi'])'''
print('=================================================================================================================')
movies = {
'actors':{
'prabhas':{'knownAs':'Darling', 'awards':{'nandi':1, 'cinemaa':1, 'siima':1},'remuneration':100,
'hits':{'industry':2, 'super':3,'flops':8}, 'age':41, 'height':6.1, 'mStatus':'single','sRate':'35%'},
'mahesh':{'knownAs':'Prince','awards':{'nandi':8, 'cinemaa':3, 'siima':3},'remuneration':50,
'hits':{'industry':2, 'super':6,'flops':11},'age':46, 'height':6.2, 'mStatus':'married','sRate':'46%'},
'ramcharan':{'knownAs':'Mega Power Star', 'awards':{'nandi':2, 'cinemaa':1, 'siima':1},
'remuneration':70, 'hits':{'industry':3, 'super':1,'flops':5}, 'age':36, 'height':5.9, 'mStatus':'married',
'sRate':'50%'},
'ntr':{'knownAs':'Jr NTR', 'awards':{'nandi':2, 'cinemaa':5, 'siima':3}, 'remuneration':70,
'hits':{'industry':1, 'super':7,'flops':11}, 'age':36, 'height':5.9, 'mStatus':'married','sRate':'40%'},
'pavan':{'knownAs':'Power Star', 'awards':{'nandi':2, 'cinemaa':2, 'siima':5}, 'hits':{'industry':2,
'super':7,'flops':16}, 'age':48, 'height':5.9, 'mStatus':'married','sRate':'37%','remuneration':50},
},
'actress':{
'tamanna':{'knownAs':'Milky Beauty', 'awards':{'nandi':0, 'cinemaa':1, 'siima':1},
'remuneration':10, 'hits':{'industry':1, 'super':7,'flops':11}, 'age':28, 'height':5.9, 'mStatus':'single',
'sRate':'40%'},
'rashmika':{'knownAs':'Butter Milky Beauty', 'awards':{'nandi':0, 'cinemaa':0, 'siima':2},
'remuneration':12,'hits':{'industry':0, 'super':4,'flops':2}, 'age':36, 'height':5.9, 'mStatus':'single',
'sRate':'30%'},
'saipallavi':{'knownAs':'Laughing Queen', 'awards':{'nandi':0, 'cinemaa':0, 'siima':2},
'remuneration':8, 'hits':{'industry':0, 'super':3,'flops':0}, 'age':28, 'height':5.9,'mStatus':'single',
'sRate':'60%'},
'samantha':{'knownAs':'Sam', 'awards':{'nandi':2, 'cinemaa':3, 'siima':5},'remuneration':15,
'hits':{'industry':3, 'super':7,'flops':4}, 'age':33, 'height':5.9,'mStatus':'married','sRate':'70%'},
'kajal':{'knownAs':'Kaj', 'awards':{'nandi':0, 'cinemaa':2, 'siima':2},'remuneration':12,
'hits':{'industry':1, 'super':6,'flops':8}, 'age':35, 'height':5.9, 'mStatus':'married','sRate':'60%'},
}
}

#1. Write a program to display all actors names
print([j for i in movies if i=='actors' for j in movies[i]])

           
#2. Write a program to display all actress names
print([j for i in movies if i=='actress' for j in movies[i]]) 
#3. Who is Darling?
print([j for i in movies if i=='actors' or 'actress' for j in movies[i] if movies[i][j]['knownAs']=='Darling'])
#4. What are the total number of Nandi Awards won by actors?
print(sum([j['awards']['nandi'] for i,j in movies['actors'].items()]))
#5. What is the name of Prince?
print([j for i in movies for j in movies[i] if movies[i][j]['knownAs']=='Prince'])
                
    
#6. What are the total number of awards own by Ram Charan?
print([sum(movies [i][j]['awards'].values()) for i in movies if i=='actors' or 'actress' for j in movies[i] if j=='ramcharan'])
#7. Which actor won more number of Nandi Awards?
print([i for i in movies['actors'] if movies['actors'][i]['awards']['nandi']==max([movies['actors'][i]['awards']['nandi'] for i in movies['actors']])]) 
#8. What is the success rate of Prince?
print([movies[i][j]['sRate'] for i in movies if i=='actors' or 'actress' for j in movies[i] if movies[i][j]['knownAs']=='Prince'])
#9. Which artist has more number of Hits?
for i in movies:
       if i =='actors' or 'actress':
           for j in movies[i]:
                
                   
'''10. Who is Milky Beauty?
11. What is the nick name of Rashmika?
12. What are actress names who did not win at least one Nandi Award?
13. What are the total number of SIIMA awards won by all artists?
14. What is the artist name who has more success rate?
15. What is the age of actor who has more super hit movies?
16. What is the actress name who is married?
17. Who is the tallest actress?
18. Who is the Youngest artist?
19. Who are unmarried actress?
20. Who is smallest actress?
21. Which actress has more Flops?
22. What is the age of butter milky beauty?
23. What are the total number of flops of all actress?
24. What are the ages of Sam and Kaj?
25. Which actress own highest total number of Awards?
26. Who is the tallest artist?
27. What are the total number of Industry hits of who has more Success Rate?
28. What is the success rate of youngest actress?
29. Who is youngest married actress?
30. Who is oldest unmarried actor?
31. Who are the high successful actor and actress?
32. Totally how many unmarried artists are acting in movies?
33. Which actress is having more industry hit movies?
34. Which actress does not have atleast one industry hit also?
35. What are the total number of industry and super hits of tallest actress?

Narayana Tech House

+91-9010607010 www.narayanatechhouse.com
36. Which actress is having lengthiest nick name?
37. Who are the youngest unmarried artist?
38. What are the total number of Industry hits and Super Hits of the actress who got more
SIIMA awards?
39. What are the ages of Darling and Milky Beauty?
40. What are names of actors whose nick name contains star?
41. What is the total remuneration of all actors?
42. What is the remuneration of an actor who has more flops?
43. What is the highest remuneration of an unmarried actress?
44. What are the names of artists who has more remuneration?
45. What is the remuneration of high successful Actress?
46. What is the remuneration of actress who has more industry hits?
47. What are the ages of an actors whose remuneration is more then 90 crores?
48. What are the total number of industry hits of both Prince and Butter Milky Beauty?
49. What is the age of Laughing Queen?
50. What are the total number of awards won by an actor who has less successful rate?'''

