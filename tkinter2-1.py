from tkinter import *
import random
root = Tk()
root.title("Random numbers")

def genNum():
    numRange = Input.entry.get().split('-')
    num=random.randint(int(numRange[0]),int(numRange[1]))
    result.set(num)

class LabelWithEntry:
    def __init__(self, text, row):
        self.label = Label(root, text = text)
        self.entry = Entry(root)
        self.label.grid(row=row, column=0)
        self.entry.grid(row=row, column=1)

Input = LabelWithEntry("Enter a range", 0)

result = StringVar()
result.set(100)

resultLabel = Label(root, textvariable=result).grid(row=1, column=1)

genBtn = Button(root, text="Generate", command=genNum).grid(row=2, column=1)

root.mainloop()
