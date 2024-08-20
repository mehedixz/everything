from tkinter import *
from datetime import datetime
import time

root = Tk()
root.title("BIRTHDAY FINDER")
root.geometry("320x200")


def calculate_age():
    date_str = entry.get()
    birthday = datetime.strptime(date_str,"%d/%m/%Y")

    now = datetime.now()
    curr_year = datetime(now.year,birthday.month,birthday.day)
    days = (curr_year - now).days

    if days < 0:
        next_year = datetime(now.year+1,birthday.month,birthday.day)
        days = (next_year - now).days

    birth["text"] = f"YOUR BIRTHDAY IS COMING IN {days} DAY'S\nTHANK’S"


label1 = Label(text = "WELLCOME TO BIRTHDAY FINDER!",font = ("Arial Black",12))
label2 = Label(text = "PLZ ENTER YOUR BIRTH: (DD/MM/YY)",bg = "pink",font = ("Franklin Gothic Medium",10))
label3 = Label(text = "")
button = Button(text = "CLICK FOR BIRTHDAY",bd = 4,bg = "yellow",command = calculate_age,font = ("Franklin Gothic Medium",8))
birth = Label()
entry = Entry(root,bd = 2,width=22, fg = "blue")

label1.pack()
label3.pack()
label2.pack()
entry.pack()
button.pack()
birth.pack()

root.mainloop()
