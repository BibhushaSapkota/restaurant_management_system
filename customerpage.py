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
