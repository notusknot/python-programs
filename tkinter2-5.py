from tkinter import *
from tkinter import messagebox
import random
root=Tk()
root.title("Color Game")

words = { 'green':'yellow', 'purple':'orange', 'blue':'red', 'yellow':'lightblue' }

score = IntVar()
score.set(0)
scoreLabel = Label(root, textvariable=score).grid(row=10, column=0)

def clear():
    Input.entry.delete(0, END)

def guess():
    global score
    x = Input.entry.get()
    if x == word[0]:
        message = "correct"
        score.set(score.get() + 1)
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
wordLabel = Label(root, text=word[1], fg=word[0]).grid(row=3, column=0)

calculateButton = Button(root, text="Guess", fg="green", command=guess)
calculateButton.grid(row=7, column=0)

clearButton = Button(root, text="Clear", fg="blue", command=clear)
clearButton.grid(row=7, column=1)

quitButton = Button(root, text="Quit", fg="red", command=exit)
quitButton.grid(row=7, column=2)

root.mainloop()
