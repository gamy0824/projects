THEME_COLOR = "#375362"
from tkinter import *

class QuizInterface:
    def __init__(self):
        self.windows = Tk()
        self.windows.title("Trivia")
        self.windows.config(bg=THEME_COLOR)

        lb_score = Label(text="Score: 0",fg="white",bg=THEME_COLOR)
        lb_score.grid(column=1,row=0)
        

        canvas
        self.canvas = Canvas(width=100,height=150)
        text = self.canvas.create_text(text ="hola mundo",fill=THEME_COLOR,font=("arial",20,"italic"))
        self.canvas.grid(column=0,row=0,columnspan=2)


        

        #Button
        false = PhotoImage("images/false.png")
        bt = Button(image=false)
        bt.grid(column=2,row=2)
        
        true = PhotoImage("images/true.png")
        bt1 = Button(image=true)
        bt1.grid(column=1,row=2)

        self.windows.mainloop()

