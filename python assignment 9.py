movies = { 
 'actors':{ 
 'prabhas':{'knownAs':'Darling', 'awards':{'nandi':1, 'cinemaa':1, 'siima':1},'remuneration':100, 'hits':{'industry':2, 'super':3,'flops':8}, 'age':41, 'height':6.1, 'mStatus':'single','sRate':'35%'}, 
 'mahesh':{'knownAs':'Prince','awards':{'nandi':8, 'cinemaa':3, 'siima':3},'remuneration':50, 'hits':{'industry':2, 'super':6,'flops':11},'age':46, 'height':6.2, 'mStatus':'married','sRate':'46%'}, 
 'ramcharan':{'knownAs':'Mega Power Star', 'awards':{'nandi':2, 'cinemaa':1, 'siima':1},  'remuneration':70, 'hits':{'industry':3, 'super':1,'flops':5}, 'age':36, 'height':5.9, 'mStatus':'married', 'sRate':'50%'},
 'ntr':{'knownAs':'Jr NTR', 'awards':{'nandi':2, 'cinemaa':5, 'siima':3}, 'remuneration':70, 'hits':{'industry':1, 'super':7,'flops':11}, 'age':36, 'height':5.9, 'mStatus':'married','sRate':'40%'}, 
 'pavan':{'knownAs':'Power Star', 'awards':{'nandi':2, 'cinemaa':2, 'siima':5}, 'hits':{'industry':2,  'super':7,'flops':16}, 'age':48, 'height':5.9, 'mStatus':'married','sRate':'37%','remuneration':50}, 
 }, 
 'actress':{ 
'tamanna':{'knownAs':'Milky Beauty', 'awards':{'nandi':0, 'cinemaa':1, 'siima':1},  
'remuneration':10, 'hits':{'industry':1, 'super':7,'flops':11}, 'age':28, 'height':5.9, 'mStatus':'single', 'sRate':'40%'}, 
 'rashmika':{'knownAs':'Butter Milky Beauty', 'awards':{'nandi':0, 'cinemaa':0, 'siima':2},  'remuneration':12,'hits':{'industry':0, 'super':4,'flops':2}, 'age':36, 'height':5.9, 'mStatus':'single', 'sRate':'30%'},
 'saipallavi':{'knownAs':'Laughing Queen','awards':{'nandi':0, 'cinemaa':0, 'siima':2},  'remuneration':8, 'hits':{'industry':0, 'super':3,'flops':0}, 'age':28, 'height':5.9,'mStatus':'single', 'sRate':'60%'}, 
 'samantha':{'knownAs':'Sam', 'awards':{'nandi':2, 'cinemaa':3, 'siima':5},'remuneration':15, 'hits':{'industry':3, 'super':7,'flops':4}, 'age':33, 'height':5.9,'mStatus':'married','sRate':'70%'}, 
 'kajal':{'knownAs':'Kaj', 'awards':{'nandi':0, 'cinemaa':2, 'siima':2},'remuneration':12, 'hits':{'industry':1, 'super':6,'flops':8}, 'age':35, 'height':5.9, 'mStatus':'married','sRate':'60%'}, 
 } 
} 
#1. Write a program to display all actors names
for i in movies:
     if i=='actors':
         for j in movies [i]:
             print(j)
#2. Write a program to display all actress names
for i in movies:
    if i=='actress':
        for j in movies [i]:
            print(j)
#3. Who is Darling?
for i in movies:
    if i=='actors':
        for j in movies[i]:
               if movies[i][j]['knownAs']=='Darling':
                   print(j)
#4. What are the total number of Nandi Awards won by actors?
x=[]
for i in movies:
    if i=='actors':
        for j in movies[i]:
            x.append(movies[i][j]['awards']['nandi'])
print(sum(x))
#5. What is the name of Prince?
for i in movies:
    if i=='actors':
        for j in movies[i]:
            if movies[i][j]['knownAs']=='Prince':
                print(j)
#6. What are the total number of awards own by Ram Charan?
for i in movies:
    if i=='actors':
        for j in movies[i]:
            if j=='ramcharan':
                print(sum(movies[i][j]['awards'].values()))
                                
#7. Which actor won more number of Nandi Awards?
x=[]
for i in movies:
    if i=='actors':
        for j in movies[i]:
            x.append(movies[i][j]['awards']['nandi'])
