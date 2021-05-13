from tkinter import*
from PIL import ImageTk, Image
from tkinter import messagebox
import sqlite3
#creating main window
root=Tk()
root.title('front page')
root.geometry("1350x756+0+0")
root.configure(background='#E2CCA3')
load=Image.open('img.jpg')
my_image=ImageTk.PhotoImage(load)
my_label=Label(root,image=my_image).place(x=0,y=0)
img1=Image.open('c.png')
myimage=ImageTk.PhotoImage(img1)
lbl1=Label(root,image=myimage,bg='#423930')
lbl1.place(x=200,y=50)

def menu():
    new = Tk()
    new.title('menu')
    new.geometry("1350x750+0+0")
    new.configure(background='#E2CCA3')

    frame = Frame(new, bg='#E2CCA3', bd=10, pady=10, padx=10, relief=RIDGE)
    frame.pack(side=TOP)
    lbltitle = Label(frame, font=('arial', 40, 'bold'), text="MENU", bd=10, bg='#E2CCA3', fg='#423930')
    lbltitle.grid(row=0, column=0)

    menuframe = Frame(new, bg='#E2CCA3', bd=20, width=1200, height=600, relief=RIDGE)
    menuframe.pack()

    drinksframe = Frame(menuframe, bg='#E2CCA3', bd=10, width=600, height=500, relief=RIDGE)
    drinksframe.pack(side=LEFT)
    hotdrinksframe = Frame(drinksframe, bg='#E2CCA3', bd=10, width=300, height=200, relief=RIDGE)
    hotdrinksframe.pack(side=TOP)
    lbl1title = Label(hotdrinksframe, font=('arial', 20, 'bold'), text="HOT DRINKS", bd=20, bg='#E2CCA3',
                      fg='#423930')
    lbl1title.grid(row=0, column=0)

    colddrinksframe = Frame(drinksframe, bg='#E2CCA3', bd=10, width=300, height=200, relief=RIDGE)
    colddrinksframe.pack(side=BOTTOM)
    lbl2title = Label(colddrinksframe, font=('arial', 19, 'bold'), text="COLD DRINKS", bd=20, bg='#E2CCA3',
                      fg='#423930')
    lbl2title.grid(row=0, column=0)

    foodsframe = Frame(menuframe, bg='#E2CCA3', bd=10, width=600, height=500, relief=RIDGE)
    foodsframe.pack(side=RIGHT)
    snacksframe = Frame(foodsframe, bg='#E2CCA3', bd=10, width=600, height=500, relief=RIDGE)
    snacksframe.pack(side=TOP)
    lbl3title = Label(snacksframe, font=('arial', 19, 'bold'), text="SNACKS", bd=20, bg='#E2CCA3', fg='#423930')
    lbl3title.grid(row=0, column=0)
    var1 = IntVar()
    var2 = IntVar()
    var3 = IntVar()
    var4 = IntVar()
    var5 = IntVar()
    var6 = IntVar()
    var7 = IntVar()
    var8 = IntVar()
    var9 = IntVar()
    var10 = IntVar()
    var11 = IntVar()
    var12 = IntVar()
    var13 = IntVar()
    var14 = IntVar()
    var15 = IntVar()
    var16 = IntVar()
    var17 = IntVar()
    var18 = IntVar()
    var19 = IntVar()
    var20 = IntVar()

    # checkbutton for drinks
    latte = Checkbutton(hotdrinksframe, text='Latte', variable=var1, onvalue=1, offvalue=0,
                        font=('arial', 15, 'bold'), bg='#E2CCA3').grid(row=1, sticky=W)
    americano = Checkbutton(hotdrinksframe, text='Americano', variable=var2, onvalue=1, offvalue=0,
                            font=('arial', 15, 'bold'), bg='#E2CCA3').grid(row=2, sticky=W)
    espresso = Checkbutton(hotdrinksframe, text='Espresso', variable=var3, onvalue=1, offvalue=0,
                           font=('arial', 15, 'bold'), bg='#E2CCA3').grid(row=3, sticky=W)
    cappuccino = Checkbutton(hotdrinksframe, text='Cappuccino', variable=var4, onvalue=1, offvalue=0,
                             font=('arial', 15, 'bold'), bg='#E2CCA3').grid(row=4, sticky=W)
    hotchocolate = Checkbutton(hotdrinksframe, text='hotchocolate', variable=var5, onvalue=1, offvalue=0,
                               font=('arial', 15, 'bold'), bg='#E2CCA3').grid(row=5, sticky=W)

    coke = Checkbutton(colddrinksframe, text='coke', variable=var6, onvalue=1, offvalue=0,
                       font=('arial', 15, 'bold'), bg='#E2CCA3').grid(row=1, sticky=W)
    fanta = Checkbutton(colddrinksframe, text='fanta', variable=var7, onvalue=1, offvalue=0,
                        font=('arial', 15, 'bold'), bg='#E2CCA3').grid(row=2, sticky=W)
    sprite = Checkbutton(colddrinksframe, text='sprite', variable=var8, onvalue=1, offvalue=0,
                         font=('arial', 15, 'bold'), bg='#E2CCA3').grid(row=3, sticky=W)
    pepsi = Checkbutton(colddrinksframe, text='pepsi', variable=var9, onvalue=1, offvalue=0,
                        font=('arial', 15, 'bold'), bg='#E2CCA3').grid(row=4, sticky=W)
    dew = Checkbutton(colddrinksframe, text='dew', variable=var10, onvalue=1, offvalue=0,
                      font=('arial', 15, 'bold'), bg='#E2CCA3').grid(row=5, sticky=W)

    txtlatte = Entry(hotdrinksframe, font=('arial', 11, 'bold'), bd=8, width=6, justify=LEFT, state=DISABLED)
    txtlatte.grid(row=1, column=1)
    txtamericano = Entry(hotdrinksframe, font=('arial', 11, 'bold'), bd=8, width=6, justify=LEFT,
                         state=DISABLED)
    txtamericano.grid(row=2, column=1)
    txtexpresso = Entry(hotdrinksframe, font=('arial', 11, 'bold'), bd=8, width=6, justify=LEFT, state=DISABLED)
    txtexpresso.grid(row=3, column=1)
    txtcappuccino = Entry(hotdrinksframe, font=('arial', 11, 'bold'), bd=8, width=6, justify=LEFT,
                          state=DISABLED)
    txtcappuccino.grid(row=4, column=1)
    txthotchocolate = Entry(hotdrinksframe, font=('arial', 11, 'bold'), bd=8, width=6, justify=LEFT,
                            state=DISABLED)
    txthotchocolate.grid(row=5, column=1)

    txtcoke = Entry(colddrinksframe, font=('arial', 11, 'bold'), bd=8, width=6, justify=LEFT, state=DISABLED)
    txtcoke.grid(row=1, column=1)

    txtfanta = Entry(colddrinksframe, font=('arial', 11, 'bold'), bd=8, width=6, justify=LEFT, state=DISABLED)
    txtfanta.grid(row=2, column=1)

    txtsprite = Entry(colddrinksframe, font=('arial', 11, 'bold'), bd=8, width=6, justify=LEFT, state=DISABLED)
    txtsprite.grid(row=3, column=1)

    txtpepsi = Entry(colddrinksframe, font=('arial', 11, 'bold'), bd=8, width=6, justify=LEFT, state=DISABLED)
    txtpepsi.grid(row=4, column=1)

    txtdew = Entry(colddrinksframe, font=('arial', 11, 'bold'), bd=8, width=6, justify=LEFT, state=DISABLED)
    txtdew.grid(row=5, column=1)

    # check button for foods
    momo = Checkbutton(snacksframe, text='momo', variable=var11, onvalue=1, offvalue=0,
                       font=('arial', 15, 'bold'), bg='#E2CCA3').grid(row=1, sticky=W)
    chowmein = Checkbutton(snacksframe, text='chowmein', variable=var12, onvalue=1, offvalue=0,
                           font=('arial', 15, 'bold'), bg='#E2CCA3').grid(row=2, sticky=W)
    thukpa = Checkbutton(snacksframe, text='thukpa', variable=var13, onvalue=1, offvalue=0,
                         font=('arial', 15, 'bold'), bg='#E2CCA3').grid(row=3, sticky=W)
    pizza = Checkbutton(snacksframe, text='pizza', variable=var14, onvalue=1, offvalue=0,
                        font=('arial', 15, 'bold'), bg='#E2CCA3').grid(row=4, sticky=W)
    burger = Checkbutton(snacksframe, text='Burger', variable=var15, onvalue=1, offvalue=0,
                         font=('arial', 15, 'bold'), bg='#E2CCA3').grid(row=5, sticky=W)
    chicken_chilly = Checkbutton(snacksframe, text='Chicken chilly', variable=var16, onvalue=1, offvalue=0,
                                 font=('arial', 15, 'bold'), bg='#E2CCA3').grid(row=6, sticky=W)
    frenchfries = Checkbutton(snacksframe, text='Fries', variable=var17, onvalue=1, offvalue=0,
                              font=('arial', 15, 'bold'), bg='#E2CCA3').grid(row=7, sticky=W)
    pasta = Checkbutton(snacksframe, text='Pasta', variable=var18, onvalue=1, offvalue=0,
                        font=('arial', 15, 'bold'), bg='#E2CCA3').grid(row=8, sticky=W)

    txtmomo = Entry(snacksframe, font=('arial', 11, 'bold'), bd=8, width=6, justify=LEFT, state=DISABLED)
    txtmomo.grid(row=1, column=1)
    txtchowmein = Entry(snacksframe, font=('arial', 11, 'bold'), bd=8, width=6, justify=LEFT, state=DISABLED)
    txtchowmein.grid(row=2, column=1)
    txtthukpa = Entry(snacksframe, font=('arial', 11, 'bold'), bd=8, width=6, justify=LEFT, state=DISABLED)
    txtthukpa.grid(row=3, column=1)
    txtpizza = Entry(snacksframe, font=('arial', 11, 'bold'), bd=8, width=6, justify=LEFT, state=DISABLED)
    txtpizza.grid(row=4, column=1)
    txtburger = Entry(snacksframe, font=('arial', 11, 'bold'), bd=8, width=6, justify=LEFT, state=DISABLED)
    txtburger.grid(row=5, column=1)
    txtchicken_chilly = Entry(snacksframe, font=('arial', 11, 'bold'), bd=8, width=6, justify=LEFT,
                              state=DISABLED)
    txtchicken_chilly.grid(row=6, column=1)
    txtfrenchfries = Entry(snacksframe, font=('arial', 11, 'bold'), bd=8, width=6, justify=LEFT, state=DISABLED)
    txtfrenchfries.grid(row=7, column=1)
    txtpasta = Entry(snacksframe, font=('arial', 11, 'bold'), bd=8, width=6, justify=LEFT, state=DISABLED)
    txtpasta.grid(row=8, column=1)

    def next():
        next1 = Tk()
        next1.title('billing')
        next1.geometry("1350x750+0+0")
        next1.configure(background='#E2CCA3')

        frame2 = Frame(next1, bg='#E2CCA3', bd=10, pady=10, padx=10, relief=RIDGE)
        frame2.pack(side=TOP)
        billtitle = Label(frame2, font=('arial', 40, 'bold'), text="Billing system", bd=10, bg='#E2CCA3',
                          fg='#423930')
        billtitle.grid(row=0, column=0)

    nextframe = Frame(foodsframe, bg='#E2CCA3', bd=10, width=500, height=400, relief=RIDGE)
    nextframe.pack(side=BOTTOM)
    nextbtn = Button(nextframe, text='next', bg='#E2CCA3', font=('arial', 15, 'bold'), command=next)
    nextbtn.pack()
    # messagebox.showinfo('info', 'login success')
