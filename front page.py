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


def pic():
    roo=Toplevel()

    my_img1=ImageTk.PhotoImage(Image.open("c .jpg"))
    my_img2=ImageTk.PhotoImage(Image.open("a.jpg"))
    my_img3=ImageTk.PhotoImage(Image.open("b .jpg"))
    my_img4=ImageTk.PhotoImage(Image.open("d.jpg"))
    my_img5=ImageTk.PhotoImage(Image.open("f.jpg"))

    image_list=[my_img1,my_img2,my_img3,my_img4,my_img5]

    my_label=Label(image=my_img1)
    my_label.grid(row=0,column=0,columnspan=3)

    def forward(image_number):
        global my_label
        global button_forward
        global button_back
        my_label.grid_forget()
        my_label=Label(image=image_list[image_number-1])
        button_forward=Button(roo,text=">>",command=lambda: forward(image_number+1))
        button_back=Button(roo,text="<<",command=lambda:back(image_number-1))
        if image_number==5:
            button_forward=Button(roo,text=">>",state=DISABLED)


        my_label.grid(row=0, column=0, columnspan=3)
        button_back.grid(row=1, column=0)
        button_forward.grid(row=1, column=2)


    def back(image_number):
        global my_label
        global button_forward
        global button_back
        my_label.grid_forget()
        my_label = Label(image=image_list[image_number - 1])
        button_forward = Button(roo, text=">>", command=lambda: forward(image_number + 1))
        button_back = Button(roo, text="<<", command=lambda: back(image_number - 1))

        if image_number==1:
            button_back=Button(roo,text="<<",state=DISABLED)

        my_label.grid(row=0, column=0, columnspan=3)
        button_back.grid(row=1, column=0)
        button_forward.grid(row=1, column=2)

    button_back=Button(roo,text="<<",command=back,state=DISABLED)
    button_exit=Button(roo,text="next",command=next)
    button_forward=Button(roo,text=">>",command=lambda:forward(2))

    button_back.grid(row=1,column=0)
    button_exit.grid(row=1,column=1)
    button_forward.grid(row=1,column=2)
    roo.mainloop()

def menu():
    new = Toplevel()
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
        next1 =Toplevel()
        next1.title('billing')
        next1.geometry("1350x750+0+0")
        next1.configure(background='#E2CCA3')

        frame5 = Frame(next1, bg='#E2CCA3', bd=10, pady=10, padx=10, relief=RIDGE)
        frame5.pack(side=TOP)
        billtitle = Label(frame5, font=('arial', 40, 'bold'), text="Billing system", bd=10, bg='#E2CCA3',
                          fg='#423930')
        billtitle.grid(row=0, column=0)


    nextframe = Frame(foodsframe, bg='#E2CCA3', bd=10, width=500, height=400, relief=RIDGE)
    nextframe.pack(side=BOTTOM)
    nextbtn = Button(nextframe, text='next', bg='#E2CCA3', font=('arial', 15, 'bold'), command=next)
    nextbtn.pack()


