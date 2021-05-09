from tkinter import*
import sqlite3
from tkinter import messagebox
def login():
    db=sqlite3.connect('login.sqlite')
    db.execute('CREATE TABLE IF NOT EXISTS login(username TEXT,password TEXT)')
    db.execute("INSERT INTO login(username,password) VALUES('admin','admin')")
    cursor=db.cursor()
    cursor.execute("SELECT * FROM login where username=? AND password=?",(userinput.get(),passinput.get()))
    row=cursor.fetchone()
    if row:
        new = Tk()
        new.geometry("1350x750+0+0")
        new.configure(background='#E2CCA3')
        # messagebox.showinfo('info', 'login success')
    else:
        messagebox.showinfo('info', 'login failed')
    cursor.connection.commit()
    db.close()
main_window=Tk()
main_window.title('login')
main_window.geometry('1350x750+0+0')
main_window.configure(background='#E2CCA3')
frame=Frame(main_window,bg='#9E7C55',width=1050,height=800)
frame.pack()

user_input=StringVar()
pass_input=StringVar()

info_label=Label(frame,text='Employee login',font=('ariel',90,'bold'),bg='#E2CCA3',fg='#423930')
info_label.grid(row=0,column=0,columnspan=8,pady=60)

LoginFrame1 = LabelFrame(frame, width=1050, height=600
                                      , font=('arial', 40, 'bold'), relief='ridge', bg='#9E7C55', bd=20)
LoginFrame1.grid(row=1, column=0,columnspan=8,pady=40)

LoginFrame2 = LabelFrame(frame, width=1050, height=600
                                      , font=('arial', 40, 'bold'), relief='ridge', bg='#9E7C55', bd=20)
LoginFrame2.grid(row=2, column=0,columnspan=8,pady=40)

info_user=Label(LoginFrame1,text='username',font='ariel,25,bold',bg='#E2CCA3',fg='#423930')
info_user.grid(row=0,column=0)
userinput=Entry(LoginFrame1,textvariable=user_input)
userinput.grid(row=0,column=4)

info_pass=Label(LoginFrame1,text='password',font='ariel,25,bold',bg='#E2CCA3',fg='#423930')
info_pass.grid(row=1,column=0)
passinput=Entry(LoginFrame1,textvariable=pass_input,show='*')
passinput.grid(row=1,column=4)

login_btn=Button(LoginFrame2,text='Login',font='ariel,15,bold',bg='#E2CCA3',fg='#423930',command=login)
login_btn.grid(row=3, column=1, pady=20, padx=20)
mainloop()

