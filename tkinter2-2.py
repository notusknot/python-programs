from tkinter import *
from tkinter import messagebox
import math
root=Tk()
root.title("Square root")

def clear():
    numInput.entry.delete(0, END)

def square():
    num.set(int(numInput.entry.get())**2)

def squareRoot():
    num.set(round(math.sqrt(int(numInput.entry.get())),3))
    
def login():
    if nameInput.entry.get() in loginInfo:
        if loginInfo[nameInput.entry.get()] == passInput.entry.get():
            m1 = messagebox.showinfo("Access granted", "Access granted")
            clear()
            
        else:
            m2 = messagebox.showwarning("Access denied", "Incorrect password")

    else:
        m3 = messagebox.showerror("Access denied", "Incorrect username")

class LabelWithEntry:
    def __init__(self, text, row):
        self.label = Label(root, text = text)
        self.entry = Entry(root)
        self.label.grid(row=row, column=0)
        self.entry.grid(row=row, column=1)

num=DoubleVar()

Label(root, textvariable=num).grid(row=1, column=0, columnspan=2)

numInput = LabelWithEntry("Number", 0)

squareButton = Button(root, text="Square", fg="blue", command=square)
squareButton.grid(row=6, column=0)

sqrtButton = Button(root, text="Square root", fg="blue", command=squareRoot)
sqrtButton.grid(row=6, column=1)

root.mainloop()