#creating customer window
def customer():
    global my_img
    data=Toplevel()
    data.geometry('1350x750+0+0')
    data.configure(background='#E2CCA3')
    frame = Frame(data, bg='#E2CCA3', bd=10, pady=10, padx=10, width=600, height=500, relief=RIDGE)
    frame.place(x=300, y=300)
    frame1= Frame(data, bg='#E2CCA3', bd=10, pady=10, padx=10, width=100, height=100,relief=RIDGE)
    frame1.place(x=300, y=10)
    info_label1 = Label(frame1, text='registration form', font=('ariel',50, 'bold'), bg='#E2CCA3', fg='#423930')
    info_label1.grid(row=11, column=108, columnspan=18,rowspan=3,pady=10,ipadx=5,ipady=5)
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
        login1=Toplevel()
        login1.geometry('1350x750+0+0')
        login1.configure(background='#E2CCA3')

        def login5():
            conn=sqlite3.connect('customer_information1.db')
            c=conn.cursor()
            c.execute("SELECT *,oid FROM information")
            records=c.fetchall()
            for record in records:
                if str(record[3])==username.get() and str(record[4])==password.get():
                    try:
                        messagebox.showinfo("login","login successful",parent=login1)
                        login1.withdraw()
                        return menu()
                    except:
                        pass
            messagebox.showinfo("login","login failed",parent=login1)
            conn.commit()
            conn.close()



        frame = Frame(login1, bg='#E2CCA3', bd=10, pady=10, padx=10, width=600, height=500, relief=RIDGE)
        frame.place(x=300, y=100)

        username = Entry(frame, width=50,font=('arial', 15, 'bold'),fg='#423930')
        username.grid(row=1, column=1)

        password = Entry(frame, width=50, show='*',font=('arial', 15, 'bold'),fg='#423930')
        password.grid(row=2, column=1)

        username_label = Label(frame, text="username", bg='#E2CCA3',font=('arial', 15, 'bold'),fg='#423930')
        username_label.grid(row=1, column=0)

        password_label = Label(frame, text="password", bg='#E2CCA3',font=('arial', 15, 'bold'),fg='#423930')
        password_label.grid(row=2, column=0)

        login4=Button(frame,text="login",command=login5,font=('arial', 15, 'bold'),fg='#423930')
        login4.grid(row=3,column=5)



    # create text box
    first_name = Entry(frame, width=70)
    first_name.grid(row=0, column=10, padx=20)

    last_name = Entry(frame, width=70)
    last_name.grid(row=3, column=10)

    address = Entry(frame, width=70)
    address.grid(row=6, column=10)

    username = Entry(frame, width=70)
    username.grid(row=9, column=10)

    password = Entry(frame, width=70)
    password.grid(row=12, column=10)

    contact_number = Entry(frame, width=70)
    contact_number.grid(row=15, column=10)


    # create textbox labels
    first_name_label = Label(frame, text="First name",bg='#E2CCA3',font=('arial', 15, 'bold'),fg='#423930')
    first_name_label.grid(row=0, column=2)

    last_name_label = Label(frame, text="Last name",bg='#E2CCA3',font=('arial', 15, 'bold'),fg='#423930')
    last_name_label.grid(row=3, column=2)

    address_label = Label(frame, text="Address",bg='#E2CCA3',font=('arial', 15, 'bold'),fg='#423930')
    address_label.grid(row=6, column=2)

    username_label = Label(frame, text="Username",bg='#E2CCA3',font=('arial', 15, 'bold'),fg='#423930')
    username_label.grid(row=9, column=2)

    password_label = Label(frame, text="Password",bg='#E2CCA3',font=('arial', 15, 'bold'),fg='#423930')
    password_label.grid(row=12, column=2)

    contact_number_label = Label(frame, text="Contact",bg='#E2CCA3',font=('arial', 15, 'bold'),fg='#423930')
    contact_number_label.grid(row=15, column=2)

    # create submit button
    submit_btn = Button(frame, text="register",font=('arial', 14, 'bold'),bg='#AEAFB4',command=submit)
    submit_btn.grid(row=18, column=10, columnspan=6, padx=10, pady=10, ipadx=50)
    login_btn = Button(frame, text="login",font=('arial', 17, 'bold'),bg='#AEAFB4', command=login)
    login_btn.grid(row=21, column=10, columnspan=6, padx=10, pady=10, ipadx=50)

    # commit chang
    conn.commit()
    # close connection
    conn.close()

    data.mainloop()


