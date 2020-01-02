from tkinter import*
from tkinter import ttk
import pymysql


class admission:
    def __init__(self, root):
        self.root=root
        self.root.geometry('1200x1400')
        self.root.title('Student Admission Form')
        bg_color = '#074663'
        f1 = Frame(self.root, bg=bg_color,bd=10, relief=GROOVE)
        f1.pack(side=TOP,fill=X)
        label = Label(f1, text='STUDENT ADMISSION FORM',fg='#ffd700',bg=bg_color, font='Timesnewroman 35 bold')
        label.pack()

        #2ndframe
        self.namevalue=StringVar()
        self.fnamevalue=StringVar()
        self.mnamevalue=StringVar()
        self.rollvalue=IntVar()
        self.classvalue=IntVar()
        self.dobvalue=StringVar()
        self.addressvalue=StringVar()
        self.searchby=StringVar()
        self.searchtext=StringVar()
        self.classvalue=StringVar()

        f2 = Frame(self.root, bg=bg_color,bd=10, relief=GROOVE )
        name = Label(f2, text='NAME', fg='white', bd=5,bg=bg_color, font='Timesnewroman 20 bold')
        name.grid(row=0, column=0,sticky='w',padx=7,pady=7)
        nameentry = Entry(f2, textvar=self.namevalue, width=20, font='lucida 14')
        nameentry.grid(row=0, column=1)

        fname = Label(f2, text='FATHERS_NAME', fg='white', bd=5, bg=bg_color, font='Timesnewroman 20 bold')
        fname.grid(row=1, column=0,padx=7,pady=7)
        fnameentry = Entry(f2, textvar=self.fnamevalue, width=20, font='lucida 14')
        fnameentry.grid(row=1, column=1)

        mname = Label(f2, text='MOTHERS_NAME', fg='white', bd=5, bg=bg_color, font='Timesnewroman 20 bold')
        mname.grid(row=2, column=0,padx=7,pady=7)
        mnameentry = Entry(f2, textvar=self.mnamevalue, width=20, font='lucida 14' )
        mnameentry.grid(row=2, column=1)

        roll = Label(f2, text='ROLL_NO.', fg='white', bd=5, bg=bg_color, font='Timesnewroman 20 bold')
        roll.grid(row=3, column=0,sticky='w',padx=7,pady=7)
        rollentry = Entry(f2, textvar=self.rollvalue, width=20, font='lucida 14' )
        rollentry.grid(row=3, column=1)

        classes = Label(f2, text='CLASSES', fg='white', bd=5, bg=bg_color, font='Timesnewroman 20 bold')
        classes.grid(row=4, column=0,sticky='w',padx=7,pady=7)
        classesentry=ttk.Combobox(f2, font='lucida 14',textvar=self.classvalue, width=20)
        classesentry['values']=('Vth','VIth','VIIth','VIIIth','IXth','Xth','XIth','XIIth')
        classesentry.grid(row=4,column=1)



        dob = Label(f2, text='D.O.B', fg='white', bd=5, bg=bg_color, font='Timesnewroman 20 bold')
        dob.grid(row=5, column=0,sticky='w',padx=7,pady=7)
        dobentry = Entry(f2, textvar=self.dobvalue, width=20, font='lucida 14' )
        dobentry.grid(row=5, column=1)

        address = Label(f2, text='ADDRESS', fg='white', bd=5, bg=bg_color, font='Timesnewroman 20 bold')
        address.grid(row=6, column=0,sticky='w',padx=7,pady=7)
        addressentry = Entry(f2, textvar=self.addressvalue, width=20, font='lucida 14' )
        addressentry.grid(row=6, column=1)

        f2.place(width=600, height=600, x=0, y=76)

        # (Button)BBBBuuuuttttoooonnnnnn3rd frame##################################################################################

        f3 = Frame(f2, relief=RIDGE, bd=10)
        b1 = Button(f3, text='Delete', command=self.delete,font='lucida 14 bold',width=8, relief=RIDGE, bd=5)
        b1.grid(row=0,column=0)
        b2 = Button(f3, text='Clear', command=self.clear,font='lucida 14 bold',width=8, relief=RIDGE, bd=5)
        b2.grid(row=0, column=1)
        b3 = Button(f3, text='Add', font='lucida 14 bold',width=8,command=self.adddata, relief=RIDGE, bd=5)
        b3.grid(row=0, column=2)
        b4 = Button(f3, text='Update',command=self.update, font='lucida 14 bold',width=8, relief=RIDGE, bd=5)
        b4.grid(row=0, column=3)
        f3.place(width=470,height=65, x=50,y=500)

        #4th frame ################################################################################
        f4 = Frame(self.root,bg=bg_color,bd=10, relief=GROOVE)
        f4.place(x=610,y=76,width=754,height=600)


        search = Label(f4, text='Search by',bg=bg_color, font='Timesnewroman 20 bold',fg='white',padx=10,pady=10)
        search.grid(row=0,column=0)
        searchbox = ttk.Combobox(f4, width=8,textvar=self.searchby,font='lucida 20')
        searchbox['value']= ("rollno")
        searchbox.grid(row=0,column=1)
        searchentry = Entry(f4, width=8,textvar=self.searchtext,font='lucida 20')
        searchentry.grid(row=0,column=2,padx=7)
        b1 = Button(f4, text='Search',command=self.searchdata,font='lucida 14 bold',relief=RIDGE,bd=5,width=8,padx=7)
        b1.grid(row=0,column=3,padx=15)
        b2 = Button(f4, text='Show all', font='lucida 14 bold',command=self.fetchdata, relief=RIDGE, bd=5, width=8, padx=7)
        b2.grid(row=0, column=4, padx=15)

        # 5thframe ###############################################################################
        f5 = Frame(f4,bd=10, relief=GROOVE)
        f5.place(x=10,y=85,width=715,height=490)

        scrollx = Scrollbar(f5, orient=HORIZONTAL)
        scrolly = Scrollbar(f5, orient=VERTICAL)
        self.table = ttk.Treeview(f5, columns=( 'Name','Father_name', 'Mother_name','rollno', 'Class',  'D.O.B', 'Address'),xscrollcommand=scrollx.set, yscrollcommand=scrolly.set)
        scrollx.config(command=self.table.xview)
        scrolly.config(command=self.table.yview)
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)

        self.table.heading('Name', text='Name')
        self.table.heading('Class', text='Class')
        self.table.heading('Mother_name', text='Mother_name')
        self.table.heading('rollno', text='rollno')
        self.table.heading('Father_name', text='Father_name')
        self.table.heading('D.O.B', text='D.O.B')
        self.table.heading('Address', text='Address')
        self.table['show'] = 'headings'
        self.table.pack(fill=BOTH, expand=1)
        self.fetchdata()
        self.table.bind('<Button-1>',self.received)



    #####################Backend(work)#####################BAckend#########BAackend#################################
    def adddata(self):
        con = pymysql.connect(host='localhost',user='root',password='',database='new_admission')
        cur = con.cursor()
        cur.execute('insert into student values(%s,%s,%s,%s,%s,%s,%s)',(self.namevalue.get(),
                                                                         self.fnamevalue.get(),
                                                                         self.mnamevalue.get(),
                                                                         self.rollvalue.get(),
                                                                         self.classvalue.get(),
                                                                         self.dobvalue.get(),
                                                                         self.addressvalue.get()
                                                                         ))
        con.commit()
        self.fetchdata()
        con.close()

    def fetchdata(self):
        con = pymysql.connect(host='localhost', user='root', password='', database='new_admission')
        cur = con.cursor()
        cur.execute('select * from student')
        rows = cur.fetchall()
        if len(rows)!=0:
            self.table.delete(*self.table.get_children())
            for row in rows:
                self.table.insert('',END,values=row)
            con.commit()
        con.close()

    def received(self,event):
        cur_row=self.table.focus()
        content=self.table.item(cur_row)

        row=content['values']
        self.namevalue.set(row[0])
        self.fnamevalue.set(row[1])
        self.mnamevalue.set(row[2])
        self.rollvalue.set(row[3])
        self.classvalue.set(row[4])
        self.dobvalue.set(row[5])
        self.addressvalue.set(row[6])

    def clear(self):
        self.namevalue.set('')
        self.fnamevalue.set('')
        self.mnamevalue.set('')
        self.rollvalue.set('')
        self.classvalue.set('')
        self.dobvalue.set('')
        self.addressvalue.set('')


    def update(self):
        con = pymysql.connect(host='localhost', user='root', password='', database='new_admission')
        cur = con.cursor()
        cur.execute('update student set name=%s,fathersname=%s,mothersname=%s,classes=%s,dob=%s,address=%s where rollno=%s', (
                                                                         self.namevalue.get(),
                                                                         self.fnamevalue.get(),
                                                                         self.mnamevalue.get(),
                                                                         self.classvalue.get(),
                                                                         self.dobvalue.get(),
                                                                         self.addressvalue.get(),
                                                                         self.rollvalue.get()
                                                                         ))
        con.commit()
        self.clear()
        self.fetchdata()
        con.close()

    def delete(self):
        con = pymysql.connect(host='localhost', user='root', password='', database='new_admission')
        cur = con.cursor()
        cur.execute('delete from student where rollno=%s',self.rollvalue.get())

        con.commit()
        self.fetchdata()
        self.clear()
        con.close()

    def searchdata(self):
        con = pymysql.connect(host='localhost', user='root', password='', database='new_admission')
        cur = con.cursor()

        cur.execute("select * from student where rollno=%s", (self.searchtext.get()))
        rows = cur.fetchall()
        if len(rows) != 0:
            self.table.delete(*self.table.get_children())
            for row in rows:
                self.table.insert('', END, values=row)
            con.commit()
        con.close()


root=Tk()
x1=admission(root)
root.mainloop()