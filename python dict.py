employees={
    'emp1':{'name':'Sai','salary':20000,'company':['TCS','Capgemini','Infosys'],'hTown':'Hyd'},
    'emp2':{'name':'Nani','salary':30000,'company':['Wipro','NTH'],'hTown':'Banglore'},
    'emp3':{'name':'Satya','salary':40000,'company':['NTH','Infosys','CTS'],'hTown':'Chennai'},
    'emp4':{'name':'Rohit','salary':25000,'company':['Infosys','TCS','Defteam'],'hTown':'Pune'},
    'emp5':{'name':'Mohan','salary':22000,'company':['NTH','HCL','Deepcompute'],'hTown':'Hyd'},
    'emp6':{'name':'Sanjay','salary':45000,'company':['Wipro','Infosys','Defteam'],'hTown':'Mumbai'}
    }
'''
print([employees [i]['salary'] for i in employees if employees [i]['name']=='Sai'])
print([employees [i]['hTown'] for i in employees if employees [i]['name']=='Nani'])
print([employees [i]['name'] for i in employees if employees [i]['hTown']=='Pune'])
print([employees [i]['company'] for i in employees if employees [i]['name']=='Satya'])
print([employees [i]['name'] for i in employees if 'TCS' in employees [i]['company']])
print([employees [i]['name'] for i in employees if 'Infosys' not in employees [i]['company']])
print([employees [i]['name'] for i in employees])
print(sum([employees [i]['salary'] for i in employees ]))
k=[employees [i]['company'] for i in employees if employees [i]['name']=='Rohit']
print(k)
print(k[-1[-1]])
for i in employees:
    if employees [i]['name']=='Rohit':
        j=employees[i]['company']
        print(j[-1])
for i in employees:
    if employees [i]['name']=='Satya':
        j=employees[i]['company']
        print(len(j))
for i in employees:
    if 'HCL' in employees [i]['company']:
        j=employees[i]['company']
        print(j)
        if j[-1]=='HCL':
               k=employees[i]['name']
               print(k)
print([employees [i]['name'] for i in employees if employees[i]['hTown']=='Hyd'])
for i in employees:
    if 'S' in employees[i]['name']:
        j=[employees [i]['name']]
        print(j)
for i in employees:
    j=employees[i]['name']
    print(j)
'''
'''
#1write a program to display salary of sai
for i in employees:
    if employees [i] ['name']=='Sai':
        print(employees [i]['salary'])
#2write a program to display htown of nani
for i in employees:
    if employees [i]['name']=='Nani':
        print(employees [i]['hTown'])
#3write a program to display employees name who is working in pune
for i in employees:
    if employees [i]['hTown']=='Pune':
        print(employees [i]['name'])
#4write a program to display all companies of satya
for i in employees:
    if employees [i]['name']=='Satya':
        print(employees [i]['company'])
#5write a program to display all employees names who is worked in tcs
for i in employees:
    if 'TCS' in employees [i]['company']:
        print(employees [i]['name'])
#write a program to display employees names who is not working in infosys
for i in employees:
    if 'Infosys' not in employees[i] ['company']:
        print(employees [i]['name'])
#7 write a program to display employees names
for i in employees:
    print(employees[i]['name'])
#write a program to display sum of all salaries
print(sum([employees [i]['salary'] for i in employees]))
#9 write a program to display the latest company of rohit
for i in employees:
    if employees [i]['name']=='Rohit':
        j=employees [i]['company']
        print(j[-1])'''
'''
#10 write a program to display total companies count of satya
for i in employees:
    if employees [i]['name']=='Satya':
        j=employees [i]['company']
        print(len(j))
'''
'''
#11 write a program to display the employees name who is working in hcl
for i in employees:
    if 'HCL' in employees [i]['company']:
        j=employees [i]['company']
        print(j)
        if j[-1]=='HCL':
            print(employees[i]['name'])
            '''
'''
#12write a program to display employee name who are working in hyd
for i in employees:
    if employees [i]['hTown']=='Hyd':
        print(employees [i]['name'])
#13write a program to display all employees whose name starts with 's' character
for i in employees:
    if employees [i]['name'][0]=='S':
        print(employees [i]['name'])
#14 write a program to display all employees whose name ends with vowel
for i in employees:
    if employees[i]['name'][-1] in 'aeiouAEIOU':
        print(employees [i]['name'])
# write a program to display employee name who worked only in two companies
''''''for i in employees:
    if len(employees[i]['company'])==2:
        print(employees [i]['name'])'''
#16 write a program to display names who worked in deepcompute
'''for i in employees:
    if  'Deepcompute' in employees [i]['company']:
        j=employees [i]['name']
        print(j)
#17 write a program to display salary of pune employee
for i in employees:
    if employees [i]['hTown']=='Pune':
        print(employees[i]['salary'])
#18 write a program display the location of employee who is taking 20000 salary
for i in employees:
    if employees [i]['salary']==20000:
        print(employees[i]['name'])
'''
'''
#19 write a program to display the salaries of sai and nani
lst=['Sai','Nani']
for i in employees:
    if employees [i]['name']in lst:
        print(employees [i]['salary'])'''
#20 write a program to display the name and salary of banglore employee
for i in employees:
    if employees [i]['hTown']=='Banglore':
        print(employees [i]['name'])
        print(employees [i]['salary'])
        
        
                            
           
        






















        

    
        

















               





     

     
     

    
