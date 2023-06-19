'''from tkinter import*
top=Tk()
top=mainloop()'''
'''from tkinter import*
parent=Tk()
redbutton=Button(parent,text='Red',fg='red',bg='blue')
redbutton.pack(fill='y',expand='true',side=LEFT)
parent=mainloop()'''
'''from tkinter import *  
parent = Tk()  
name = Label(parent,text = "Name").grid(row = 0, column = 0)  
e1 = Entry(parent).grid(row = 0, column = 1,sticky=W)  
password = Label(parent,text = "Password").grid(row = 1, column = 0)  
e2 = Entry(parent).grid(row = 1, column = 1)  
submit = Button(parent, text = "Submit").grid(row = 4, column = 0)  
parent.mainloop()  '''
'''from tkinter import*
class koti:
    def __init__(self,root):
        self.root=root
        self.root.title('my project')
        self.root.geometry('1300x800')
        labelname=Label(self.root,text='Narayana Tech House',font=('Cooper Black',40),bg='blue',relief=RAISED,bd=4)
        labelname.pack(fill='x')
        #creating frames
        createframe1=Frame(self.root,bg='pink')
        createframe1.place(x=10,y=80,width=650,height=700)
        createframe2=Frame(self.root,bg='pink')
        createframe2.place(x=670,y=80,width=850,height=700)
        #work on frame 1
        label1=Label(createframe1,text='Data Entry HERE!!',font=('Arial Black',20),bg='green',fg='white',bd=4,relief=RAISED)
        label1.pack()
        a1=Label(createframe1,text='Roll No:',font=('Arial Black',20),bg='yellow',fg='white')
        a1.grid(padx=15,row=1,column=0)
        
        

root=Tk()
obj=koti(root)'''
'''from tkinter import*
class koti:
    def __init__(self,root):
        self.root=root
        root.title('my project')
        root.geometry('1600x800')
        label1=Label(self.root,text='b.koteswara rao',font=('Cascadia Mono SemiBold',50),fg='pink',bg='black',bd=10,anchor=N,cursor='Arrow Cursor')
        label1.place(x=200,y=100)
        label1.pack(fill='x')
        #creating frames
        frame1=Frame(self.root,bg='pink')
        frame1.place(x=10,y=115,width=650,height=665)
        frame2=Frame(self.root,bg='black')
        frame2.place(x=670,y=115,width=855,height=665)
        #work on frame1
        a=Label(frame1,text='Data Entry Here!!!',font=('Century',20),bd=4,relief=GROOVE,bg='red')
        a.grid(row=0)
        b=Label(frame1,text='Roll No:',font=('Century',20),bd=4,relief=GROOVE,bg='red')
        b.grid(row=0,column=0)
        b1=Entry(frame1,font=('Century',20),bd=4,relief=GROOVE,bg='red')
        b1.grid(row=1,column=0,sticky='w')
        
root=Tk()
obj=koti(root)'''
'''#1 creating a window
from tkinter import*
class koti:
    def __init__(self,root):
        self.root=root
        self.root.geometry('1560x800+20+20')#window size
        #creating frames
        frame1=Frame(self.root,bg='pink')
        frame1.place(x=10,y=5,height=50,width=1510)
        
root=Tk()
k=koti(root)'''















from tkinter import *

