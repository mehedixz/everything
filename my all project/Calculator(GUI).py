from tkinter import *

root = Tk()
root.title("CALCULATOR")
root.geometry("336x308")

# Create main function


def click(event):

    global screen_value
    text = event.widget.cget("text")

    try:
        if text == "=":
            value = eval(screen.get())
            screen_value.set(value)
            screen.update()

        elif text == "C":
            screen_value.set("")
            screen.update()

        elif text == "Hi !":
            screen_value.set("HELLO, WELLCOME!")

        else:
            screen_value.set(screen_value.get()+text)
            screen.update()
    except:
        screen_value.set("Error")
        screen.update()


# Entry field
screen_value = StringVar()
screen_value.set("")
screen = Entry(root, textvariable = screen_value , font = "ArialBlack 22 bold", bd = 5,fg = "black", relief = "sunken")
screen.grid(row = 0, columnspan = 4)

# All button
# First row
button = Button(root, text = "7", font = "lucida 15 bold", width = 6, bd = 3)
button.grid(row = 1, column = 0 )
button.bind("<Button-1>", click)

button = Button(root, text = "8", font = "lucida 15 bold", width = 6, bd = 3)
button.grid(row = 1, column = 1 )
button.bind("<Button-1>", click)

button = Button(root, text = "9", font = "lucida 15 bold", width = 6, bd = 3)
button.grid(row = 1, column = 2 )
button.bind("<Button-1>", click)

button = Button(root, text = "+", font = "lucida 15 bold", width = 6, bd = 3, bg = "pink", fg = "blue")
button.grid(row = 1, column = 3 )
button.bind("<Button-1>", click)

# Second row
button = Button(root, text = "4", font = "lucida 15 bold", width = 6, bd = 3)
button.grid(row = 2, column = 0 )
button.bind("<Button-1>", click)

button = Button(root, text = "5", font = "lucida 15 bold", width = 6, bd = 3)
button.grid(row = 2, column = 1 )
button.bind("<Button-1>", click)

button = Button(root, text = "6", font = "lucida 15 bold", width = 6, bd = 3)
button.grid(row = 2, column = 2 )
button.bind("<Button-1>", click)

button = Button(root, text = "-", font = "lucida 15 bold", width = 6, bd = 3, bg = "pink", fg = "blue")
button.grid(row = 2, column = 3 )
button.bind("<Button-1>", click)

# Third row
button = Button(root, text = "1", font = "lucida 15 bold", width = 6, bd = 3)
button.grid(row = 3, column = 0)
button.bind("<Button-1>", click)

button = Button(root, text = "2", font = "lucida 15 bold", width = 6, bd = 3)
button.grid(row = 3, column = 1)
button.bind("<Button-1>", click)

button = Button(root, text = "3", font = "lucida 15 bold", width = 6, bd = 3)
button.grid(row = 3, column = 2 )
button.bind("<Button-1>", click)

button = Button(root, text = "*", font = "lucida 15 bold", width = 6, bd = 3, bg = "pink", fg = "blue")
button.grid(row = 3, column = 3 )
button.bind("<Button-1>", click)

# Fourth row
button = Button(root, text = "(", font = "lucida 15 bold", width = 6, bd = 3)
button.grid(row = 4, column = 0 )
button.bind("<Button-1>", click)

button = Button(root, text = "0", font = "lucida 15 bold", width = 6, bd = 3)
button.grid(row = 4, column = 1 )
button.bind("<Button-1>", click)

button = Button(root, text = ")", font = "lucida 15 bold", width = 6, bd = 3)
button.grid(row = 4, column = 2 )
button.bind("<Button-1>", click)

button = Button(root, text = "/", font = "lucida 15 bold", width = 6, bd = 3, bg = "pink", fg = "blue")
button.grid(row = 4, column = 3)
button.bind("<Button-1>", click)

# Fifth row
button = Button(root, text = "C", font = "lucida 15 bold", width = 6, bd = 3)#, bg = "yellow")
button.grid(row = 5, column = 0)
button.bind("<Button-1>", click)

button = Button(root, text = ".", font = "lucida 15 bold", width = 6, bd = 3)
button.grid(row = 5, column = 1)
button.bind("<Button-1>", click)

button = Button(root, text = "=", font = "lucida 15 bold", width = 6, bd = 3)#, bg = "yellow")
button.grid(row = 5, column = 2)
button.bind("<Button-1>", click)

button = Button(root, text = "Hi !", font = "lucida 15 bold", width = 6, bd = 3, bg = "blue", fg = "white")
button.grid(row = 5, column = 3)
button.bind("<Button-1>", click)

# Sixth row
label = Label(root , text = "Calculator", font = ("Franklin Gothic Medium",20,"bold"))
label.grid(row = 6, columnspan = 4)


root.mainloop()
