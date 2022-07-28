# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
import email
from nntplib import GroupInfo
from tkinter import *
from turtle import color

#windows
app = Tk()
app.title("Passoword Manager")
app.config(padx=50,pady=50,bg="black")

# canvas
canvas = Canvas(width=200,height=200,bg="black",highlightthickness=0)
canvas.grid(column=1,row=0)
# imagen
image = PhotoImage(file="logo.png")
canvas.create_image(100,100,image=image)

# Label

web = Label(text="Website:")
web.grid(row=1,column=0)
email = Label(text="Email/User:")
email.grid(row=2,column=0)
password = Label(text="Password:")
password.grid(row=3,column=0)

# entries
website = Entry(width=35)
website.grid(row=1,column=1,columnspan=2)
website.focus()
user_email = Entry(width=35)
user_email.grid(row=2,column=1,columnspan=2)
user_email.insert(END,"yoryimgrullon@gmail.com")
password_text = Entry(width=21)
password_text.grid(row=3,column=1)

# Button
bt = Button(text="Password Generrator")
bt.grid(row=3,column=2)
bt1 = Button(text="ADD",width=36)
bt1.grid(row=4,column=1,columnspan=2) 










app.mainloop()