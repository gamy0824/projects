BACKGROUND_COLOR = "#B1DDC6"
from asyncio.windows_events import NULL
from cgitb import text
from email.mime import image
from tkinter import *
from turtle import bgcolor, color, title
from random import *
import pandas as pd




app = Tk()
app.config(bg=BACKGROUND_COLOR)
app.title("Flash")
app.config(padx=55,pady= 55)

def french():
    f = pd.read_csv("data/french_words.csv")
    file = pd.DataFrame.to_dict(f)
    h = (choice(file["French"]))
    canvas.itemconfig(french_title, text= "French")
    canvas.itemconfig(french_words, text = h)


# pic1 = PhotoImage(file="images\right.png")

#label

# lb = Label(text="",font="carosello")
# lb.grid(column=0,row=0)

# front canvas
canvas = Canvas(width=800,height=526)
canvas_pic = PhotoImage(file="images\card_front.png")
canvas.create_image(400,263,image= canvas_pic)
canvas.config(bg=BACKGROUND_COLOR,highlightthickness=0)
french_title = canvas.create_text(400,100,text="",font= ("ariel", 40, "italic"))
french_words = canvas.create_text(400,263,text= "",font= ("ariel", 50, "bold"))
canvas.grid(column=1,row=1,columnspan=2)


# Button 
pic = PhotoImage(file="images/wrong.png")
bt = Button(image= pic,highlightthickness=0,command=french)
bt.grid(column=1,row=2)

pic1 = PhotoImage(file="images/right.png")
bt1 = Button(image=pic1,highlightthickness=0,command=french)
bt1.grid(column=2,row=2)

french()

app.mainloop()
