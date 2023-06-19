players = {
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
'''#1 write a program to display all player names
for i in players:
    print(players [i]['name'])
'''
'''#2 write a program to display ages of players
for i in players:
    print(players [i]['name'],end=' ')
    print(players [i]['age'],end=',')'''

'''#3 write a program to display the youngest player name
ages=[]
for i in players:
    ages.append( players [i] ['age'])
print(ages)
j=(min(ages))
print(j)
for i in players:
    if players [i]['age']==j:
        print(players [i]['name'])'''


#4
'''tests=[]
for i in players:
    tests.append(players [i]['matches']['test'])
print(tests)
j=max(tests)
print(j)
for i in players:
    if players [i]['matches']['test']==j:
      print(players [i]['name'])'''
#5
'''wickets=[]
for i in players:
    wickets.append(players [i]['wickets']['test'])
print(wickets)'''
'''for i in players:
    if players[i]['wickets']['test']==0:
        print(players [i]['name'],end='=')
        print(players [i]['matches']['test'],end=',')'''
#6
'''wickets=[]
for i in players:
    wickets.append(players [i]['wickets']['odi'])
print(wickets)
j=max(wickets)
print(j)
for i in players:
    if players[i]['wickets']['odi']==j:
        print(players [i]['name'])'''
#7
'''odis=[]
for i in players:
    odis.append(players[i]['matches']['odi'])
print(odis)
j=max(odis)
for i in players:
    if players [i]['matches']['odi']==j:
        print(players [i]['name'])'''
#8
'''scoretest=[]
scoreodi=[]
for i in players:
    scoretest.append(players[i]['scores']['test'])
    scoreodi.append(players[i]['scores']['odi'])
print(scoretest)
j=max(scoretest)
print(j)
print(scoreodi)
k=max(scoreodi)
print(k)
for i in players:
    if players [i]['scores']['test']==j:
        print(players [i]['name'])
for i in players:
        if players [i]['scores']['odi']==k:
            print(players [i]['name'])'''
       
           
#9
'''for i in players:
    if players [i]['name']=='Kohli':
        j=players [i]['matches']['test']+players [i]['matches']['odi']
        print(j)
'''
#10
'''for i in players:
    if players [i]['name']=='Rohit':
        print(players [i]['age'])'''
#11
'''j=[]
for i in players:
    print(players[i]['scores']['odi'])
    j.append(players [i]['scores']['odi'])
print(j)
print(sum(j))'''
#12
'''for i in players:
    if players [i]['name']=='Zaheer Khan':
        j=players [i]['wickets']['odi']+players [i]['wickets']['test']
        print(j)'''
#13
'''for i in players:
    if players [i]['role']=='opening':
        print(players [i]['name'])'''
'''#14
tshirt=[]
for i in players:
    tshirt.append(players[i]['shirt'])
print(tshirt)
j=max(tshirt)
for i in players:
 if players[i]['shirt']==j:
  print(players [i]['name'])'''
'''#15
for i in players:
    if players [i]['location']=='Bombay':
        print(players [i]['name'])'''
'''#16
for i in players:
    if players [i]['name']=='Sachin':
        print(players [i]['shirt'])'''
'''#17
for i in players:
    if players [i]['name']=='Rohit':
        print(players [i]['role'])'''
'''#18
for i in players:
    if players [i]['shirt']==45:
        print(players [i]['location'])'''
'''#19
for i in players:
    if players [i]['role']=='Bowler':
        print(players [i]['wickets'])'''
'''#20
j=[]
for i in players:
    if players [i]['role']=='opening':
        j.append(players [i]['name'])
print(len(j))'''
#21
for i in players:
    if players [i]['location']=='Bombay':
        if players [i]['role']=='opening':
            print(players [i]['name'])
'''#23
for i in players:
    if players [i]['name']=='Rohit':
        print(players [i]['role'])
        print(players [i]['location'])'''
'''#22
for i in players:
    if players [i]['location']=='Delhi':
        print(players [i]['role'])'''
'''#24
for i in players:
    if players [i]['location']=='Bombay':
         if players [i]['role']=='top-order':
             print(players [i]['scores']['test']+players [i]['scores']['odi'])'''
'''#25
j=[]
for i in players:
    j.append(players [i]['role'])
print(j)
k=list(set(j))
print(k)'''
'''#26
for i in players:
    if players [i]['location']=='Delhi':
        if players [i]['role']=='top-order':
            print(players [i]['shirt'])'''
'''#27
for i in players:
    if players [i]['role']=='keeper':
        print(players [i]['name'])'''
'''#28
for i in players:
    if players [i]['name']=='Dhoni':
        print(players [i]['shirt'])'''
'''#29
for i in players:
    if players [i]['matches']['test']<100:
        print(players [i]['name'])'''
'''#30
for i in players:
    if players [i]['location']=='Ranchi':
        print(players [i]['wickets']['test']+players [i]['wickets']['odi'])'''
















        














        
        








    
            
    










    

    
    







    
    
