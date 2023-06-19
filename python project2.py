
from tkinter import *
import pymysql
class koti:
    def __init__(self,root):
        self.root=root
        self.root.geometry('1580x800')
        self.rollno=StringVar()
        self.fname=StringVar()
        self.lname=StringVar()
        self.email=StringVar()
        self.mobile=StringVar()
        self.course=StringVar()
        self.fee=StringVar()
        self.iname=StringVar()
        self.loc=StringVar()
        #Creating Header       
        title1= Label(self.root, text='Welcome To Narayana Tech House',font=('cooper black',50),bd=4,relief=RAISED,bg='blue',fg='yellow')
        title1.pack(fill='x')
        
        #Creating Frames
        
        formFrame= Frame (self.root,bg='blue')
        formFrame.place(x=10,y=100,width=500,height=680)
        
       #working with FormFrame
        
        title2= Label(formFrame,text='Data Entry Here!!!',font=('Arial Black',20),bd=10,relief=RAISED,bg='blue',fg='yellow')
        title2.grid(row=0,columnspan=2,padx=100,pady=20)            

       #Roll No
        
        rollnobl= Label(formFrame,text='Roll No:',font=('Arial Black',15),bg='blue',fg='yellow')
        rollnobl.grid(row=1,column=0,padx=10,sticky='W')

        rollnobEntry= Entry(formFrame,font=('Arial Black',15),text=self.rollno)
        rollnobEntry.grid(row=1,column=1,sticky='E')

       #First Name
        
        fnamelb1= Label(formFrame,text='First Name:',font=('Arial Black',15),bg='blue',fg='yellow')
        fnamelb1.grid(row=2,column=0, padx=10,sticky='w')

        fnameEntry= Entry(formFrame,font=('Arial Black',15),text=self.fname)
        fnameEntry.grid(row=2,column=1,sticky='E')

       #Last Name

        fnamelb1= Label(formFrame,text='Last Name:',font=('Arial Black',15),bg='blue',fg='yellow')
        fnamelb1.grid(row=3,column=0, padx=10,sticky='w')

        fnameEntry= Entry(formFrame,font=('Arial Black',15),text=self.lname)
        fnameEntry.grid(row=3,column=1,sticky='E')

       # Email iD

        elb1= Label(formFrame,text='Email Id:',font=('Arial Black',15),bg='blue',fg='yellow')
        elb1.grid(row=4,column=0, padx=10,sticky='w')

        eEntry= Entry(formFrame,font=('Arial Black',15),text=self.email)
        eEntry.grid(row=4,column=1,sticky='E')

       # Mobile No

        Mnolb1= Label(formFrame,text='Mobile No:',font=('Arial Black',15),bg='blue',fg='Yellow')
        Mnolb1.grid(row=5,column=0, padx=10,sticky='w')

        MnoEntry= Entry(formFrame,font=('Arial Black',15),text=self.mobile)
        MnoEntry.grid(row=5,column=1,sticky='E')

       # Course Name

        clb1= Label(formFrame,text='Course Name :',font=('Arial Black',15),bg='blue',fg='Yellow')
        clb1.grid(row=6,column=0, padx=10,sticky='w')

        cEntry= Entry(formFrame,font=('Arial Black',15),text=self.course)
        cEntry.grid(row=6,column=1,sticky='E')


       # Fee

        flb1= Label(formFrame,text='Fee :',font=('Arial Black',15),bg='blue',fg='yellow')
        flb1.grid(row=7,column=0, padx=10,sticky='w')
 
        fEntry= Entry(formFrame,font=('Arial Black',15),text=self.fee)
        fEntry.grid(row=7,column=1,sticky='E')


       # Institute
       
        inlb1= Label(formFrame,text='Institute :',font=('Arial Black',15),bg='blue',fg='yellow')
        inlb1.grid(row=8,column=0, padx=10,sticky='w')

        inEntry= Entry(formFrame,font=('Arial Black',15),text=self.iname)
        inEntry.grid(row=8,column=1,sticky='E')

       
       #location
        
        loclb1= Label(formFrame,text='Location :',font=('Arial Black',15),bg='blue',fg='yellow')
        loclb1.grid(row=9,column=0, padx=10,sticky='w')

        locEntry= Entry(formFrame,font=('Arial Black',15),text=self.loc)
        locEntry.grid(row=9,column=1,sticky='E')


        #Create btnFrame
        btnFrame= Frame(formFrame,bd=10,relief=RAISED,bg='Black')
        btnFrame.place(x=15,y=420,width=470,height=120)

        #Create Buttoms
        addBtn=Button(btnFrame, text='Add',command=self.addingdata,font=('Arial Black',15),bg='yellow',fg='blue')
        addBtn.grid(row=0,column=0, padx=10,pady=25)

        deleteBtn=Button(btnFrame, text='Delete',font=('Arial Black',15),bg='yellow',fg='red')
        deleteBtn.grid(row=0,column=1, padx=10,pady=25)
        
        updateBtn=Button(btnFrame, text='Update',font=('Arial Black',15),bg='yellow',fg='black')
        updateBtn.grid(row=0,column=2, padx=10,pady=25)
        
        clareBtn=Button(btnFrame, text='Click me',command=self.clearingdata,font=('Arial Black',15),bg='yellow',fg='purple')
        clareBtn.grid(row=0,column=3, padx=10,pady=25)

        #Creating Display Form

        displayFrame= Frame(self.root,bg='blue')
        displayFrame.place(x=520,y=100,width=1000,height=680)


        #Working with Display form
        
        title1= Label(displayFrame,text='Data Display Here!!!',font=('Arial Black',20),bd=10,relief=RAISED,bg='blue',fg='yellow')
        title1.grid(row=0,columnspan=2,padx=250,pady=20)

    def addingdata(self):
        connection=pymysql.connect(host='localhost',user='root',password='root',db='project')
        c=connection.cursor()
        c.execute('insert into students values(%s,%s,%s,%s,%s,%s,%s,%s,%s)',
                 (
                     self.rollno.get(),
                     self.fname.get(),
                     self.lname.get(),
                     self.email.get(),
                     self.mobile.get(),
                     self.course.get(),
                     self.fee.get(),
                     self.iname.get(),
                     self.loc.get()
                     ))
        connection.commit()
        self.clearingdata()
        connection.close
    def clearingdata(self):
        self.rollno.set(' '),
        self.fname.set(' '),
        self.lname.set(' '),
        self.email.set(' '),
        self.mobile.set(' '),
        self.course.set(' '),
        self.fee.set(' '),
        self.iname.set(' '),
        self.loc.set(' ')
        
                    
        

root=Tk()
obj=koti(root)

