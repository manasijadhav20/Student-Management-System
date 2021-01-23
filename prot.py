
import requests
import bs4
import socket
from tkinter import *
from tkinter import messagebox
from tkinter import scrolledtext
import sys    
import time
from PIL import Image,ImageTk  #pip install pillow
from playsound import playsound
from itertools import count

# Used Oracle 11g Database
# SQL> conn
# Enter user-name: system
# Enter password:
# Connected.
# SQL> create table student_data(rno int,name varchar(20),marks int);

# Table created.

# SQL> insert into student_data values(10,'Maeve',96);

# 1 row created.

def f14():
    root.withdraw()
    root2.deiconify()


class ImageLabel(Label):
    """a label that displays images, and plays them if they are gifs"""
    def load(self, im):
        if isinstance(im, str):
            im = Image.open(im)
        self.loc = 0
        self.frames = []

        try:
            for i in count(1):
                self.frames.append(ImageTk.PhotoImage(im.copy()))
                im.seek(i)
        except EOFError:
            pass

        try:
            self.delay = im.info['duration']
        except:
            self.delay = 100

        if len(self.frames) == 1:
            self.config(image=self.frames[0])
        else:
            self.next_frame()

    def unload(self):
        self.config(image=None)
        self.frames = None

    def next_frame(self):
        if self.frames:
            self.loc += 1
            self.loc %= len(self.frames)
            self.config(image=self.frames[self.loc])
            self.after(self.delay, self.next_frame)

root = Tk()
root.title("Welcome ")
root.geometry("1600x1000+0+0")
lbl = ImageLabel(root)
btnAdd=Button(root,text="Welcome please click here ^_^ ",font=("arial",18,"bold"),width=50,background='SkyBlue1',command=f14)
btnAdd.pack(pady=10)
lbl.pack()
lbl.place(x=0,y=0,relwidth=1,relheight=1)
lbl.load('mini.gif')



root2=Toplevel(root)  			
root2.title("S.M.S ")
root2.geometry("1600x1000+0+0")
root2.configure(bg='SkyBlue1')
root2.withdraw()
load=Image.open("img2.jpg")
load=load.resize((1350,750),Image.ANTIALIAS)
render=ImageTk.PhotoImage(load)
img=Label(root2,image=render)
img.image = render
img.place(x=0,y=0,relwidth=1,relheight=1)


def f1():
	root2.withdraw()
	addst.deiconify()

def f2():
	viewst.withdraw()
	root2.deiconify()

def f3():
	root2.withdraw()
	updatest.deiconify()

def f4():
	root2.withdraw()
	deletest.deiconify()

def f5():
	root2.withdraw()
	graphst.deiconify()

def f6():
    import cx_Oracle
    con=None
    cursor=None
    try:
        con=cx_Oracle.connect('system/abc123')
        rno=entRno.get()
        name=entName.get()
        marks=entMarks.get()
        cursor=con.cursor()
        if rno.isdigit():
            rno=int(entRno.get())
            if name.isalpha():
                if len(name) > 1:
                    name=entName.get()
                    if marks.isdigit():
                        if (int)(marks) < 101:
                            marks=int(entMarks.get())
                            sql="insert into student_data values('%d','%s','%d')"
                            args=(rno,name,marks)
                            cursor.execute(sql%args)
                            con.commit()
                            msg=str(cursor.rowcount)+"record inserted"
                            messagebox.showinfo("Sahi kiya re ",msg)
                            playsound('clap.mp3')
                            entRno.delete(0,END)
                            entMarks.delete(0,END)
                            entName.delete(0,END)
                            entRno.focus()
                        else:
                            msg="Range of marks is 0-100 "
                            messagebox.showerror("Galat kiya re ",msg)
                            entMarks.delete(0,END)
                            entMarks.focus()
                    else:
                        msg="Marks should be integers"
                        messagebox.showerror("Galat kiya re",msg)
                        entMarks.delete(0,END)
                        entMarks.focus()            
                else:
                    msg="Minimum length is 2 for name"
                    messagebox.showerror("Galat kiya re ",msg)
                    entName.delete(0,END)
                    entName.focus()
            else:
                msg="Only alphabets allowed "
                messagebox.showerror("Galat kiya re ",msg)
                entName.delete(0,END)
                entName.focus() 
        else:
            msg="Roll no should be +ve integer "
            messagebox.showerror("Galat kiya re ",msg)
            entRno.focus()
            entRno.focus()        

    except cx_Oracle.DatabaseError as e:
        messagebox.showerror("Galat kiya re ",e)
        con.rollback()
    finally:
        if cursor is not None:
            cursor.close()
        if con is not None:
            con.close()                       
