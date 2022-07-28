from tkinter import *
import requests

r = requests.get("https://api.kanye.rest")
data =r.json()["quote"]


def quote():
    r = requests.get("https://api.kanye.rest")
    r.raise_for_status()
    data =r.json()["quote"]
    canvas.itemconfig(texto,text=data)
app = Tk()
app.title("Me llagaron primero que Kanye")
app.minsize(width=350,height=600)
pic = PhotoImage(file="background.png")
canvas = Canvas(width=300,height=414)
canvas.create_image(150,207,image=pic)
texto = canvas.create_text(150,207,text="mete aqui la vuelta",width=150,font=("arial",30,"bold"),fill="black")
canvas.grid(column=0,row=0)

pic1 = PhotoImage(file="kanye.png")

#
bt = Button(image=pic1,command=quote)
bt.grid(column=0,row=1)

app.mainloop()