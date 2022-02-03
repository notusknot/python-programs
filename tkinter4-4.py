import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

root = Tk()
root.title("Login Application")

class LabelWithEntry:
    def __init__(self, frame, text, row):
        self.label = Label(frame, text = text)
        if "password" in text.lower():
            self.entry = Entry(frame, show="*")
        else:
            self.entry = Entry(frame)
        self.label.grid(row=row, column=0, columnspan=1)
        self.entry.grid(row=row, column=1, columnspan=3)
    def get(self):
        return self.entry.get()
    def delete(self):
        if len(self.get()) > 0:
            self.entry.delete(0, END)
    def add(self, string):
        self.delete()
        self.entry.insert(END, string)

loginInfo = {}

def login():
    if usernameLogin.get() not in loginInfo:
        messagebox.showerror("Login app", "Incorrect username")
    elif loginInfo[usernameLogin.get()] == passwordLogin.get():
        messagebox.showinfo("Login App", "Logged in")
        usernameLogin.delete()
        passwordLogin.delete()
    else:
        messagebox.showerror("Login app", "Incorrect password")

def register():
    if termsVar.get() == '0':
        messagebox.showerror("Register", "Please check the terms of service")
    elif usernameReg.get() in loginInfo:
        messagebox.showerror("Register", "Username taken")
    else:
        loginInfo[usernameReg.get()] = passwordReg.get()
        messagebox.showinfo("Register", "Successfully registered")
        usernameReg.delete()
        passwordReg.delete()

def unsub():
    if usernameUnsub.get() not in loginInfo:
        messagebox.showerror("Unsubscribe", "Incorrect username")
    elif loginInfo[usernameUnsub.get()] == passwordUnsub.get():
        messagebox.showinfo("Unsubscribe", "Unsubscribed")
        del loginInfo[usernameUnsub.get()]
        usernameUnsub.delete()
        passwordUnsub.delete()
    else:
        messagebox.showerror("Unsubscribe", "Incorrect password")

def reset():
    if usernameReset.get() not in loginInfo:
        messagebox.showerror("Reset password", "Username doesn't exist")
    elif loginInfo[usernameReset.get()] == passwordReset.get():
        loginInfo[usernameReset.get()] = newPasswordReset.get()
        messagebox.showinfo("Reset password", "Password successfully changed")
        usernameReset.delete()
        passwordReset.delete()
        newPasswordReset.delete()
    else:
        messagebox.showerror("Login app", "Incorrect password")

def showPass():
    if int(passCheckVar.get()) == 1:
        passwordReg.entry.config(show="")
    else:
        passwordReg.entry.config(show="*")

notebook = ttk.Notebook(root)
notebook.grid()

loginFrame = Frame(notebook)
regFrame = Frame(notebook)
resetFrame = Frame(notebook)
unsubFrame = Frame(notebook)

notebook.add(loginFrame, text="Login")
notebook.add(regFrame, text="Register")
notebook.add(resetFrame, text="Reset")
notebook.add(unsubFrame, text="Unsubscribe")

# Login Frame

usernameLogin = LabelWithEntry(loginFrame, "Username", 0)
passwordLogin = LabelWithEntry(loginFrame, "Password", 1)

Button(loginFrame, text="Log in", command=login).grid(row=5, column=1)

# Register Frame

passCheckVar = StringVar()
termsVar = StringVar()

usernameReg = LabelWithEntry(regFrame, "Username", 0)
passwordReg = LabelWithEntry(regFrame, "Password", 1)

Button(regFrame, text="Register", command=register).grid(row=5, column=1)

showPassCheckbox = Checkbutton(regFrame, text="Show password", variable=passCheckVar, command=showPass).grid(row=2,column=2)
termsCheckbox = Checkbutton(regFrame, text="Accept terms and conditions", variable=termsVar).grid(row=4, column=0)

# Unsubscribe

usernameUnsub = LabelWithEntry(unsubFrame, "Username", 0)
passwordUnsub = LabelWithEntry(unsubFrame, "Password", 1)

Button(unsubFrame, text="Unsubscribe", command=unsub).grid(row=5, column=1)

# Reset Frame

usernameReset = LabelWithEntry(resetFrame, "Username", 0)
passwordReset = LabelWithEntry(resetFrame, "Old password", 1)
newPasswordReset = LabelWithEntry(resetFrame, "New password", 2)

Button(resetFrame, text="Reset", command=reset).grid(row=5, column=1)

