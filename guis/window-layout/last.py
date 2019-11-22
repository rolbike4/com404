# gui.py

from tkinter import *

class Gui(Tk):

    def __init__(self):
        super().__init__()

        self.__add_outer_frame()
        self.__add_heading_label()
        self.__add_q1_label()
        self.__add_yes_checkbutton()
        self.__add_no_checkbutton()
        self.__add_q2_label()
        self.__add_yes2_checkbutton()
        self.__add_no2_checkbutton()
        
        




    def __add_outer_frame(self):
        self.outer_frame = Frame()
        self.outer_frame.grid(row=0, column=0)
        self.outer_frame.configure( bg="#eee", 
                                    padx=10, 
                                    pady=10)


    def __add_heading_label(self):
        self.heading_label = Label(self.outer_frame)
        self.heading_label.grid(row=0, column=0, columnspan=3)
        self.heading_label.configure(   bg="#eee",
                                        font="Arial 18",
                                        text="Passport Checker")

    def __add_q1_label(self):
        self.q1_label = Label(self.outer_frame)
        self.q1_label.grid(row=1, column=0)
        self.q1_label.configure(   bg="#eee",
                                        font="Arial 12",
                                        text="Photo matches face?")

    def __add_yes_checkbutton(self):
        self.yes_checkbutton= Checkbutton(self.outer_frame)
        self.yes_checkbutton.grid(row=1, column=1)
        self.yes_checkbutton.configure(text="yes")

    def __add_no_checkbutton(self):
        self.no_checkbutton= Checkbutton(self.outer_frame)
        self.no_checkbutton.grid(row=1, column=2)
        self.no_checkbutton.configure(text="no")


    def __add_q2_label(self):
        self.q2_label = Label(self.outer_frame)
        self.q2_label.grid(row=2, column=0)
        self.q2_label.configure(   bg="#eee",
                                        font="Arial 12",
                                        text="Passport has at least 6 months validity?")

    def __add_yes2_checkbutton(self):
        self.yes2_checkbutton= Checkbutton(self.outer_frame)
        self.yes2_checkbutton.grid(row=2, column=1)
        self.yes2_checkbutton.configure(text="yes")

    def __add_no2_checkbutton(self):
        self.no2_checkbutton= Checkbutton(self.outer_frame)
        self.no2_checkbutton.grid(row=2, column=2)
        self.no2_checkbutton.configure(text="no")
        

    def __add_q3_label(self):
        self.q3_label = Label(self.outer_frame)
        self.q3_label.grid(row=2, column=0)
        self.q3_label.configure(   bg="#eee",
                                        font="Arial 12",
                                        text="Passport has at least 6 months validity?")

    def __add_yes3_checkbutton(self):
        self.yes3_checkbutton= Checkbutton(self.outer_frame)
        self.yes3_checkbutton.grid(row=2, column=1)
        self.yes3_checkbutton.configure(text="yes")

    def __add_no3_checkbutton(self):
        self.no3_checkbutton= Checkbutton(self.outer_frame)
        self.no3_checkbutton.grid(row=2, column=2)
        self.no3_checkbutton.configure(text="no")
        
