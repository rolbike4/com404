from tkinter import *
import time

class Gui(Tk):

    def __init__(self):
        super().__init__()

        self.ball_image = PhotoImage(file="U:\\practice tca\\ball.gif")
        self.ball2_image = PhotoImage(file="U:\\practice tca\\ball2.gif")

        self.configure(height=500,
                       width=500)

        self.ball_x_pos = 500
        self.ball_y_pos = 0
        self.ball_x_change = 5
        self.ball_y_change = 5

        self.ball2_x_pos = 0
        self.ball2_y_pos = 500
        self.ball2_x_change = 5
        self.ball2_y_change = 5

        

        self.__add_ball_image_label()
        self.__add_ball2_image_label()

        self.tick()

    def tick(self):

        if self.ball_x_pos >= 500:
            self.ball_x_change = self.ball_x_change * -1
            
        if self.ball_y_pos >= 500:
            self.ball_y_change = self.ball_y_change * -1

        if self.ball_x_pos <= 0:
            self.ball_x_change = self.ball_x_change * -1

        if self.ball_y_pos <= 0:
            self.ball_y_change = self.ball_y_change * -1


        if self.ball2_x_pos >= 500:
            self.ball2_x_change = self.ball2_x_change * -1
            
        if self.ball2_y_pos >= 500:
            self.ball2_y_change = self.ball2_y_change * -1

        if self.ball2_x_pos <= 0:
            self.ball2_x_change = self.ball2_x_change * -1

        if self.ball2_y_pos <= 0:
            self.ball2_y_change = self.ball2_y_change * -1
        
        self.ball_x_pos = self.ball_x_pos + self.ball_x_change
        self.ball_y_pos = self.ball_y_pos + self.ball_y_change
        self.ball_image_label.place(x=self.ball_x_pos, 
                                    y=self.ball_y_pos)
       

        self.ball2_x_pos = self.ball2_x_pos + self.ball2_x_change
        self.ball2_y_pos = self.ball2_y_pos + self.ball2_y_change
        self.ball2_image_label.place(x=self.ball2_x_pos,
                                     y=self.ball2_y_pos)


        self.after(100, self.tick)



    def __add_ball_image_label(self):
        self.ball_image_label = Label()
        self.ball_image_label.place(x=self.ball_x_pos, 
                                    y=self.ball_y_pos)
        self.ball_image_label.configure(image=self.ball_image)

    def __add_ball2_image_label(self):
        self.ball2_image_label = Label()
        self.ball2_image_label.place(x=self.ball2_x_pos,
                                     y=self.ball2_y_pos)
        self.ball2_image_label.configure(image=self.ball2_image)
        
if __name__ == "__main__":
    gui = AnimatedGui()    
    gui.mainloop() 
