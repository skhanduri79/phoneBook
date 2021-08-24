from tkinter import*
import datetime
from viewContact import myContact
from windows.addContact import addContact
from windows.aboutUs import aboutUs

date = datetime.datetime.now().date()
date = str(date)

class Application(object):
    def __init__(self,master):
        self.master = master

        # frames

        self.top = Frame(master,height=150, bg= 'white')
        self.top.pack(fill=X)

        self.bottom = Frame(master,height=400,bg='#966093')
        self.bottom.pack(fill=X)

        # top frame design 
        self.top_img = PhotoImage(file='../icons/icon2.png')
        self.top_img_label = Label(self.top, image=self.top_img)
        self.top_img_label.place(x=170,y=45)

        # top frame heading     
        self.heading = Label(self.top, text = "My PhoneBook", font = 'arial 18 bold', fg='red', bg='white')
        self.heading.place(x=250,y=50)   

        # date label
        self.date_label = Label(self.top,text = 'Date: '+date, fg='green', bg='white',font=' arial 12 italic')
        self.date_label.place(x=500,y=8)

        # button1: view contact

        self.btnView = Button(self.bottom, text ='     My contacts     ', font = 'arial 16 bold', fg="#3632a8", bg="white", command = self.view_Contact)
        self.btnView.place(x=270, y=70)

        # button2: add contact

        self.btnAdd = Button(self.bottom, text =' Add new contact ', font = 'arial 16 bold', fg="#3632a8", bg="white", command=self.add_contact)
        self.btnAdd.place(x=270, y=150)

        # button3: about us 

        self.btnAbout = Button(self.bottom, text ='        About Us       ', font = 'arial 16 bold', fg='#3632a8', bg="white", command=self.about_us)
        self.btnAbout.place(x=270, y=220)

    def view_Contact(self):
        contact = myContact()

    def add_contact(self): 
        contact=addContact()   

    def about_us(self):
        contact=aboutUs()


def main():
    root  = Tk()
    app = Application(root)
    root.title("Phonebook")
    root.geometry("650x550+450+200")
    root.resizable(False,False)
    root.mainloop()
 

if __name__=="__main__":
    main()