from tkinter import *
from datetime import datetime
import time

root = Tk()
root.title("AGE FINDER")
root.geometry("300x200")


def calculate_age():
    date_str = entry.get()
    birthday = datetime.strptime(date_str,"%d/%m/%Y")

    now = datetime.now()
    days = (now - birthday).days
    age = days//365

    years["text"] = f"YOUR AGE IS {age} YEAR’S \nTHANK’S"


label1 = Label(text = "WELLCOME TO AGE FINDER!",font = ("Arial Black",12))
label2 = Label(text = "PLZ ENTER YOUR BIRTHDAY: (DD/MM/YY)",bg = "pink",font = ("Franklin Gothic Medium",10))
label3 = Label(text = "")
button = Button(text = "CLICK FOR AGE",bd = 4,bg = "yellow",command = calculate_age,font = ("Franklin Gothic Medium",10))
years = Label()
entry = Entry(root,bd = 2, fg = "blue")

label1.pack()
label3.pack()
label2.pack()
entry.pack()
button.pack()
years.pack()


root.mainloop()

