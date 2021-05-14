from tkinter import*
from tkinter import ttk
import random
import sqlite3
import time
from datetime import datetime
import tkinter.messagebox

def main():
    root=Tk()
    app=Window1(root)


class Window1:
    def __init__(self,master):
        self.master=master
        self.master.title("Library Login System")
        self.master.geometry('1350x750+0+0')
        self.master.configure(bg='powder blue')
        self.frame=Frame(self.master, bg='powder blue')
        self.frame.pack()

        self.Username=StringVar()
        self.Password=StringVar()

        self.lblTitle=Label(self.frame, text='Library Login System', font=('arial',50,'bold'),bg='powder blue',fg='black')
        self.lblTitle.grid(row=0,column=0,columnspan=2,pady=40)

  #==========================================================================================================================================

        self.LoginFrame1=LabelFrame(self.frame, width=1350, height=600, font=('arial',20,'bold'),relief='ridge', bg='cadet blue',bd=20)
        self.LoginFrame1.grid(row=1, column=0)

        self.LoginFrame2=LabelFrame(self.frame, width=1000, height=600, font=('arial',20,'bold'),relief='ridge', bg='cadet blue',bd=20)
        self.LoginFrame2.grid(row=2, column=0)

  #================================================= Label & Entry===========================================================================

        self.lblUsername=Label(self.LoginFrame1, text= 'Username', font=('arial',20,'bold'), bd=22,bg='cadet blue' , fg='Cornsilk')
        self.lblUsername.grid( row=0, column=0)
        self.txtUsername=Entry(self.LoginFrame1, font=('arial',20,'bold'),textvariable=self.Username)
        self.txtUsername.grid( row=0, column=1, padx=119)

        self.lblPassword=Label(self.LoginFrame1, text= 'Password', font=('arial',20,'bold'),bd=22,bg='cadet blue' , fg='Cornsilk')
        self.lblPassword.grid( row=1, column=0)
        self.txtPassword=Entry(self.LoginFrame1, font=('arial',20,'bold'),show = "*", textvariable=self.Password)
        self.txtPassword.grid( row=1, column=1, columnspan=2, pady=30)
                                     
  #====================================================  Button==============================================================================
        self.btnLogin=Button(self.LoginFrame2, text='Login',width=17,font=('arial',20,'bold'),command=self.Login_System)
        self.btnLogin.grid(row=3,column=0,pady=20,padx=8)

        self.btnReset=Button(self.LoginFrame2, text='Reset',width=17,font=('arial',20,'bold'),command=self.Reset)
        self.btnReset.grid(row=3,column=1,pady=20,padx=8)

        self.btnExit=Button(self.LoginFrame2, text='Exit',width=17,font=('arial',20,'bold'), command=self.iExit)
        self.btnExit.grid(row=3,column=2,pady=20,padx=8)

  #===========================================================================================================================================

    def Login_System(self):
        u=(self.Username.get())
        p=(self.Password.get())

        if(u==(str("shivam")) and p==str(1234)):
            self.newWindow=Toplevel(self.master)
            self.app=Library(self.newWindow)
        else:
            tkinter.messagebox.askyesno("Login Systems", "Invalid login detail")
            self.Username.set("")
            self.Password.set("")
            self.txtUsername.focus()

    def Reset(self):
        self.Username.set("")
        self.Password.set("")
        self.txtUsername.focus()

    def iExit(self):
        self.iExit=tkinter.messagebox.askyesno("Login Systems", "Confirm if you want to exit")
        if self.iExit > 0:
            self.master.destroy()
        else:
            command=self.new_window
            return   
       

    def new_window(self):
        self.newWindow=Toplevel(self.master)
        self.app=Library(self.newWindow)
 
    

