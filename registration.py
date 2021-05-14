from tkinter import*
import tkinter.messagebox
import sqlite3

data = Tk()
data.title("customer resigtration and login")
data.geometry('1350x750+0+0')
data.configure(background='#E2CCA3')
frame = Frame(data, bg='#E2CCA3', bd=10, pady=10, padx=10,width=600,height=500, relief=RIDGE)
frame.place(x=300,y=100)



first_name_label=Label(frame,text="first name")
first_name_label.grid(row=0,column=0)

last_name_label=Label(frame,text="last name")
last_name_label.grid(row=1,column=0)

address_label=Label(frame,text="address")
address_label.grid(row=2,column=0)

contact_number_label=Label(frame,text="contact number")
contact_number_label.grid(row=3,column=0)

username_label=Label(frame,text="address")
username_label.grid(row=4,column=0)

password_label=Label(frame,text="address")
password_label.grid(row=5,column=0)


first_name=Entry(frame, width=30)
first_name.grid(row=0,column=1,padx=20)

last_name=Entry(frame,width=30)
last_name.grid(row=1,column=1)

address=Entry(frame,width=30)
address.grid(row=2,column=1)

contact_number=Entry(frame,width=30)
contact_number.grid(row=3,column=1)

username=Entry(frame,width=30)
username.grid(row=4,column=1)

password=Entry(frame,width=30)
password.grid(row=5,column=1)

conn = sqlite3.connect("login_information.db")
c=conn.cursor
c.execute("""CREATE TABLE informations(
            first_name text,
            last_name text,
            address text,
            contact_number integer,
            username text,
            password text
)
""")
username=StringVar()
password=StringVar()
firstname=StringVar()
lastname=StringVar()

data.mainloop()
