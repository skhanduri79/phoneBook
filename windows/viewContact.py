from tkinter import *
from tkinter import Button
import sqlite3
from windows.addContact import addContact
from windows.updateContact import updateContact
from windows.displayContact import displayContact
from tkinter import messagebox

con  = sqlite3.connect('../database/database.db')
cur = con.cursor

class myContact(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)

        self.title("My Contact")
        self.geometry("650x650+600+200")
        self.resizable(False,False)

         # frames

        self.top = Frame(self,height=150, bg= 'white')
        self.top.pack(fill=X)

        self.bottom = Frame(self,height=650,bg='#34eb34')
        self.bottom.pack(fill=X)

         # top frame heading     
        self.heading = Label(self.top, text = "My Contacts", font = 'arial 18 bold', fg='red', bg='white')
        self.heading.place(x=270,y=50) 

        self.scroll = Scrollbar(self.bottom, orient=VERTICAL)

        # listbox
        self.listbox = Listbox(self.bottom, width=40, height=27)
        self.listbox.grid(row=0, column=0, padx=(40,0))
        self.scroll.config(command=self.listbox.yview)
        self.listbox.config(yscrollcommand=self.scroll.set)

        contacts = con.execute("select * from 'addressBook'").fetchall()
        print(contacts)
        count=0
        for contact in contacts:
          self.listbox.insert(count, str(contact[0])+"."+contact[1]+" "+contact[2])
          count+=1

        self.scroll.grid(row=0,column=0,sticky=N+S)

       # buttons
    
        self.btnAdd = Button(self.bottom, text='ADD', width=12, font='Sans 16 bold', command = self.add_contact).grid(row=0, column=2,padx=20, pady=10, sticky=N)

        self.btnUpdate = Button(self.bottom, text='UPDATE', width=12, font='Sans 16 bold', command=self.update_contact).grid(row=0, column=2,padx=20, pady=50, sticky=N)

        self.btnDisplay = Button(self.bottom, text='DISPLAY', width=12, font='Sans 16 bold', command=self.display_contact).grid(row=0, column=2,padx=20, pady=90, sticky=N)

        self.btnDelete = Button(self.bottom, text='DELETE', width=12, font='Sans 16 bold', command=self.delete_contact).grid(row=0, column=2,padx=20, pady=130, sticky=N)

    def add_contact(self):
      contact = addContact()  
      self.destroy() 

    def update_contact(self):
      selected_item = self.listbox.curselection()  
      person = self.listbox.get(selected_item)
      person_id=person.split(".")[0]
      
      update_page = updateContact(person_id)

    def display_contact(self):
        selected_item = self.listbox.curselection()
        person = self.listbox.get(selected_item)
        person_id = person.split(".")[0]

        display_page = displayContact(person_id)
    def delete_contact(self):
        selected_item = self.listbox.curselection()
        person = self.listbox.get(selected_item)
        person_id = person.split(".")[0]

        query= "delete from addressbook where person_id={}".format(person_id)
        string_for_mbox = "are you sure you want to delete", person.split(".")[1], "?"
        answer= messagebox.askquestion("Warning", "Are you sure you want to delete?")
        if answer== 'yes':
            try:
                con.execute(query)
                con.commit()
                messagebox.showinfo("Success !!", "Deleted")
                self.destroy()

            except Exception as e:
                messagebox.showinfo("info", str(e))
    