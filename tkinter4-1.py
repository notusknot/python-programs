import tkinter
from tkinter import *
root = Tk()

scrollbar = Scrollbar(root, orient=VERTICAL)
listbox = Listbox(root, yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)
listbox.grid(row=0, column=0)

scrollbar.grid(row=0, column=1, sticky='ns')

colorList = ["purple", "red", "blue", "brown", "green", "orange", "yellow", "purple", "red", "blue", "brown", "green", "orange", "yellow"]

for loop in colorList:
    listbox.insert(END, loop)

colorLabel = Label(root, width=20)
colorLabel.grid(row=1, column=0, columnspan=1)

while True:
    selection = listbox.curselection()
    if len(selection) > 0:
        index = selection[0]
        colorLabel.config(bg=colorList[index])
        
    root.update()

root.mainloop()
