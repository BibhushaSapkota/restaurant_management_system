from tkinter import *
import sqlite3


def details():
    data = Tk()
    data.geometry('1350x750+0+0')
    data.configure(background='#E2CCA3')

    # creating a database or connect to one
    conn = sqlite3.connect('employee_detail.db')
    # creating cursor
    # cursor class is an instance using which you can invoke methods that
    # execute SQLITE statements,fetch data from the result sets of the queries
    c = conn.cursor()

    # create table
    c.execute("""CREATE TABLE details(
               first_name text,
               last_name text,
               address text,
               shift text,
               off days text,
               contact_number integer
    )
    """)

    def submit():
        # create a database or connect to one
        conn = sqlite3.connect('employee_detail.db')
        # create cursor
        c = conn.cursor()

        # insert into table
        c.execute("INSERT INTO details VALUES(:first_name,:last_name,:address,:shift,:offdays,:contact_number)", {
            'first_name': first_name.get(),
            'last_name': last_name.get(),
            'address': address.get(),
            'shift': shift.get(),
            'off days': offdays.get(),
            'contact_number': contact_number.get(),
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

    def query():
        conn = sqlite3.connect('employee_details.db')

        c = conn.cursor()
        c.execute("SELECT *,oid FROM details")

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
        c.execute("DELETE from details WHERE oid=" + deletebox.get())
        print('Deleted successfully')

        c.execute("SELECT *,oid FROM details")

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

        c.execute("""UPDATE details SET
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

        c.execute("SELECT * FROM details WHERE oid=" + record_id)

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
        contact_number_editor_label.grid(row=4, column=0)

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

    first_name = Entry(data, width=50)
    first_name.grid(row=0, column=10, padx=20)

    last_name = Entry(data, width=50)
    last_name.grid(row=2, column=10)

    address = Entry(data, width=50)
    address.grid(row=4, column=10)

    shift = Entry(data, width=50)
    shift.grid(row=6, column=10)

    offdays = Entry(data, width=50)
    offdays.grid(row=8, column=10)

    contact_number = Entry(data, width=50)
    contact_number.grid(row=10, column=10)

    deletebox = Entry(data, width=30)
    deletebox.grid(row=9, column=1)

    # create textbox labels
    first_name_label = Label(data, text="first name", bg='#E2CCA3')
    first_name_label.grid(row=0, column=2)

    last_name_label = Label(data, text="last name", bg='#E2CCA3')
    last_name_label.grid(row=2, column=2)

    address_label = Label(data, text="address", bg='#E2CCA3')
    address_label.grid(row=4, column=2)

    shift_label = Label(data, text="shift", bg='#E2CCA3')
    shift_label.grid(row=6, column=2)

    offdays_label = Label(data, text="state", bg='#E2CCA3')
    offdays_label.grid(row=8, column=2)

    contact_number_label = Label(data, text="contact", bg='#E2CCA3')
    contact_number_label.grid(row=10, column=2)

    deletebox_label = Label(data, text="select ID")
    deletebox_label.grid(row=12, column=0)

    # create submit button
    submit_btn = Button(data, text="register", command=submit)
    submit_btn.grid(row=14, column=10, columnspan=6, padx=10, pady=10, ipadx=50)
    display_btn = Button(data, text="show records", command=query)
    display_btn.grid(row=15, column=10, columnspan=6, padx=10, pady=10, ipadx=50)
    delete_btn = Button(data, text="delete", command=delete)
    delete_btn.grid(row=10, column=0, columnspan=2, padx=10, pady=10, ipadx=50)
    update_btn = Button(data, text="update", command=update)
    update_btn.grid(row=11, column=0, columnspan=2, padx=10, pady=10, ipadx=50)

    print("Table created successfully")
    # commit chang
    conn.commit()
    # close connection
    conn.close()

    data.mainloop()