#creating customer window
def customer():
    global my_img
    data=Tk()
    data.geometry('1350x750+0+0')
    data.configure(background='#E2CCA3')
    frame = Frame(data, bg='#E2CCA3', bd=10, pady=10, padx=10, width=600, height=500, relief=RIDGE)
    frame.place(x=300, y=100)
    # creating a database or connect to one
    conn = sqlite3.connect('customer_information1.db')
    # creating cursor
    # cursor class is an instance using which you can invoke methods that
    # execute SQLITE statements,fetch data from the result sets of the queries
    c = conn.cursor()

    # create table
    #c.execute("""CREATE TABLE information(
    #           first_name text,
    #           last_name text,
    #           address text,
    #           username text,
    #           password text,
    #           contact_number integer
    #)
    #""")

    def submit():
        # create a database or connect to one
        conn = sqlite3.connect('customer_information1.db')
        # create cursor
        c = conn.cursor()

        # insert into table
        c.execute("INSERT INTO information VALUES(:first_name,:last_name,:address,:username,:password,:contact_number)", {
            'first_name': first_name.get(),
            'last_name': last_name.get(),
            'address': address.get(),
            'username': username.get(),
            'password': password.get(),
            'contact_number': contact_number.get(),
        })
        print('address inserted successfully')

        conn.commit()

        conn.close()

        # clear the text boxes
        first_name.delete(0, END)
        last_name.delete(0, END)
        address.delete(0, END)
        username.delete(0, END)
        password.delete(0, END)
        contact_number.delete(0, END)

    """defquery():
        conn = sqlite3.connect('customer_information1.db')

        c = conn.cursor()
        c.execute("SELECT *,oid FROM information")

        records = c.fetchall()
        print(records)

        print_record = ''
        for record in records:
            print_record += str(record)+ "\n"

        query_label = Label(data, text=print_record)
        query_label.grid(row=8, column=0, columnspan=2)

        conn.commit()
        conn.close()"""

    def login():
        login1=Tk()
        login1.geometry('1350x750+0+0')
        login1.configure(background='#E2CCA3')

        def login5():
            conn=sqlite3.connect('customer_information1.db')
            c=conn.cursor()
            c.execute("SELECT *,oid FROM information")
            records=c.fetchall()
            for record in records:
                if str(record[3])==username.get() and str(record[4])==password.get():
                    messagebox.showinfo("login","login successful",parent=login1)
                    menu()
                    login1.withdraw()
                else:
                    messagebox.showinfo("login","login failed",parent=login1)
            conn.commit()
            conn.close()



        frame = Frame(login1, bg='#E2CCA3', bd=10, pady=10, padx=10, width=600, height=500, relief=RIDGE)
        frame.place(x=300, y=100)

        username = Entry(frame, width=50)
        username.grid(row=1, column=1)

        password = Entry(frame, width=50)
        password.grid(row=2, column=1)

        username_label = Label(frame, text="username", bg='#E2CCA3')
        username_label.grid(row=1, column=0)

        password_label = Label(frame, text="password", bg='#E2CCA3')
        password_label.grid(row=2, column=0)

        login4=Button(frame,text="login",command=login5)
        login4.grid(row=3,column=0)



    # create text box
    first_name = Entry(frame, width=50)
    first_name.grid(row=0, column=10, padx=20)

    last_name = Entry(frame, width=50)
    last_name.grid(row=2, column=10)

    address = Entry(frame, width=50)
    address.grid(row=4, column=10)

    username = Entry(frame, width=50)
    username.grid(row=6, column=10)

    password = Entry(frame, width=50)
    password.grid(row=8, column=10)

    contact_number = Entry(frame, width=50)
    contact_number.grid(row=10, column=10)


    # create textbox labels
    first_name_label = Label(frame, text="first name",bg='#E2CCA3')
    first_name_label.grid(row=0, column=2)

    last_name_label = Label(frame, text="last name",bg='#E2CCA3')
    last_name_label.grid(row=2, column=2)

    address_label = Label(frame, text="address",bg='#E2CCA3')
    address_label.grid(row=4, column=2)

    username_label = Label(frame, text="username",bg='#E2CCA3')
    username_label.grid(row=6, column=2)

    password_label = Label(frame, text="password",bg='#E2CCA3')
    password_label.grid(row=8, column=2)

    contact_number_label = Label(frame, text="contact",bg='#E2CCA3')
    contact_number_label.grid(row=10, column=2)

    # create submit button
    submit_btn = Button(frame, text="register", command=submit)
    submit_btn.grid(row=14, column=10, columnspan=6, padx=10, pady=10, ipadx=50)
    login_btn = Button(frame, text="login", command=login)
    login_btn.grid(row=16, column=10, columnspan=6, padx=10, pady=10, ipadx=50)

    print("Table created successfully")
    # commit chang
    conn.commit()
    # close connection
    conn.close()

    data.mainloop()

