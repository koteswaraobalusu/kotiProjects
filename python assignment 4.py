'''i=0
while i==0:
    height=int(input('enter height in cms:'))
    weight=int(input('enter weight in kgs:'))
    height=height/100
    bmi=weight/height**2
    print(bmi)
    if bmi>=0 and bmi<=18.5:
        print('underweight')
    elif bmi>=18.5and bmi<=24.9:
        print('normal weight')
    if bmi>=25.0 and bmi<=29.9:
        print('pre obesity')
    elif bmi>=30.0and bmi<=40:
        print(' obesity')
    elif bmi>40:
        print('extreme obesity')
i=i+0'''
'''i=1
team=['kohli','dhoni','sachin','surya']
while i==1:
    team1=team
   
    a=input('enter any name:')
    if a in team1:
       print('{}is available in team'.format(a))
    else:
      print('given {} not in team thats why append '.format(a))
      team1.append(a)
    print(team1)
  
i=i+0'''
for i in range(1,129):
    print(chr(i),end=',')
    