def employee_details():
    data = Tk()
    data.geometry('1350x750+0+0')
    data.configure(background='#E2CCA3')
    frame = Frame(data, bg='#E2CCA3', bd=20, pady=10, padx=10, width=600, height=500, relief=RIDGE)
    frame.place(x=300, y=10)
    frame1= Frame(data, bg='#E2CCA3', bd=20, pady=10, padx=10, width=100, height=100,relief=RIDGE)
    frame1.place(x=300, y=450)
    frame2= Frame(data, bg='#E2CCA3', bd=20, pady=10, padx=10, width=100, height=100,relief=RIDGE)
    frame2.place(x=300, y=300)


    # creating a database or connect to one
    conn = sqlite3.connect('employee_detail.db')
    # creating cursor
    # cursor class is an instance using which you can invoke methods that
    # execute SQLITE statements,fetch data from the result sets of the queries
    c = conn.cursor()

    # create table
    #c.execute("""CREATE TABLE detail(
    #           first_name text,
    #           last_name text,
    #           address text,
    #           shift text,
    #           offdays text,
    #           contact_number integer
    #)
    #""")

    def submit():
        # create a database or connect to one
        conn = sqlite3.connect('employee_detail.db')
        # create cursor
        c = conn.cursor()

        # insert into table
        c.execute("INSERT INTO detail VALUES(:first_name,:last_name,:address,:shift,:offdays,:contact_number)", {
            'first_name': first_name.get(),
            'last_name': last_name.get(),
            'address': address.get(),
            'shift': shift.get(),
            'offdays': offdays.get(),
            'contact_number': contact_number.get(),
            'deletebox':deletebox.get()
        })
        print('address inserted successfully')

        conn.commit()

        conn.close()

        # clear the text boxes
        first_name.delete(0, END)
        last_name.delete(0, END)
        address.delete(0, END)
        shift.delete(0, END)
        offdays.delete(0, END)
        contact_number.delete(0, END)
        deletebox.delete(0,END)

    def query():
        conn = sqlite3.connect('employee_details.db')

        c = conn.cursor()
        c.execute("SELECT *,oid FROM detail")

        records = c.fetchall()
        print(records)

        print_record = ''
        for record in records:
            print_record += str(record) + "\n"

        query_label = Label(data, text=print_record)
        query_label.grid(row=8, column=0, columnspan=2)

        conn.commit()
        conn.close()

    def delete():
        conn = sqlite3.connect('employee_details.db')

        c = conn.cursor()
        c.execute("DELETE from detail WHERE oid=" + deletebox.get())
        print('Deleted successfully')

        c.execute("SELECT *,oid FROM detail")

        records = c.fetchall()

        print_record = ''
        for record in records:
            print_record += str(record[0]) + " " + str(record[1]) + ' ' + '\t' + str(record[6]) + "\n"

        query_label = Label(data, text=print_record)
        query_label.grid(row=8, column=0, columnspan=2)

        conn.commit()
        conn.close()

    def save():
        conn = sqlite3.connect('employee_details.db')

        c = conn.cursor()
        record_id = deletebox.get()

        c.execute("""UPDATE detail SET
             first_name=:first,
             last_name=:last,
             address=:address,
             shift=:shift,
             offdays=:offdays,
             contact_number=:contact number
             WHERE oid=:oid""",
                  {'first': first_name_editor.get(),
                   'last': last_name_editor.get(),
                   'address': address_editor.get(),
                   'shift': shift_editor.get(),
                   'offdays': offdays_editor.get(),
                   'contact_number': contact_number.get(),
                   'oid': record_id
                   }
                  )
        conn.commit()
        conn.close()

        editor.destroy()

    def update():
        global editor
        editor = Tk()
        editor.title('Update Data')

        conn = sqlite3.connect('employee_details.db')

        c = conn.cursor()

        record_id = deletebox.get()

        c.execute("SELECT * FROM detail WHERE oid=" + record_id)

        records = c.fetchall()
        global first_name_editor
        global last_name_editor
        global address_editor
        global contact_number_editor
        global shift_editor
        global offdays_editor

        first_name_editor = Entry(editor, width=30)
        first_name_editor.grid(row=0, column=1, padx=20)

        last_name_editor = Entry(editor, width=30)
        last_name_editor.grid(row=1, column=1)

        address_editor = Entry(editor, width=30)
        address_editor.grid(row=2, column=1)

        shift_editor = Entry(editor, width=30)
        shift_editor.grid(row=3, column=1)

        offdays_editor = Entry(editor, width=30)
        offdays_editor.grid(row=4, column=1)

        contact_number_editor = Entry(editor, width=30)
        contact_number.grid(row=5, column=1)

        # create textbox labels
        first_name_editor_label = Label(editor, text="first name")
        first_name_editor_label.grid(row=0, column=0)

        last_name_editor_label = Label(editor, text="last name")
        last_name_editor_label.grid(row=1, column=0)

        address_editor_label = Label(editor, text="address")
        address_editor_label.grid(row=2, column=0)

        shift_editor_label = Label(editor, text="shift")
        shift_editor_label.grid(row=3, column=0)

        offdays_editor_label = Label(editor, text="off days")
        offdays_editor_label.grid(row=4, column=0)

        contact_number_editor_label = Label(editor, text="contact number")
        contact_number_editor_label.grid(row=5, column=0)

        for record in records:
            first_name_editor.insert(0, record[0])
            last_name_editor.insert(0, record[1])
            address_editor.insert(0, record[2])
            shift_editor.insert(0, record[3])
            offdays_editor.insert(0, record[4])
            contact_number_editor.insert(0, record[5])
        edit_btn = Button(editor, text="Save", command=save)
        edit_btn.grid(row=6, column=0, columnspan=2, padx=10, pady=10, ipadx=125)

        # create text box

    first_name = Entry(frame, width=50)
    first_name.grid(row=0, column=10, padx=20)

    last_name = Entry(frame, width=50)
    last_name.grid(row=2, column=10)

    address = Entry(frame, width=50)
    address.grid(row=4, column=10)

    shift = Entry(frame, width=50)
    shift.grid(row=6, column=10)

    offdays = Entry(frame, width=50)
    offdays.grid(row=8, column=10)

    contact_number = Entry(frame, width=50)
    contact_number.grid(row=10, column=10)

    deletebox = Entry(frame2, width=60)
    deletebox.grid(row=12, column=10)

    # create textbox labels
    first_name_label = Label(frame, text="first name", bg='#E2CCA3', font=('arial', 11, 'bold'))
    first_name_label.grid(row=0, column=2)

    last_name_label = Label(frame, text="last name", bg='#E2CCA3', font=('arial', 11, 'bold'))
    last_name_label.grid(row=2, column=2)

    address_label = Label(frame, text="address", bg='#E2CCA3', font=('arial', 11, 'bold'))
    address_label.grid(row=4, column=2)

    shift_label = Label(frame, text="shift", bg='#E2CCA3', font=('arial', 11, 'bold'))
    shift_label.grid(row=6, column=2)

    offdays_label = Label(frame, text="off days", bg='#E2CCA3', font=('arial', 11, 'bold'))
    offdays_label.grid(row=8, column=2)

    contact_number_label = Label(frame, text="contact", bg='#E2CCA3', font=('arial', 11, 'bold'))
    contact_number_label.grid(row=10, column=2)

    deletebox_label = Label(frame2, text="select ID", bg='#E2CCA3',font=('arial', 11, 'bold'))
    deletebox_label.grid(row=12, column=2)

    # create submit button
    submit_btn = Button(frame1, text="register", command=submit, font=('arial', 15, 'bold'))
    submit_btn.grid(row=1, column=10, columnspan=6, padx=10, pady=10, ipadx=50)
    display_btn = Button(frame1, text="show details", command=query, font=('arial', 15, 'bold'))
    display_btn.grid(row=3, column=12, columnspan=18, padx=10, pady=10, ipadx=50)
    delete_btn = Button(frame1, text=" delete ", command=delete, font=('arial', 15, 'bold'))
    delete_btn.grid(row=2, column=10, columnspan=6, padx=10, pady=10, ipadx=50)
    update_btn = Button(frame1, text="update ", command=update, font=('arial', 15, 'bold'))
    update_btn.grid(row=2, column=18, columnspan=7, padx=10, pady=10, ipadx=50)
    menu_btn = Button(frame1, text=" menu  ", command=menu, font=('arial', 15, 'bold'))
    menu_btn.grid(row=1, column=18, columnspan=7, padx=10, pady=10, ipadx=50)

    # commit chang
    conn.commit()
    # close connection
    conn.close()


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
            employee_details()
        else:
            messagebox.showinfo('info', 'login failed')
        cursor.connection.commit()
        db.close()

    main_window = Toplevel()
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

    #detail_btn = Button(LoginFrame2, text='detail', font='ariel,15,bold', bg='#E2CCA3', fg='#423930', command=employee_details)
    #detail_btn.grid(row=3, column=3, pady=20, padx=20)

    main_window.mainloop()

# Button  option
button_customer=Button(root,padx=10,pady=15,text="customer",command=customer,fg='#380808',bg="#E2CCA3",font=("Times",25,"bold"))
button_customer.pack()
button_customer.place(x=900,y=650)
button_employee=Button(root,padx=10,pady=15,text="employee",command=employee,fg='#380808',bg="#E2CCA3",font=("Times",25,"bold"))
button_employee.pack()
button_employee.place(x=300,y=650)
#button_pic=Button(root,padx=10,pady=15,text="picture",command=pic,fg='#380808',bg="#E2CCA3",font=("Times",25,"bold"))
#button_pic.pack()
#button_pic.place(x=500,y=650)


root.mainloop()