class Library:
    
    
    def __init__(self,master):
        self.master=master
        self.master.title("Library Management System")
        self.master.geometry('1350x750+0+0')
        self.master.configure(bg='cadet blue')

        MType=StringVar()
        ID=StringVar()
        Title=StringVar()
        Name=StringVar()
        FatherName=StringVar()
        Course=StringVar()
        Branch=StringVar()
        Year=StringVar()
        MobileNo=StringVar()
        BookID=StringVar()
        BookTitle=StringVar()
        BookType=StringVar()
        Author=StringVar()
        DateBorrowed=StringVar()
        DateDue=StringVar()
        SellingPrice=StringVar()
        LateReturnFine=StringVar()
        DateOverDue=StringVar()
        DaysOnLoan=StringVar()
        Prescription=StringVar()

        def iReset2():
            MType.set("")
            ID.set("")
            Title.set("")
            Name.set("")
            FatherName.set("")
            Course.set("")
            Branch.set("")
            Year.set("")
            MobileNo.set("")
            BookID.set("")
            BookTitle.set("")
            BookType.set("")
            Author.set("")
            DateBorrowed.set("")
            DateDue.set("")
            SellingPrice.set("")
            LateReturnFine.set("")
            DateOverDue.set("")
            DaysOnLoan.set("")
            self.txtFrameDetail.delete("1.0",END)
            self.txtDisplayR.delete("1.0",END)
                

        def iDelete():
            iReset2()
            self.txtDisplayR.delete("1.0",END)

        def iEliminate():
            msg=tkinter.messagebox.askyesno("Library Management System ", "Confirm if you want to exit")
            if msg=="True":
               master.quit()
                                

        def iDisplayData():
            self.txtFrameDetail.insert(END,MType.get()+"\t\t"+ID.get()+"\t"+Title.get()+"\t"+Name.get()+
                                       "\t"+ FatherName.get() +"\t \t"+Course.get()+"\t\t"+Branch.get()+"\t"+Year.get()+"\t"+BookTitle.get()+"\t\t"+
                                       DateBorrowed.get()+"\t "+DaysOnLoan.get()+ "\n")

        def insert():
            name = Name.get()
            branch = Branch.get()
            course = Course.get()
            bookID = BookTitle.get()
            bookName = BookID.get()
            conn = sqlite3.connect('library.db')
            with conn:
                cursor = conn.cursor()
                cursor.execute('INSERT INTO studentDb(Name,Branch,Course,BookID,BookName) VALUES(?,?,?,?,?)',(name,branch,course,bookID,bookName))
                db.close()
            
            

        def iReceipt():
            self.txtDisplayR.delete("1.0",END)
            self.txtDisplayR.insert(END, "Member Type: \t\t" + MType.get() + "\n")
            self.txtDisplayR.insert(END, "ID No : \t\t" + ID.get() + "\n")
            self.txtDisplayR.insert(END, "Title: \t\t" + Title.get() + "\n")
            self.txtDisplayR.insert(END, "Name: \t\t" + Name.get() + "\n")
            self.txtDisplayR.insert(END, "Father Name: \t\t" + FatherName.get() + "\n")
            self.txtDisplayR.insert(END, "Course: \t\t" + Course.get() + "\n")
            self.txtDisplayR.insert(END, "Branch : \t\t" + Branch.get() + "\n")
            self.txtDisplayR.insert(END, "Year: \t\t" + Year.get() + "\n")
            self.txtDisplayR.insert(END, "Mobile No: \t\t" + MobileNo.get() + "\n")
            self.txtDisplayR.insert(END, "Book ID: \t\t" + BookID.get() + "\n")
            self.txtDisplayR.insert(END, "Book Title: \t\t" + BookTitle.get() + "\n")
            self.txtDisplayR.insert(END, "Author: \t\t" + Author.get() + "\n")
            self.txtDisplayR.insert(END, "Date Borrowed: \t\t" + DateBorrowed.get() + "\n")
            
        
                        
    
        MainFrame=Frame(self.master)
        MainFrame.grid()

        TitleFrame = Frame(MainFrame, width=1350, padx=20, bd=20, relief=RIDGE)
        TitleFrame.pack(side=TOP)
        self.lblTitle=Label(TitleFrame, width=39 , font=("arial", 40 , "bold"),text="\t Library Management Systems \t", padx=12)
        self.lblTitle.grid()

        ButtonFrame=Frame(MainFrame, bd=20, width=1350, height=50, padx=20, relief=RIDGE)
        ButtonFrame.pack(side=BOTTOM)

        FrameDetail=Frame(MainFrame, bd=20, width=1350, height=100, padx=20, relief=RIDGE)
        FrameDetail.pack(side=BOTTOM)

        DataFrame=Frame(MainFrame, bd=20, width=1300, height=400, padx=20, relief=RIDGE)
        DataFrame.pack(side=BOTTOM)

        DataFrameLEFT=LabelFrame(DataFrame , bd=10, width=800, height=300, padx=20, relief=RIDGE, font=("arial",12,"bold"), text="Library Membership Info:",)
        DataFrameLEFT.pack(side=LEFT)

        DataFrameRIGHT=LabelFrame(DataFrame , bd=10, width=450, height=300, padx=20, relief=RIDGE, font=("arial",12,"bold"), text="Book Details:",)
        DataFrameRIGHT.pack(side=RIGHT)

        #========================= Widgets=====================================#
        self.lblMemberType = Label(DataFrameLEFT, font=("arial", 12, "bold"), text ="Member Type:", padx=2, pady=2)
        self.lblMemberType.grid(row=0, column=0, sticky=W)

        self.cboMemberType = ttk.Combobox(DataFrameLEFT, state="readonly",textvariable=MType, font=("arial", 12, "bold"), width=23)
        self.cboMemberType['value']=('', 'Student', 'Faculty', 'Admin')
        self.cboMemberType.current(0)
        self.cboMemberType.grid(row=0, column=1)
        
        self.lblBookID = Label(DataFrameLEFT, font=("arial", 12, "bold"), text ="Book Title:", padx=2, pady=2)
        self.lblBookID.grid(row=0, column=2, sticky=W)
        self.txtBookID=Entry(DataFrameLEFT, font=("arial", 12, "bold"),width=25,textvariable=BookID)
        self.txtBookID.grid(row=0,column=3)

        self.lblID = Label(DataFrameLEFT, font=("arial", 12, "bold"),text="ID:", padx=2,pady=2)
        self.lblID.grid(row=1,column=0,sticky=W)
        self.txtID=Entry(DataFrameLEFT, font=("arial", 12, "bold"),textvariable=ID, width=25)
        self.txtID.grid(row=1,column=1)

        self.lblBookTitle = Label(DataFrameLEFT, font=("arial", 12, "bold"), text="Book ID:", padx=2,pady=2)
        self.lblBookTitle.grid(row=1,column=2,sticky=W)
        self.txtBookTitle=Entry(DataFrameLEFT, font=("arial", 12, "bold"), textvariable=BookTitle,width=25)
        self.txtBookTitle.grid(row=1,column=3)

        self.lblTitle=Label(DataFrameLEFT, font= ("arial",12,"bold"), text="Title:",padx=2,pady=2)
        self.lblTitle.grid(row=2,column=0,sticky=W)
        self.cboTitle=ttk.Combobox(DataFrameLEFT,state="readonly",textvariable=Title,font=("arial",12,"bold"),width=23)
        self.cboTitle['value']=('','Er.', 'Mr.', 'Miss.', 'Mrs.', 'Dr.', 'Capt.', 'Ms.')
        self.cboTitle.current(0)
        self.cboTitle.grid(row=2,column=1)

        self.lblAuthor = Label(DataFrameLEFT, font=("arial", 12, "bold"),text="Author:", padx=2,pady=2)
        self.lblAuthor.grid(row=2,column=2,sticky=W)
        self.txtAuthor=Entry(DataFrameLEFT, font=("arial", 12, "bold"),width=25,textvariable=Author)
        self.txtAuthor.grid(row=2,column=3)


        self.lblName = Label(DataFrameLEFT, font=("arial", 12, "bold"),text="Name:", padx=2,pady=2)
        self.lblName.grid(row=3,column=0,sticky=W)
        self.txtName=Entry(DataFrameLEFT, font=("arial", 12, "bold"),width=25,textvariable=Name)
        self.txtName.grid(row=3,column=1)
        
        self.lblDateBorrowed = Label(DataFrameLEFT, font=("arial", 12, "bold"),text="Date Borrowed:", padx=2,pady=2)
        self.lblDateBorrowed.grid(row=3,column=2,sticky=W)
        self.txtDateBorrowed=Entry(DataFrameLEFT, font=("arial", 12, "bold"),width=25,textvariable=DateBorrowed)
        self.txtDateBorrowed.grid(row=3,column=3)

        self.lblFatherName = Label(DataFrameLEFT, font=("arial", 12, "bold"),text="Father Name:", padx=2,pady=2)
        self.lblFatherName.grid(row=4,column=0,sticky=W)
        self.txtFatherName=Entry(DataFrameLEFT, font=("arial", 12, "bold"),width=25,textvariable=FatherName)
        self.txtFatherName.grid(row=4,column=1)

        self.lblDateDue=Label(DataFrameLEFT, font=("arial", 12, "bold"),text="Date Due:", padx=2,pady=2)
        self.lblDateDue.grid(row=4,column=2,sticky=W)
        self.txtDateDue=Entry(DataFrameLEFT, font=("arial", 12, "bold"),width=25,textvariable=DateDue)
        self.txtDateDue.grid(row=4,column=3)

        self.lblCourse=Label(DataFrameLEFT, font=("arial", 12, "bold"),text="Course:", padx=2,pady=2)
        self.lblCourse.grid(row=5,column=0,sticky=W)
        self.txtCourse=Entry(DataFrameLEFT, font=("arial", 12, "bold"),width=25,textvariable=Course)
        self.txtCourse.grid(row=5,column=1)

        self.lblDaysOnLoan=Label(DataFrameLEFT, font=("arial", 12, "bold"),text="Days on Loan:", padx=2,pady=2)
        self.lblDaysOnLoan.grid(row=5,column=2,sticky=W)
        self.txtDaysOnLoan=Entry(DataFrameLEFT, font=("arial", 12, "bold"),width=25,textvariable=DaysOnLoan)
        self.txtDaysOnLoan.grid(row=5,column=3)
        
        self.lblBranch = Label(DataFrameLEFT, font=("arial", 12, "bold"),text="Branch:", padx=2,pady=2)
        self.lblBranch.grid(row=6,column=0,sticky=W)
        self.txtBranch=Entry(DataFrameLEFT, font=("arial", 12, "bold"),width=25,textvariable=Branch)
        self.txtBranch.grid(row=6,column=1)

        self.lblLateReturnFine=Label(DataFrameLEFT, font=("arial", 12, "bold"),text="Late Return Fine:", padx=2,pady=2)
        self.lblLateReturnFine.grid(row=6,column=2,sticky=W)
        self.txtLateReturnFine=Entry(DataFrameLEFT, font=("arial", 12, "bold"),width=25,textvariable=LateReturnFine)
        self.txtLateReturnFine.grid(row=6,column=3)

        self.lblYear=Label(DataFrameLEFT, font=("arial", 12, "bold"),text="Year:", padx=2,pady=2)
        self.lblYear.grid(row=7,column=0,sticky=W)
        self.txtYear=Entry(DataFrameLEFT, font=("arial", 12, "bold"),width=25,textvariable=Year)
        self.txtYear.grid(row=7,column=1)

        self.lblDateOverDue=Label(DataFrameLEFT, font=("arial", 12, "bold"),text="Date Over Due:", padx=2,pady=2)
        self.lblDateOverDue.grid(row=7,column=2,sticky=W)
        self.txtDateOverDue=Entry(DataFrameLEFT, font=("arial", 12, "bold"),width=25,textvariable=DateOverDue)
        self.txtDateOverDue.grid(row=7,column=3)
        
        self.lblMobileNo=Label(DataFrameLEFT, font=("arial", 12, "bold"),text="Mobile No:", padx=2,pady=2)
        self.lblMobileNo.grid(row=8,column=0,sticky=W)
        self.txtMobileNo=Entry(DataFrameLEFT, font=("arial", 12, "bold"),width=25,textvariable=MobileNo)
        self.txtMobileNo.grid(row=8,column=1)

        self.lblSellingPrice=Label(DataFrameLEFT, font=("arial", 12, "bold"),text="Book Price:", padx=2,pady=2)
        self.lblSellingPrice.grid(row=8,column=2,sticky=W)
        self.txtSellingPrice=Entry(DataFrameLEFT, font=("arial", 12, "bold"),width=25,textvariable=SellingPrice)
        self.txtSellingPrice.grid(row=8,column=3)

        
        #=========================Widgets=============================================================================#
        self.txtDisplayR=Text(DataFrameRIGHT, font=("arial", 12, "bold"),width=32, height=13, padx=8,pady=20)
        self.txtDisplayR.grid(row=0, column=2)


        scrollbar=Scrollbar(DataFrameRIGHT)
        scrollbar.grid(row=0,column=1,sticky='ns')

        


        ListOfBooks = ['Math-3','Operating system','Software Engineering','Data Structure',"Let's C", 'Database Management system','Discrete Structures & Theory of Logic','DATAWAREHOUSING & DATA MINING',
                       'Computer Organization and  Architecture','Theory of Automata and Formal Languages','CYBER SECURITY','Design and Analysis of Algorithm', 'Principles of Programming Languages','WEB TECHNOLOGIES', 'Computer Networks']
        ListOfBooks.sort()
        
        db = sqlite3.connect('library.db')
        cursor = db.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS LibraryDb(Book_Title)")
        cursor.execute("CREATE TABLE IF NOT EXISTS studentDb(Name,Branch,Course,BookID,BookName)")
        db.commit()



        def SelectedBook(event):
            value=str(booklist.get(booklist.curselection()))
            w=value
            
            conn=sqlite3.connect('library.db')
            c=conn.cursor()
            c.execute('''insert into LibraryDb(Book_Title) values(?)''' ,(w,))
            
            c.execute('''SELECT * FROM LibraryDb WHERE Book_Title =?''' ,(w,))
            conn.commit()
            for row in c.fetchall():
                BookID.set(row[0])
                BookTitle.set(row[1])
                Author.set(row[2])
                LateReturnFine.set(row[3])
                SellingPrice.set(row[4])
                DaysOnLoan.set(14)
                
                import datetime

                d1=datetime.date.today()
                d2=datetime.timedelta(14)
                d3=d1+d2
                DateBorrowed.set(d1)
                DateDue.set(d3)
                DateOverDue.set("No")
                
             

        booklist= Listbox(DataFrameRIGHT, width=20,height=12,font=('arial',12,'bold'),yscrollcommand=scrollbar.set)
        booklist.bind('<<ListboxSelect>>',SelectedBook)
        booklist.grid(row=0, column=0,padx=8)
        scrollbar.config(command=booklist.yview)

        
        for items in ListOfBooks:
            booklist.insert(END,items)

        #=========================Labels==============================================================================#
        self.lblLabel=Label(FrameDetail, font=("arial",10,'bold'), pady=8,
        text="Member Type\t ID.\t Title\t Name\t Father Name\t Course\t Branch\
        \t Year\t Book Title\t Date Borrowed\t Days on Loan",)
        self.lblLabel.grid(row=0, column=0)

        self.txtFrameDetail=Text(FrameDetail,font=('arial',12,'bold'),width=121,height=4,padx=2, pady=4)
        self.txtFrameDetail.grid(row=1,column=0)
        
        #=========================Buttons=============================================================================#        
        self.btnDisplayData=Button(ButtonFrame, text='Display Data', font=('arial',12,'bold'),width=20, bd=4,command=iDisplayData)
        self.btnDisplayData.grid(row=0,column=1)

        self.btnDelete=Button(ButtonFrame, text='Delete', font=('arial',12,'bold'),width=20, bd=4,command=iDelete)
        self.btnDelete.grid(row=0,column=3)

        self.btnReset1=Button(ButtonFrame, text='Reset', font=('arial',12,'bold'),width=20, bd=4, command=iReset2)
        self.btnReset1.grid(row=0,column=4)

        self.btnExit1=Button(ButtonFrame, text='Exit', font=('arial',12,'bold'),width=20, bd=4, command=iEliminate)
        self.btnExit1.grid(row=0,column=5)

        self.btnSubmit=Button(ButtonFrame, text='Submit', font=('arial',12,'bold'),width=20, bd=4, command=iReceipt)
        self.btnSubmit.grid(row=0,column=0)

        self.btnSubmit=Button(ButtonFrame, text='Save', font=('arial',12,'bold'),width=10, bd=4, command=insert)
        self.btnSubmit.grid(row=0,column=2)



           
        #======================Frames==========================================#
        
        
        
if __name__=="__main__":
    main()

    

