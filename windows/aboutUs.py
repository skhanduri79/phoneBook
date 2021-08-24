from tkinter import*

class aboutUs(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)

        self.title("About Us")
        self.geometry("650x550+490+190")
        self.resizable(False,False)

        # frames

        self.top = Frame(self,height=650,width=550, bg= 'pink')
        self.top.pack(fill=BOTH)

        # label

        self.text=Label(self.top, text="Hey!! "
                                       "\n"
                        "This application is made by Sakshi Khanduri."
                        "\n"
                        "This gui application is made with Tkinter python.", font='arial 14 bold', fg="black").place(x=50,y=50)


