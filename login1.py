from tkinter import *
from tkinter import messagebox
import customerpage


class Management:
    def __init__(self, root):
        self.main = root
        self.main.title("Employee Management System")
        self.main.geometry("2000x1300+0+0")

        fram1 = Frame(self.main, bd=5, relief=GROOVE)
        fram1.place(x=500, y=150, width=740, height=300)

        self.user = StringVar()
        self.password = StringVar()

        title = Label(fram1, text="EMPLOYEE MANAGEMENT SYSTEM", font=("Gadugi", 20, "bold")).grid(row=0, column=0,
                                                                                                  pady=10)

        Softwarica = Label(fram1, text="Username", font=("Gadugi", 25)).grid(row=1, column=0, pady=5)

        Softwarica1 = Entry(fram1, bd=7, relief=GROOVE, textvariable=self.user, width=20, font=("Gadugi 14 bold")).grid(
            row=3, column=0, padx=5, pady=5)

        Softwarica2 = Label(fram1, text="Password", font=("Gadugi", 25)).grid(row=1, column=2, pady=10)

        Softwarica3 = Entry(fram1, show="*", bd=7, relief=GROOVE, textvariable=self.password, width=20,
                            font=("Gadugi 14 bold")).grid(row=3, column=2, padx=5, pady=5)

        Coventry = Button(fram1, text="Login", bd=5, width=15, font="Gadugi 14 bold", command=self.login).place(x=10,
                                                                                                                y=180)

        Coventry1 = Button(fram1, text="Register", bd=5, width=15, font="Gadugi 14 bold", command=self.register).place(
            x=200, y=180)

        Coventry2 = Button(fram1, text="Reset", bd=5, width=15, font="Gadugi 14 bold", command=self.reset).place(x=390,
                                                                                                                 y=180)

        Coventry3 = Button(fram1, text="Exit", bd=5, width=11, font="Gadugi 14 bold", command=self.exit).place(x=580,
                                                                                                               y=180)

    def login(self):
        with open(self.user.get(), 'r') as user_here:
            password = user_here.readline()
            if self.password.get() in password:
                self.main.destroy()
                new = Tk()
                customerpage.data(new)
                new.mainloop()
            else:
                messagebox.showerror("Error", "invalid username or password")

    def register(self):
        print(self.user.get())
        print(self.password.get())
        if self.user.get() == '' or self.password.get() == "":
            messagebox.showerror("Error", "The fields must be filled")
        elif len(self.password.get()) < 6:
            messagebox.showerror("Error", "Password must me ast least six digit")

        else:
            with open(self.user.get(), 'w') as write_in:
                write_in.write(self.password.get())

            messagebox.showinfo("Done", "Your Account has been saved.Proceed to fill other details")


    def reset(self):
        self.user.set("")
        self.password.set("")

    def exit(self):
        option = messagebox.askyesno("Exit", "Do you want to exit?")
        if option > 0:
            self.main.destroy()
        else:
            return


root = Tk()
call = Management(root)
root.mainloop()
