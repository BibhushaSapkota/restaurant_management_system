
from tkinter import*
from PIL import ImageTk, Image
from tkinter import messagebox
import sqlite3



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





def customer():
    global my_img
    data=Tk()
    data.geometry('1350x750+0+0')
    data.configure(background='#E2CCA3')

    # creating a database or connect to one
    conn = sqlite3.connect('address_book.db')
    # creating cursor
    # cursor class is an instance using which you can invoke methods that
    # execute SQLITE statements,fetch data from the result sets of the queries
    c = conn.cursor()

    # create table
    # c.execute("""CREATE TABLE addresses(
    #           first_name text,
    #           last_name text,
    #           address text,
    #           city text,
    #          state text,
    #           contact_number integer
    # )
    # """)

    def submit():
        # create a database or connect to one
        conn = sqlite3.connect('address_book.db')
        # create cursor
        c = conn.cursor()

        # insert into table
        c.execute("INSERT INTO addresses VALUES(:first_name,:last_name,:address,:city,:state,:contact_number)", {
            'first_name': first_name.get(),
            'last_name': last_name.get(),
            'address': address.get(),
            'city': city.get(),
            'state': state.get(),
            'contact_number': contact_number.get(),
        })
        print('address inserted successfully')

        conn.commit()

        conn.close()

        # clear the text boxes
        first_name.delete(0, END)
        last_name.delete(0, END)
        address.delete(0, END)
        city.delete(0, END)
        state.delete(0, END)
        contact_number.delete(0, END)

    def query():
        conn = sqlite3.connect('address_book.db')

        c = conn.cursor()
        c.execute("SELECT *,oid FROM addresses")

        records = c.fetchall()
        print(records)

        print_record = ''
        for record in records:
            print_record += str(record)+ "\n"

        query_label = Label(data, text=print_record)
        query_label.grid(row=8, column=0, columnspan=2)

        conn.commit()
        conn.close()


    # create text box
    first_name = Entry(data, width=50)
    first_name.grid(row=0, column=10, padx=20)

    last_name = Entry(data, width=50)
    last_name.grid(row=2, column=10)

    address = Entry(data, width=50)
    address.grid(row=4, column=10)

    city = Entry(data, width=50)
    city.grid(row=6, column=10)

    state = Entry(data, width=50)
    state.grid(row=8, column=10)

    contact_number = Entry(data, width=50)
    contact_number.grid(row=10, column=10)


    # create textbox labels
    first_name_label = Label(data, text="first name",bg='#E2CCA3')
    first_name_label.grid(row=0, column=2)

    last_name_label = Label(data, text="last name",bg='#E2CCA3')
    last_name_label.grid(row=2, column=2)

    address_label = Label(data, text="address",bg='#E2CCA3')
    address_label.grid(row=4, column=2)

    city_label = Label(data, text="city",bg='#E2CCA3')
    city_label.grid(row=6, column=2)

    state_label = Label(data, text="state",bg='#E2CCA3')
    state_label.grid(row=8, column=2)

    contact_number_label = Label(data, text="contact",bg='#E2CCA3')
    contact_number_label.grid(row=10, column=2)

    # create submit button
    submit_btn = Button(data, text="register", command=submit)
    submit_btn.grid(row=14, column=10, columnspan=6, padx=10, pady=10, ipadx=50)
    display_btn = Button(data, text="show records", command=query)
    display_btn.grid(row=15, column=10, columnspan=6, padx=10, pady=10, ipadx=50)

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
            new = Tk()
            new.geometry("1350x750+0+0")
            new.configure(background='#E2CCA3')
            # messagebox.showinfo('info', 'login success')
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

