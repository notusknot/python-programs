import tkinter
from tkinter import messagebox
from tkinter import *
root = Tk()
root.title("Phone book")

phonebookDict = {}

class LabelWithEntry:
    def __init__(self, text, row):
        self.label = Label(root, text = text)
        self.entry = Entry(root)
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

def add():
    name = nameInput.get()
    phone = phoneInput.get()
    
    if name in phonebookDict:
        messagebox.showwarning("Phone book", "Name already registered")
        return
    
    if phone.isnumeric() and len(phone) == 10:
        for loop in phonebookDict:
            if phonebookDict[loop] == phone:
                messagebox.showwarning("Phone book", "Phone number already registered")
                return
        nameInput.delete()
        phonebookDict[name] = phone
        messagebox.showinfo("Phone book", "Successfully added number")
        phoneInput.delete()
    else:
        messagebox.showwarning("Phone book", "Please enter a valid phone number, no spaces or dashes")
    updateListbox()

def updateListbox():
    phonebookListbox.delete(0, END)
    for loop in phonebookDict:
        phonebookListbox.insert(END, loop)
    root.update()

def load():
    selection = phonebookListbox.curselection()
    if len(selection) == 0:
        messagebox.showwarning("Phone book", "Nothing selected")
        return
    index = selection[0]
    name = phonebookListbox.get(index)
    nameInput.add(name)
    phoneInput.add(phonebookDict[name])
    return name

def delete():
    name = load()
    if name == None:
        return
    del phonebookDict[name]
    updateListbox()

def update():
    name = nameInput.get()
    phone = phoneInput.get()
    if phone.isnumeric() and len(phone) == 10:
        nameInput.delete()
        if not name in phonebookDict:
            phonebookDict[name] = phone
        messagebox.showinfo("Phone book", "Successfully added number")
        phoneInput.delete()
    else:
        messagebox.showwarning("Phone book", "Please enter a valid phone number, no spaces or dashes")
    updateListbox()

nameInput = LabelWithEntry("Name", 0)
phoneInput = LabelWithEntry("Phone", 1)

addButton = Button(root, text="Add", command=add).grid(row=2, column=0)
loadButton = Button(root, text="Load", command=load).grid(row=2, column=1)
deleteButton = Button(root, text="Delete", command=delete).grid(row=2, column=2)
updateButton = Button(root, text="Update", command=update).grid(row=2, column=3)

scrollbar = Scrollbar(root, orient=VERTICAL)
phonebookListbox = Listbox(root, yscrollcommand=scrollbar.set)
scrollbar.config(command=phonebookListbox.yview)
scrollbar.grid(sticky='ns', column=3)
phonebookListbox.grid(row=3, column=0, columnspan=4)



