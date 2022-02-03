from tkinter import *
from tkinter import messagebox
import random
root=Tk()
root.title("Number game")

words = { 'treehouse':'ohuserete', 'pineapple':'appineepl', 'window':'wowdni', 'truck':'rtcuk' }


def clear():
    Input.entry.delete(0, END)

def guess():
    x = Input.entry.get()
    if x == word[0]:
        message = "correct"
        clear()
    else:
        message = "incorrect"
        clear()

    m = messagebox.showinfo("Result",message)

class LabelWithEntry:
    def __init__(self, text, row):
        self.label = Label(root, text = text)
        self.entry = Entry(root)
        self.label.grid(row=row, column=0)
        self.entry.grid(row=row, column=1)

num = random.randint(1, 100)

Input = LabelWithEntry("Guess the word", 0)

word = list(random.choice(list(words.items())))
wordLabel = Label(root, text=word[1]).grid(row=2, column=0)

calculateButton = Button(root, text="Guess", fg="green", command=guess)
calculateButton.grid(row=6, column=0)

clearButton = Button(root, text="Clear", fg="blue", command=clear)
clearButton.grid(row=6, column=1)

quitButton = Button(root, text="Quit", fg="red", command=exit)
quitButton.grid(row=6, column=2)

root.mainloop()
