from tkinter import *
from tkinter import messagebox
import random
root=Tk()
root.title("Number game")

def clear():
    Input.entry.delete(0, END)

def guess():
    x = int(Input.entry.get())
    if num == x:
        message = "Correct!"
    elif num > x:
        message = "The number is greater than your guess"
    else:
        message = "The number is less than your guess"

    m = messagebox.showinfo("Result",message)

class LabelWithEntry:
    def __init__(self, text, row):
        self.label = Label(root, text = text)
        self.entry = Entry(root)
        self.label.grid(row=row, column=0)
        self.entry.grid(row=row, column=1)

num = random.randint(1, 100)

Input = LabelWithEntry("Guess number 1-100", 0)

calculateButton = Button(root, text="Guess", fg="green", command=guess)
calculateButton.grid(row=6, column=0)

clearButton = Button(root, text="Clear", fg="blue", command=clear)
clearButton.grid(row=6, column=1)

quitButton = Button(root, text="Quit", fg="red", command=exit)
quitButton.grid(row=6, column=2)

root.mainloop()