def employee():
    global my_img

    def login():
        db = sqlite3.connect('login.sqlite')
        db.execute('CREATE TABLE IF NOT EXISTS login(username TEXT,password TEXT)')
        db.execute("INSERT INTO login(username,password) VALUES('admin','admin')")
        cursor = db.cursor()
        cursor.execute("SELECT * FROM login where username=? AND password=?", (userinput.get(), passinput.get()))
        row = cursor.fetchone()
        if row:
            menu()
        else:
            messagebox.showinfo('info', 'login failed')
        cursor.connection.commit()
        db.close()

    main_window = Tk()
    main_window.title('login')
    main_window.geometry('1350x750+0+0')
    main_window.configure(background='#E2CCA3')
    frame = Frame(main_window, bg='#9E7C55', width=1050, height=800)
    frame.pack()

    user_input = StringVar()
    pass_input = StringVar()

    info_label = Label(frame, text='Employee login', font=('ariel', 90, 'bold'), bg='#E2CCA3', fg='#423930')
    info_label.grid(row=0, column=0, columnspan=8, pady=60)

    LoginFrame1 = LabelFrame(frame, width=1050, height=600
                             , font=('arial', 40, 'bold'), relief='ridge', bg='#9E7C55', bd=20)
    LoginFrame1.grid(row=1, column=0, columnspan=8, pady=40)

    LoginFrame2 = LabelFrame(frame, width=1050, height=600
                             , font=('arial', 40, 'bold'), relief='ridge', bg='#9E7C55', bd=20)
    LoginFrame2.grid(row=2, column=0, columnspan=8, pady=40)

    info_user = Label(LoginFrame1, text='username', font='ariel,25,bold', bg='#E2CCA3', fg='#423930')
    info_user.grid(row=0, column=0)
    userinput = Entry(LoginFrame1, textvariable=user_input)
    userinput.grid(row=0, column=4)

    info_pass = Label(LoginFrame1, text='password', font='ariel,25,bold', bg='#E2CCA3', fg='#423930')
    info_pass.grid(row=1, column=0)
    passinput = Entry(LoginFrame1, textvariable=pass_input, show='*')
    passinput.grid(row=1, column=4)

    login_btn = Button(LoginFrame2, text='Login', font='ariel,15,bold', bg='#E2CCA3', fg='#423930', command=login)
    login_btn.grid(row=3, column=1, pady=20, padx=20)


# Button  option
button_customer=Button(root,padx=10,pady=15,text="customer",command=customer,fg='#380808',bg="#E2CCA3",font=("Times",25,"bold"))
button_customer.pack()
button_customer.place(x=900,y=650)
button_employee=Button(root,padx=10,pady=15,text="employee",command=employee,fg='#380808',bg="#E2CCA3",font=("Times",25,"bold"))
button_employee.pack()
button_employee.place(x=300,y=650)


root.mainloop()