print(max(x))
for i in movies:
    if i=='actors':
        for j in movies[i]:
            if movies[i][j]['awards']['nandi']==max(x):
                print(j)
                
#8. What is the success rate of Prince?
for i in movies:
    if i=='actors':
        for j in movies[i]:
            if movies[i][j]['knownAs']=='Prince':
                print(movies[i][j]['sRate'])
#9. Which artist has more number of Hits?
x=[]
for i in movies:
    if i=='actors':
        for j in movies[i]:
            x.append(sum(movies[i][j]['hits'].values()))
for i in movies:
    if i=='actress':
        for j in movies[i]:
            x.append(sum(movies[i][j]['hits'].values()))
for i in movies:
    if i=='actors'or'actress':
        for j in movies[i]:
            if sum(movies[i][j]['hits'].values())==max(x):
                print(j)
    
#10. Who is Milky Beauty?
for i in movies:
    if i=='actress':
        for j in movies[i]:
            if movies[i][j]['knownAs']=='Milky Beauty':
                print(j)
#11. What is the nick name of Rashmika?
for i in movies:
    if i=='actress':
        for j in movies[i]:
            if j=='rashmika':
                print(movies[i][j]['knownAs'])
#12. What are actress names who did not win at least one Nandi Award?
for i in movies:
    if i=='actress':
        for j in movies[i]:
            if movies[i][j]['awards']['nandi']==0:
                print(j)
#13. What are the total number of SIIMA awards won by all artists?
x=[]
for i in movies:
    if i=='actors' or 'actress':
        for j in movies[i]:
            x.append(movies[i][j]['awards']['siima'])
print(sum(x))
#14. What is the artist name who has more success rate?
x=[]
for i in movies:
    if i=='actors' or 'actress':
        for j in movies[i]:
            x.append(movies[i][j]['sRate'])
for i in movies:
    if i=='actors' or 'actress':
        for j in movies[i]:
            if movies[i][j]['sRate']==max(x):
                print(j)

#15. What is the age of actor who has more super hit movies?
x=[]
for i in movies:
    if i=='actors' or 'actress':
        for j in movies[i]:
            x.append(movies[i][j]['hits']['super'])
for i in movies:
    if i=='actors' or 'actress':
        for j in movies[i]:
            if movies[i][j]['hits']['super']==max(x):
                print(j)

#16. What is the actress name who is married?
for i in movies:
    if i=='actress':
        for j in movies[i]:
            if movies[i][j]['mStatus']=='married':
                print(j)
#17. Who is the tallest actress?
x=[]
for i in movies:
    if i=='actress':
        for j in movies[i]:
            x.append(movies[i][j]['height'])
for i in movies:
    if i=='actress':
        for j in movies[i]:
            if movies[i][j]['height']==max(x):
                print(j)
#18. Who is the Youngest artist?
x=[]
for i in movies:
    if i=='actress'or'actress':
        for j in movies[i]:
            x.append(movies[i][j]['age'])
for i in movies:
    if i=='actress'or'actress':
        for j in movies[i]:
            if movies[i][j]['age']==min(x):
                print(j)

#19. Who are unmarried actress?
for i in movies:
    if i=='actress':
        for j in movies[i]:
            if movies[i][j]['mStatus']=='single':
                print(j)
#20. Who is smallest actress?
x=[]
for i in movies:
    if i=='actress':
        for j in movies[i]:
            x.append(movies[i][j]['height'])
for i in movies:
    if i=='actress':
        for j in movies[i]:
            if movies[i][j]['height']==min(x):
                print(j)

#21. Which actress has more Flops?
x=[]
for i in movies:
    if i=='actors' or 'actress':
        for j in movies[i]:
            x.append(movies[i][j]['hits']['flops'])
for i in movies:
    if i=='actors' or 'actress':
        for j in movies[i]:
            if movies[i][j]['hits']['flops']==max(x):
                print(j)

#22. What is the age of butter milky beauty?
for i in movies:
    if i=='actress':
        for j in movies[i]:
            if movies[i][j]['knownAs']=='Milky Beauty':
                print(movies[i][j]['age'])
#23. What are the total number of flops of all actress?
x=[]
for i in movies:
    if i=='actress':
        for j in movies[i]:
            x.append(movies[i][j]['hits']['flops'])