def f7():
	addst.withdraw()
	root2.deiconify()

def f8():
	root2.withdraw()
	viewst.deiconify()
	import cx_Oracle

	con = None
	cursor = None
	try:
		con = cx_Oracle.connect("system/abc123")
		cursor = con.cursor();stData.delete('1.0',END)
		sql="select rno,name,marks from student_data"
		cursor.execute(sql)
		data= cursor.fetchall()
		msg=""
		for d in data:
			msg = msg +"r:"+str(d[0])+" n:"+ d[1]+" m:"+str(d[2])+"\n"
		stData.insert(INSERT,msg)
	except cx_Oracle.DatabaseError as e:
		print("some issue ",e)

	finally:
		if cursor is not None:
			cursor.close()
		if con is not None:
			con.close()

def f9():
    import cx_Oracle

    con = None
    cursor = None
    try:
        con = cx_Oracle.connect("system/abc123")
        rno1=entRno1.get()
        name1=entName1.get()
        marks1=entMarks1.get()
        if rno1.isdigit():
            rno1=int(entRno1.get())
            if name1.isalpha():
                if len(name1) > 1:
                    name1=entName1.get()
                    if marks1.isdigit():
                        if int(marks1) <=100:
                            marks1=int(entMarks1.get())
                            cursor = con.cursor()
                            sql="update student_data set name='%s',marks='%d' where rno='%d' "
                            args=(name1,marks1,rno1)
                            cursor.execute(sql%args)
                            con.commit()
                            if cursor.rowcount !=0:
                                msg=str(cursor.rowcount)+ "records updated "
                                messagebox.showinfo("Sahi kiya re ",msg)
                                entRno1.delete(0,END)
                                entName1.delete(0,END)
                                entMarks1.delete(0,END)
                                entRno1.focus()
                            else:
                                msg="record does not exists"    
                                messagebox.showinfo("Galt kiya re ",msg)
                                entRno1.delete(0,END)
                                entName1.delete(0,END)
                                entMarks1.delete(0,END)
                                entRno1.focus()
                        else:
                            msg="Range of marks is 0-100 "
                            messagebox.showerror("Galat kiya re ",msg)
                            entMarks1.delete(0,END)
                            entMarks1.focus()  
                    else:
                        msg="Marks should be integers"
                        messagebox.showerror("Galat kiya re",msg)
                        entMarks1.delete(0,END)
                        entMarks1.focus()
                else:
                    msg="Minimum length is 2 for name"
                    messagebox.showerror("Galat kiya re ",msg)
                    entName1.delete(0,END)
                    entName1.focus()
            else:
                msg="Only alphabets allowed "
                messagebox.showerror("Galat kiya re ",msg)
                entName1.delete(0,END)
                entName1.focus()  
        else:
            msg="Roll no should be +ve integer "
            messagebox.showerror("Galat kiya re ",msg)
            entRno1.delete(0,END)
            entRno1.focus()    

    except cx_Oracle.DatabaseError as e:
        messagebox.showerror("Galat kiya re" , e)
        con.rollback()

    finally:
        if cursor is not None:
            cursor.close()
        if con is not None:
            con.close()


def f10():
	updatest.withdraw()
	root2.deiconify()
	
def f11():
	deletest.withdraw()
	root2.deiconify()
	
