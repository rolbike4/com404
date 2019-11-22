# gui.py

from tkinter import *

class Gui(Tk):

    def __init__(self):
        super().__init__()

        self.__add_outer_frame()
        self.__add_heading_label()
        self.__add_instruction_label()
        self.__add_lyric_frame()
        self.__add_lyric_entry()
        self.__add_add_button()
        self.__add_instruction2_label()
        self.__add_lyrics_listbox()




    def __add_outer_frame(self):
        self.outer_frame = Frame()
        self.outer_frame.grid(row=0, column=0)
        self.outer_frame.configure( bg="#eee", 
                                    padx=10, 
                                    pady=10)

    def __add_heading_label(self):
        self.heading_label = Label(self.outer_frame)
        self.heading_label.grid(row=0, column=0, sticky=E)
        self.heading_label.configure(   bg="#eee",
                                        font="Arial 18",
                                        text="Song Maker")

    def __add_instruction_label(self):
        self.instruction_label = Label(self.outer_frame)
        self.instruction_label.grid(row=1, column=0, columnspan=2, sticky=W)
        self.instruction_label.configure(   bg="#eee",
                                            text="Lyrics to add:")
    def __add_lyric_frame(self):
        self.lyric_frame = Frame(self.outer_frame)
        self.lyric_frame.grid(row=2, column=0)

    def __add_lyric_entry(self):
        self.lyric_entry = Entry(self.lyric_frame)
        self.lyric_entry.pack(side=LEFT)
        self.lyric_entry.configure(text="")

    def __add_add_button(self):
        self.add_button = Button(self.lyric_frame)
        self.add_button.pack(side=RIGHT)
        self.add_button.configure(width=10,
                                        text="Add")
        self.add_button.bind("<ButtonRelease-1>", self.__add_button_clicked)
        
    def __add_button_clicked(self, event):
        new_lyrics=self.lyric_entry.get()
        self.lyrics_listbox.insert(END, new_lyrics)

    def __add_instruction2_label(self):
        self.instruction2_label = Label(self.outer_frame)
        self.instruction2_label.grid(row=3, column=0, sticky=W)
        self.instruction2_label.configure(   bg="#eee",
                                            text="Lyrics")

    def __add_lyrics_listbox(self):
        self.lyrics_listbox = Listbox(self.outer_frame)
        self.lyrics_listbox.grid(row=4, column=0, columnspan=2)
        self.lyrics_listbox.configure(height=1)

        
