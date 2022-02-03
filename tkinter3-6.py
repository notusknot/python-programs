from tkinter import *
root = Tk()
root.title("Groceries")

last = 1
checkBoxes = []
checkVars = []

groceryList = { 'Milk':3.39,
                'Chocolates':2.09,
                'Eggs':6.99,
                'Bread':4.29,
                'Fruits':1.79
              }

Frame1 = Frame(root)
Frame2 = Frame(root)

chooseLabel = Label(Frame1, text="Choose the items that you want to buy").grid(row=0, column=0, columnspan=2)

class LabelWithEntry:
    def __init__(self, frame, text, row):
        self.label = Label(frame, text = text)
        self.entry = Spinbox(frame, from_=0,to=100)
        self.label.grid(row=row, column=0)
        self.entry.grid(row=row, column=1, columnspan=3)

def clear():
    for loop in checkBoxes:
        loop.deselect()

def checkout():
    pass

def frameChange():
    global groceryList
    for var in checkVars:
        if var.get() != '1':
            del groceryList[var.get()]
    Frame1.destroy()
    row = 0
    for item in groceryList:
        itemLabel = LabelWithEntry(Frame2, item, row)
        row += 1
    checkoutBtn = Button(Frame2, text="Checkout", command=checkout).grid(row=row, column=2)
    Frame2.pack()
    
for item in groceryList:
    checkVar = StringVar()
    checkVar.set(item)
    btn = Checkbutton(Frame1, text=item, variable=checkVar)
    checkVars.append(checkVar)
    checkBoxes.append(btn)
    btn.grid(column=0, columnspan=2)
    last += 1

clearBtn = Button(Frame1, text="Clear", command=clear).grid(row=last, column=0)
nextBtn = Button(Frame1, text="Next", command=frameChange).grid(row=last, column=1)
    
Frame1.pack()
    

root.mainloop()
