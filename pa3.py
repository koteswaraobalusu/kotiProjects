'''employees={'emp1':{'name':'Sai','salary':20000,'company':['TCS','Capgemini','Infosys'],'hTown':'Hyd'},
           'emp2':{'name':'Nani','salary':30000,'company':['Wipro','NTH'],'hTown':'Bangalore'},
           'emp3':{'name':'Satya','salary':40000,'company':['NTH','Infosys','CTS'],'hTown':'Chennai'},
           'emp4':{'name':'Rohit','salary':25000,'company':['Infosys','TCS','Deftteam'],'hTown':'Pune'},
           'emp5':{'name':'Mohan','salary':22000,'company':['NTH','HCL','DeapCompute'],'hTown':'Hyd'},
           'emp6':{'name':'Sanjay','salary':45000,'company':['Wipro','Infosys','Deftteam'],'hTown':'Mumbai'}
          }
print([employees[i]['salary']for i in employees if employees[i]['name']=='Sai'])

        
print([j['salary'] for i,j in employees.items() if j['hTown']=='Bangalore'])
print(len(employees))
print([len(j) for i,j in employees.items()])
print([j for i,j in employees.items()])
print(employees[-1]'''
emp1={'name':'Sai','salary':20000,'company':['TCS','Capgemini','Infosys'],'hTown':'Hyd'}
print(emp1[-1])


       