def f12():
    import cx_Oracle

    con = None
    cursor = None   
    try:
        con=cx_Oracle.connect('system/abc123')
        rno=entRno2.get()
        if rno.isdigit():
            rno=int(entRno2.get())
            cursor = con.cursor()
            sql="delete from student_data where rno='%d' "
            args=(rno)
            cursor.execute(sql%args)
            con.commit()
            if cursor.rowcount !=0:
                msg=str(cursor.rowcount)+ "record deleted "
            else:
                msg="record does not exists"    
            messagebox.showinfo("Sahi kiya re ",msg)
            entRno2.delete(0,END)
            entRno2.focus()
        else:
            msg="Please enter a +ve integer value"
            messagebox.showerror("Galat kiya re",msg)
            entRno2.focus()    
    except cx_Oracle.DatabaseError as e:
        messagebox.showerror("Galat kiya re" , e)
        con.rollback()
    finally:
        if cursor is not None:
            cursor.close()
        if con is not None:
            con.close()
# def play():
#     f=mp3play.load('clap.mp3')
#     play=lambda: f.play() #pip install mp3play

def play():
    playsound('clap.mp3')

def f13():
    import cx_Oracle
    con=None
    cursor=None
    import matplotlib.pyplot as plt
    import pandas as pd
    import numpy as np

    con=cx_Oracle.connect('system/abc123')
    cur = con.cursor()
    x=cur.execute("select name,marks from student_data where rownum < 6")
    plt.title('Student Records',color='r')
    plt.xlabel('Name',color='g')
    plt.ylabel('Marks',color='g')

    rows=cur.fetchall()
    df=pd.DataFrame([[xy for xy in x]for x in rows])

    x=df[0]
    y=df[1]
    plt.bar(x,y,color='b',alpha=0.6)
    plt.grid()
    plt.show()

    cur.close()
    con.close()


def tick():
    time_string = time.strftime('%H:%M:%S')
    clock.config(text=time_string)
    clock.after(200, tick)    

# lblTime = Label(root2,text="Time",font=("arial",18,"bold"),width=5,background='SkyBlue1').place(x=0,y=1)
clock = Label(root2, font=('times', 20, 'bold'), bg='SkyBlue1')
clock.grid(row=0, column=0) 
tick()
lblHead=Label(root2,text="----------Student Management System---------- ",font=("arial",18,"bold"),width=45,background='SkyBlue1').place(x=375,y=0)    
btnAdd=Button(root2,text="Add",font=("arial",18,"bold"),width=10,background='SkyBlue1',command=f1)
btnView=Button(root2,text="View",font=("arial",18,"bold"),width=10,background='SkyBlue1',command=f8)
btnUpdate=Button(root2,text="Update",font=("arial",18,"bold"),width=10,background='SkyBlue1',command=f3)
btnDelete=Button(root2,text="Delete",font=("arial",18,"bold"),width=10,background='SkyBlue1',command=f4)
btnGraph=Button(root2,text="Graph",font=("arial",18,"bold"),width=10,background='SkyBlue1',command=f13)
lblQuote=Label(root2,text="Quote of the day: ",font=("arial",18,"bold"),background='SkyBlue1').place(x=60,y=430)
lblQotd=Label(root2,text="Qotd: ",font=("arial",18,"italic"),wraplength= 1000,background='SkyBlue1')
res=requests.get("https://www.brainyquote.com/quotes_of_the_day.html")
soup=bs4.BeautifulSoup(res.text , 'lxml')
quote=soup.find('img' , {"class": "p-qotd"})
now=quote['alt']
lblQotd.configure(text=now)
lblTp=Label(root2,text="Temperature: ",font=("arial",18,"bold"),background='SkyBlue1').place(x=60,y=500)
lblTemp=Label(root2,text="Temp: ",font=("arial",18,"bold"),background='SkyBlue1')
lblLc=Label(root2,text="Location: ",font=("arial",18,"bold"),background='SkyBlue1').place(x=60,y=560)
lblLoc=Label(root2,text="Loc: ",font=("arial",18,"bold"),background='SkyBlue1')

cities = ['mumbai']
for city in cities:
    socket.create_connection( ("www.google.com",80) ) 
    a1 = "http://api.openweathermap.org/data/2.5/weather?units=metric"
    a2 = "&q=" +city
    a3 = "&appid=c6e315d09197cec231495138183954bd"
    api_address = a1 + a2 + a3
    res1=requests.get(api_address)
    data=res1.json()
    main=data['main']
    now=main['temp']
    lblTemp.configure(text=str(now) +"\u00B0C")
    lblLoc.configure(text=city)

