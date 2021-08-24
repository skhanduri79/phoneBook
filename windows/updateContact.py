from tkinter import *
import sqlite3
from tkinter import messagebox

con = sqlite3.connect('../database/database.db')


class updateContact(Toplevel):
    def __init__(self, person_id):
        Toplevel.__init__(self)

        self.title("Update Contact")
        self.geometry("650x550+500+220")
        self.resizable(False, False)

        query = "select * from addressBook where person_id = '{}'".format(person_id)
        result = con.execute(query).fetchone()
        print(result)
        self.person_id = person_id
        person_name = result[1]
        person_sirname = result[2]
        person_phone = result[3]
        person_email = result[4]
        person_add = result[5]
        # frames

        self.top = Frame(self, height=150, bg='white')
        self.top.pack(fill=X)

        self.bottom = Frame(self, height=400, bg='#4b35bd')
        self.bottom.pack(fill=X)

        # top frame heading
        self.heading = Label(self.top, text="Update Contacts", font='arial 15 bold', fg='red', bg='white')
        self.heading.place(x=250, y=50)

        # name
        self.name = Label(self.bottom, text="Name: ", font='arial 15 bold', fg='white', bg='#4b35bd')
        self.name.place(x=49, y=40)

        self.entry_name = Entry(self.bottom, width=30, bd=4)
        self.entry_name.insert(0, person_name)
        self.entry_name.place(x=200, y=40)

        # surname
        self.surname = Label(self.bottom, text="Last Name: ", font='arial 15 bold', fg='white', bg='#4b35bd')
        self.surname.place(x=49, y=80)

        self.entry_sirname = Entry(self.bottom, width=30, bd=4)
        self.entry_sirname.insert(0, person_sirname)
        self.entry_sirname.place(x=200, y=80)

        # email
        self.email = Label(self.bottom, text="email: ", font='arial 15 bold', fg='white', bg='#4b35bd')
        self.email.place(x=49, y=120)

        self.email_entry = Entry(self.bottom, width=30, bd=4)
        self.email_entry.insert(0, person_email)
        self.email_entry.place(x=200, y=120)

        # phone number
        self.phno = Label(self.bottom, text="phone number: ", font='arial 15 bold', fg='white', bg='#4b35bd')
        self.phno.place(x=49, y=160)

        self.phno_entry = Entry(self.bottom, width=30, bd=4)
        self.phno_entry.insert(0, person_phone)
        self.phno_entry.place(x=200, y=160)

        # address
        self.address = Label(self.bottom, text="Address: ", font='arial 15 bold', fg='white', bg='#4b35bd')
        self.address.place(x=49, y=200)

        self.address_entry = Text(self.bottom, width=30, height=8)
        self.address_entry.insert(1.0, person_add)
        self.address_entry.place(x=200, y=200)

        # button submit
        self.btnsubmit = Button(self.bottom, text="UPDATE ", font='arial 15 bold', fg='white', bg='#951cad',
                                command=self.update_people)
        self.btnsubmit.place(x=210, y=340)

    def update_people(self):
        id = self.person_id
        name = self.entry_name.get()
        sirname = self.entry_sirname.get()
        email = self.email_entry.get()
        phone = self.phno_entry.get()
        address = self.address_entry.get(1.0, 'end-1c')
        query = "update addressBook set  person_name='{}',person_lastname = '{}',person_email = '{}',person_phone ='{" \
                "}',person_address='{}' where person_id = {}".format(
            name, sirname, email, phone, address, id)

        try:
            con.execute(query)
            con.commit()
            messagebox.showinfo("Success", "Contact Updated")

        except Exception as e:
            print(e)
