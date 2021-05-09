from tkinter import*
import tkinter.messagebox
from tkinter import ttk
import random
import time
import datetime

class Window1:
    def __init__(self, master):
        self.master = master
        self.master.title("restaurant login system")
        self.master.geometry('1350x750+0+0')
        self.master.configure(bg='#E2CCA3')
        self.frame = Frame(self.master, bg='#E2CCA3')
        self.frame.pack()

        self.Username = StringVar()
        self.password = StringVar()

        self.lblTitle = Label(self.frame, text='Restaurant login system', font=('arial', 50, 'bold'),
                              bg='#E2CCA3',
                              fg='black')
        self.lblTitle.grid(row=0, column=0, columnspan=2, pady=40)

        self.LoginFrame1 = LabelFrame(self.frame, width=1350, height=600
                                      , font=('arial', 20, 'bold'), relief='ridge', bg='#9E7C55', bd=20)
        self.LoginFrame1.grid(row=1, column=0)

        self.LoginFrame2 = LabelFrame(self.frame, width=1050, height=600
                                      , font=('arial', 20, 'bold'), relief='ridge', bg='#9E7C55', bd=20)
        self.LoginFrame2.grid(row=2, column=0)

        self.lblusername = Label(self.LoginFrame1, text='Username', font=('arial', 20, 'bold'), bd=22,
                                 bg='#9E7C55', fg='Cornsilk')
        self.lblusername.grid(row=0, column=0)
        self.txtusername = Entry(self.LoginFrame1, font=('arial', 20, 'bold'))
        self.txtusername.grid(row=0, column=1)

        self.lblpassword = Label(self.LoginFrame1, text='Password', font=('arial', 20, 'bold'), bd=22,
                                 bg='#9E7C55', fg='cornsilk')
        self.lblpassword.grid(row=1, column=0)
        self.txtpassword = Entry(self.LoginFrame1, font=('arial', 20, 'bold'))
        self.txtpassword.grid(row=1, column=1)

        self.btnlogin = Button(self.LoginFrame2, text="login", width=17, font=('arial', 20, 'bold'),
                               command=self.Login_System)
        self.btnlogin.grid(row=3, column=0, pady=20, padx=8)

        self.btnreset = Button(self.LoginFrame2, text="reset", width=17, font=('arial', 20, 'bold'),
                               command=self.reset)
        self.btnreset.grid(row=3, column=1, pady=20, padx=8)

        self.btnexit = Button(self.LoginFrame2, text="exit", width=17, font=('arial', 20, 'bold'),
                              command=self.iExit)
        self.btnexit.grid(row=3, column=2, pady=20, padx=8)

    def Login_System(self):
        u = (self.Username.get())
        p = (self.password.get())
        if u == 123456789 and p == 987654321:
            self.new_window = Toplevel(self.master)
            self.app = Window2(self.new_window)
        else:
            tkinter.messagebox.askyesno("login systems", "Sorry,Invalid login detail")
            self.Username.set("")
            self.password.set("")
            self.txtusername.focus()

    def reset(self):
        self.Username.set("")
        self.password.set("")
        self.txtusername.focus()

    def iExit(self):
        self.iExit = tkinter.messagebox.askyesno("Login Systems", "confirm if you want to exit")
        if self.iExit > 0:
            self.master.destroy()
        else:
            command = self.new_window
            return

    def new_window(self):
        self.new_window = Toplevel(self.master)
        self.app = Window2(self.new_window)


class Window2:
    def __init__(self, master):
        self.master = master
        self.master.title("restaurant management system")
        self.master.geometry('1350x750+0+0')
        self.master.configure(bg='#E2CCA3')
        self.frame = Frame(self.master, bg='#E2CCA3')
        self.frame.pack()

new=Tk()
call = Window1(new)
call1 = Window2(new)
new.mainloop()
