from tkinter import *
from tkinter import messagebox
import math
root=Tk()
root.title("Shopping cart")

cart = {}

def checkout():
    messagebox.showinfo("Grocery cart", cart)

def addCart():
    if len(Input.entry.get()) > 0:
        if num.get() > 0:
            cart[Input.entry.get()] = num.get()
            messagebox.showinfo("Grocery cart", Input.entry.get() + " was added")
            Input.entry.delete(0, END)
        else:
            messagebox.showwarning("Grocery cart", "Not enough items!")
    else:
        messagebox.showwarning("Grocery cart", "Please add an item!")

def addItem():
    num.set(num.get() + 1)

def removeItem():
    if num.get() > 0:
        num.set(num.get() - 1)

class LabelWithEntry:
    def __init__(self, text, row):
        self.label = Label(root, text = text)
        self.entry = Entry(root)
        self.label.grid(row=row, column=0, columnspan=3)
        self.entry.grid(row=row, column=3, columnspan=3)

num = IntVar()

Input = LabelWithEntry("Please enter an item", 0)

Label(root, text="Choose quantity").grid(row=1, column=0, columnspan=3)

minusButton = Button(root, text="-", fg="red", command=removeItem).grid(row=1, column=3)
Label(root, textvariable=num).grid(row=1, column=4)
plusButton = Button(root, text="+", fg="green", command=addItem).grid(row=1, column=5)

checkoutButton = Button(root, text="Checkout", fg="red", command=checkout).grid(row=3, column=0, columnspan=3)
addButton = Button(root, text="Add to cart", fg="blue", command=addCart).grid(row=3, column=3, columnspan=3)

root.mainloop()
