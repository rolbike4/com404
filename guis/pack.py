from tkinter import *

class Gui(Tk):
    def __init__(self):
        super().__init__()
        
        self.title("Newsletter")
        self.configure(bg="#000",
                       height=500,
                       width=500,)
        self.__add_heading_label()
        self.__add_sentence_label()
        self.__add_email_frame()
        self.__add_email_label()
        self.__add_email_entry()
        self.__add_subscribe_button()

   def __add_email_frame(self):
        self.email_frame = Frame()
        self.email_frame.pack(fill=X)
        self.email_frame.configure(bg="#000")
        
        
    def __add_heading_label(self):
        self.heading_label = Label()
        self.heading_label.grid(row=2, column=3, columnspan=2)
        #self.heading_label.pack(fill=X)
        #self.heading_label.place(x=80,y=20)
        self.heading_label.configure(font="Arial 24",
                                     text="Received our newsletter.",
                                     bg="#000",
                                     fg="#f00")

    def __add_sentence_label(self):
        self.sentence_label = Label()
        self.sentence_label.grid(row=1, column=3, columnspan=2)
        #self.sentence_label.pack(fill=X)
        #self.sentence_label.place(x=80,y=60)
        self.sentence_label.configure(font="Arial 16",
                                          text="Please enter your email adress.",
                                          bg="#000",
                                          fg="#ff0")


    def __add_email_label(self):
        self.email_label = Label()
        self.email_label.grid(row=3, column=2, columnspan=2)
        #self.email_label.pack(side=LEFT)
        #self.email_label.place(x=80,y=100)
        self.email_label.configure(font="Arial 14",
                                   text="Email:",
                                   bg="#000",
                                   fg="#ff0")

    def __add_email_entry(self):
        self.email_entry = Entry()
        #self.email_entry.place(x=150,y=105)
       # self.email_entry.pack(side=RIGHT)

    def __add_subscribe_button(self):
        self.subscribe_button = Button()
        #self.subscribe_button.place(x=150,y=160)
        #self.subscribe_button.pack(fill=X)
        self.subscribe_button.configure(width=16,
                                    height=1,
                                    text="Subscribe")
        