clock.pack(anchor = W)
#lblHead.pack(pady=5)
btnAdd.pack(pady=10)
btnView.pack(pady=10)
btnUpdate.pack(pady=10)
btnDelete.pack(pady=10)
btnGraph.pack(pady=10)
lblQotd.pack(pady=35)
lblTemp.pack(pady=5)
lblLoc.pack(pady=10)
#----------------------------------------------------------------------------------------------------------
addst=Toplevel(root2)
addst.title("Add S")
addst.geometry("1600x1000+0+0")
addst.configure(bg='SkyBlue1')
addst.withdraw()
lblRno=Label(addst,text="enter rno ",font=("arial",18,"bold"))
entRno=Entry(addst,bd=5,font=("arial",18,"bold"))
lblName=Label(addst,text="enter name ",font=("arial",18,"bold"))
entName=Entry(addst,bd=5,font=("arial",18,"bold"))
lblMarks=Label(addst,text="enter marks ",font=("arial",18,"bold"))
entMarks=Entry(addst,bd=5,font=("arial",18,"bold"))
btnAddSave=Button(addst,text="Save ",font=("arial",18,"bold"),background='dark orange',command=f6)
btnAddBack=Button(addst,text="Back ",font=("arial",18,"bold"),background='dark orange',command=f7)

lblRno.pack(pady=5)
entRno.pack(pady=5)
lblName.pack(pady=5)
entName.pack(pady=5)
lblMarks.pack(pady=5)
entMarks.pack(pady=5)
btnAddSave.pack(pady=5)
btnAddBack.pack(pady=5)

#----------------------------------------------------------------------------------------------------------

viewst=Toplevel(root2)
viewst.title("View S")
viewst.geometry("1600x1000+0+0")
viewst.configure(bg='SkyBlue1')
viewst.withdraw()

stData=scrolledtext.ScrolledText(viewst,width=40,height=25)
btnViewBack=Button(viewst,text="Back ",font=("arial",18,"bold"),background='dark orange',command=f2)

stData.pack(pady=15)
btnViewBack.pack(pady=10)

#-----------------------------------------------------------------------------------------------------------

updatest=Toplevel(root2)
updatest.title("Update S")
updatest.geometry("1600x1000+0+0")
updatest.configure(bg='SkyBlue1')
updatest.withdraw()
lblRno1=Label(updatest,text="enter rno ",font=("arial",18,"bold"),background='snow')
entRno1=Entry(updatest,bd=5,font=("arial",18,"bold"))
lblName1=Label(updatest,text="enter name ",font=("arial",18,"bold"),background='snow')
entName1=Entry(updatest,bd=5,font=("arial",18,"bold"))
lblMarks1=Label(updatest,text="enter marks ",font=("arial",18,"bold"),background='snow')
entMarks1=Entry(updatest,bd=5,font=("arial",18,"bold"))
btnUpdateSave=Button(updatest,text="Save ",font=("arial",18,"bold"),background='dark orange',command=f9)
btnUpdateBack=Button(updatest,text="Back ",font=("arial",18,"bold"),background='dark orange',command=f10)

lblRno1.pack(pady=5)
entRno1.pack(pady=5)
lblName1.pack(pady=5)
entName1.pack(pady=5)
lblMarks1.pack(pady=5)
entMarks1.pack(pady=5)
btnUpdateSave.pack(pady=5)
btnUpdateBack.pack(pady=5)

#----------------------------------------------------------------------------------------------------------

deletest=Toplevel(root2)
deletest.title("Delete S")
deletest.geometry("1600x1000+0+0")
deletest.configure(bg='SkyBlue1')
deletest.withdraw()
lblRno2=Label(deletest,text="enter rno ",font=("arial",18,"bold"),background='snow')
entRno2=Entry(deletest,bd=5,font=("arial",18,"bold"))
btnAddSave=Button(deletest,text="Save ",font=("arial",18,"bold"),background='dark orange',command=f12)
btnAddBack=Button(deletest,text="Back ",font=("arial",18,"bold"),background='dark orange',command=f11)

lblRno2.pack(pady=20)
entRno2.pack(pady=5)
btnAddSave.pack(pady=5)
btnAddBack.pack(pady=5)

root2.mainloop()


			



