print(sum(x))
#24. What are the ages of Sam and Kaj?
lst=['samantha','kajal']
for i in movies:
    if i =='actress':
        for j in movies[i]:
            if j in lst:
                print(movies[i][j]['age'])
        
#25. Which actress own highest total number of Awards?
x=[]
for i in movies:
    if i=='actress':
        for j in movies[i]:
            x.append(sum(movies[i][j]['awards'].values()))
print(x)
for i in movies:
    if i=='actress':
        for j in movies[i]:
            if sum(movies[i][j]['awards'].values())==max(x):
                print(j)


#26. Who is the tallest artist?
x=[]
for i in movies:
    if i=='actors' or 'actress':
        for j in movies[i]:
            x.append(movies[i][j]['height'])
for i in movies:
    if i=='actors' or 'actress':
        for j in movies[i]:
            if movies[i][j]['height']==max(x):
                print(j)

#27. What are the total number of Industry hits of who has more Success Rate?
x=[]
for i in movies:
    if i=='actors' or 'actress':
        for j in movies[i]:
            x.append(movies[i][j]['hits']['industry'])
print(sum(x))
y=[]
for i in movies:
    if i=='actress' or 'actor':
        for j in movies[i]:
            y.append(movies[i][j]['sRate'])
for i in movies:
    if i=='actress' or 'actor':
        for j in movies[i]:
            if movies[i][j]['sRate']==max(y):
                print(j)

        

#28. What is the success rate of youngest actress?
x=[]
for i in movies:
    if i=='actress':
        for j in movies[i]:
            x.append(movies[i][j]['age'])
print(min(x))
for i in movies:
    if i=='actress':
        for j in movies[i]:
            if movies[i][j]['age']==min(x):
                print(j)

#29. Who is youngest married actress?
x=[]
for i in movies:
    if i=='actress':
        for j in movies[i]:
            if movies[i][j]['mStatus']=='married':
                x.append(movies[i][j]['age'])
print(min(x))
for i in movies:
    if i=='actress':
        for j in movies[i]:
            if movies[i][j]['mStatus']=='married':
                if movies[i][j]['age']==min(x):
                    print(j)
#30. Who is oldest unmarried actor?
x=[]
for i in movies:
    if i=='actress':
        for j in movies[i]:
            if movies[i][j]['mStatus']=='single':
                x.append(movies[i][j]['age'])
print(max(x))
for i in movies:
    if i=='actress':
        for j in movies[i]:
            if movies[i][j]['mStatus']=='single':
                if movies[i][j]['age']==max(x):
                    print(j)

#31. Who are the high successful actor and actress?
x=[]
for i in movies:
    if i=='actress' or 'actor':
        for j in movies[i]:
            x.append(movies[i][j]['sRate'])
for i in movies:
    if i=='actress':
        for j in movies[i]:
            if movies[i][j]['sRate']==max(x):
                print(j)
#32. Totally how many unmarried artists are acting in movies?
x=[]
for i in movies:
    if i=='actress'or 'actor':
        for j in movies[i]:
            if movies[i][j]['mStatus']=='single':
                print(j)
#33. Which actress is having more industry hit movies?
x=[]
for i in movies:
    if i=='actress':
        for j in movies[i]:
                x.append(movies[i][j]['hits']['industry'])
for i in movies:
    if i=='actress'or 'actor':
        for j in movies[i]:
            if movies[i][j]['hits']['industry']==max(x):
                print(j)
#34. Which actress does not have atleast one industry hit also?
x=[]
for i in movies:
    if i=='actress':
        for j in movies[i]:
                if movies[i][j]['hits']['industry']==0:
                    print(j)



#35. What are the total number of industry and super hits of tallest actress?
x=[]
for i in movies:
    if i=='actress':
        for j in movies[i]:
                x.append(movies[i][j]['height'])
for i in movies:
    if i=='actress':
        for j in movies[i]:
            if movies[i][j]['height']==max(x):
                print(movies [i][j]['hits']['industry']+movies[i][j]['hits']['industry'])

#Narayana Tech House

#+91-9010607010 www.narayanatechhouse.com
#36. Which actress is having lengthiest nick name?
x=[]
for i in movies:
    if i=='actress':
        for j in movies[i]:
                x.append(len(movies[i][j]['knownAs']))
for i in movies:
    if i=='actress':
        for j in movies[i]:
            if len(movies[i][j]['knownAs'])==max(x):
                print(j)