class studentsinfo:
    def _init_(self,root):
        self.root=root
        self.root.geometry('1550x800')

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
        rollnobl.grid(row=1,column=0,padx=10,sticky='w')

        rollnobEntry= Entry(formFrame,font=('Arial Black',15))
        rollnobEntry.grid(row=1,column=1,sticky='E')

       #Fast Name
        
        fnamelb1= Label(formFrame,text='First Name:',font=('Arial Black',15),bg='blue',fg='yellow')
        fnamelb1.grid(row=2,column=0, padx=10,sticky='w')

        fnameEntry= Entry(formFrame,font=('Arial Black',15))
        fnameEntry.grid(row=2,column=1,sticky='E')

       #Last Name

        fnamelb1= Label(formFrame,text='Last Name:',font=('Arial Black',15),bg='blue',fg='yellow')
        fnamelb1.grid(row=3,column=0, padx=10,sticky='w')

        fnameEntry= Entry(formFrame,font=('Arial Black',15))
        fnameEntry.grid(row=3,column=1,sticky='E')

       # Email iD

        elb1= Label(formFrame,text='Email Id:',font=('Arial Black',15),bg='blue',fg='yellow')
        elb1.grid(row=4,column=0, padx=10,sticky='w')

        eEntry= Entry(formFrame,font=('Arial Black',15))
        eEntry.grid(row=4,column=1,sticky='E')

       # Mobile No

        Mnolb1= Label(formFrame,text='Mobile No:',font=('Arial Black',15),bg='blue',fg='Yellow')
        Mnolb1.grid(row=5,column=0, padx=10,sticky='w')

        MnoEntry= Entry(formFrame,font=('Arial Black',15))
        MnoEntry.grid(row=5,column=1,sticky='E')

       # Course Name

        clb1= Label(formFrame,text='Course Name :',font=('Arial Black',15),bg='blue',fg='Yellow')
        clb1.grid(row=6,column=0, padx=10,sticky='w')

        cEntry= Entry(formFrame,font=('Arial Black',15))
        cEntry.grid(row=6,column=1,sticky='E')


       # Fee

        flb1= Label(formFrame,text='Fee :',font=('Arial Black',15),bg='blue',fg='yellow')
        flb1.grid(row=7,column=0, padx=10,sticky='w')
 
        fEntry= Entry(formFrame,font=('Arial Black',15))
        fEntry.grid(row=7,column=1,sticky='E')


       # Institute
       
        inlb1= Label(formFrame,text='Institute :',font=('Arial Black',15),bg='blue',fg='yellow')
        inlb1.grid(row=8,column=0, padx=10,sticky='w')

        inEntry= Entry(formFrame,font=('Arial Black',15))
        inEntry.grid(row=8,column=1,sticky='E')

       
       #location
        
        loclb1= Label(formFrame,text='Location :',font=('Arial Black',15),bg='blue',fg='yellow')
        loclb1.grid(row=9,column=0, padx=10,sticky='w')

        locEntry= Entry(formFrame,font=('Arial Black',15))
        locEntry.grid(row=9,column=1,sticky='E')


        #Create btnFrame
        btnFrame= Frame(formFrame,bd=10,relief=RAISED,bg='Black')
        btnFrame.place(x=15,y=420,width=470,height=120)

        #Create Buttoms
        addBtn=Button(btnFrame, text='Add',font=('Arial Black',15),bg='yellow',fg='blue')
        addBtn.grid(row=0,column=0, padx=10,pady=25)

        deleteBtn=Button(btnFrame, text='Delete',font=('Arial Black',15),bg='yellow',fg='red')
        deleteBtn.grid(row=0,column=1, padx=10,pady=25)
        
        updateBtn=Button(btnFrame, text='Update',font=('Arial Black',15),bg='yellow',fg='black')
        updateBtn.grid(row=0,column=2, padx=10,pady=25)
        
        clareBtn=Button(btnFrame, text='Click me',font=('Arial Black',15),bg='yellow',fg='purple')
        clareBtn.grid(row=0,column=3, padx=10,pady=25)

        #Creating Display Form

        displayFrame= Frame(self.root,bg='blue')
        displayFrame.place(x=520,y=100,width=1000,height=680)


        #Working with Display form
        
        title1= Label(displayFrame,text='Data Display Here!!!',font=('Arial Black',20),bd=10,relief=RAISED,bg='blue',fg='yellow')
        title1.grid(row=0,columnspan=2,padx=250,pady=20)

root=Tk()
obj=studentsinfo(root)
     
        


