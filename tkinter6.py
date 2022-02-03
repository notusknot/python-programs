from tkinter import *
from tkinter import messagebox
root=Tk()
root.title("Login")

loginInfo = { 'admin1':'rootPassword', 'user1':'userPassword' }

def clear():
    nameInput.entry.delete(0, END)
    passInput.entry.delete(0, END)

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

Label(root, text="Please enter the following").grid(row=0, column=0, columnspan=2)

nameInput = LabelWithEntry("Username", 1)
passInput = LabelWithEntry("Password", 2)

calculateButton = Button(root, text="login", fg="blue", command=login)
calculateButton.grid(row=6, column=0)

clearButton = Button(root, text="Clear", fg="red", command=clear)
clearButton.grid(row=6, column=1)

root.mainloop()