#37. Who are the youngest unmarried artist?
x=[]
for i in movies:
    if i=='actress'or 'actor':
        for j in movies[i]:
                x.append(movies[i][j]['age'])
for i in movies:
    if i=='actress'or 'actor':
        for j in movies[i]:
            if movies[i][j]['age']==min(x):
                print(j)
#38. What are the total number of Industry hits and Super Hits of the actress who got more SIIMA awards?
x=[]
for i in movies:
    if i=='actress':
        for j in movies[i]:
                x.append(movies[i][j]['awards']['siima'])

for i in movies:
    if i=='actress':
        for j in movies[i]:
            if movies[i][j]['awards']['siima']==max(x):
                print(movies[i][j]['hits']['industry']+movies[i][j]['hits']['super'])
#39. What are the ages of Darling and Milky Beauty?
x=['Darling''Milky Beauty']
for i in movies:
    if i=='actor'or'actress':
        for j in movies[i]:
            if movies[i][j]['knownAs']=='Darling':
                print(movies[i][j]['age'])
            elif movies[i][j]['knownAs']=='Milky Beauty':
                print(movies[i][j]['age'])
lst=['samantha','kajal']
for i in movies:
    if i =='actress':
        for j in movies[i]:
            if j in lst:
                print(movies[i][j]['age'])
        
#40. What are names of actors whose nick name contains star?
for i in movies:
    for j in movies[i]:
        if 'Star' in movies[i][j]['knownAs']:
            print(j)
#41. What is the total remuneration of all actors?
x=[]
for i in movies:
    if i=='actor'or'actress':
        for j in movies[i]:
            x.append(movies[i][j]['remuneration'])
print(sum(x))

#42. What is the remuneration of an actor who has more flops?
x=[]
for i in movies:
    if i=='actor'or'actress':
        for j in movies[i]:
            x.append(movies[i][j]['hits']['flops'])
print(x)
for i in movies:
    for j in movies[i]:
        if movies[i][j]['hits']['flops']==max(x):
             print(j)

#43. What is the highest remuneration of an unmarried actress?
x=[]
for i in movies:
    if i=='actress':
        for j in movies[i]:
            if movies[i][j]['mStatus']!='married':
                x.append(movies[i][j]['remuneration'])
print(max(x))

#44. What are the names of artists who has more remuneration?
x=[]
for i in movies:
    if i=='actor'or'actress':
        for j in movies[i]:
            x.append(movies[i][j]['remuneration'])
print(x)
for i in movies:
    for j in movies[i]:
        if movies[i][j]['remuneration']==max(x):
             print(j)


#45. What is the remuneration of high successful Actress
x=[]
for i in movies:
    if i=='actress':
        for j in movies[i]:
            x.append(movies[i][j]['sRate'])
print(max(x))
for i in movies:
    if i=='actress':
        for j in movies[i]:
            if movies[i][j]['sRate']==max(x):
                print(movies[i][j]['remuneration'])

#46. What is the remuneration of actress who has more industry hits?
x=[]
for i in movies:
    if i=='actress':
        for j in movies[i]:
            x.append(movies[i][j]['hits']['industry'])
for i in movies:
    if i=='actress':
        for j in movies[i]:
            if movies[i][j]['hits']['industry']==max(x):
                print(j)
            

#47. What are the ages of an actors whose remuneration is more then 90 crores?
for i in movies:
    if i=='actors':
        for j in movies[i]:
            if movies[i][j]['remuneration']>90:
                print(movies[i][j]['age'])
#48. What are the total number of industry hits of both Prince and Butter Milky Beauty?
lst=['Prince','Milky Beauty']
x=[]
for i in movies:
    for j in movies[i]:
        if movies[i][j]['knownAs'] in lst:
            x.append(movies[i][j]['hits']['industry'])
print(sum(x))
#49. What is the age of Laughing Queen?
for i in movies:
    for j in movies[i]:
        if movies[i][j]['knownAs']=='Laughing Queen':
            print(movies[i][j]['age'])
#50. What are the total number of awards won by an actor who has less successful rate?
x=[]
for i in movies:
    for j in movies[i]:
        x.append(movies[i][j]['sRate'])
for i in movies:
    if i=='actress':
        for j in movies[i]:
            if movies[i][j]['sRate']==min(x):
                print(sum(movies[i][j]['awards'].values()))

