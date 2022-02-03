from tkinter import *
import random
root = Tk()
root.title("Password")

letters = []
numbers = []
specialChars = []

for i in range(97, 123, 1):
    letters.append(chr(i))

for i in range(65, 91, 1):
    letters.append(chr(i))

for i in range(0, 10, 1):
    numbers.append(str(i))

for i in range(33, 48, 1):
    specialChars.append(chr(i))

def low(l):
    if l <= 26*2:
        return ''.join(random.sample(letters, l))
    else:
        s = ''
        for loop in range(0, l, 1):
            s += random.choice(letters)
        return s

def medium(l):
    s = ''
    for loop in range(0, l-l//2, 1):
        s += random.choice(letters)
    for loop in range(0, l//2, 1):
        s += random.choice(numbers)
    return s

def high(l):
    s = ''
    for loop in range(0, round(l*0.4), 1):
        s += random.choice(letters)
    for loop in range(0, round(l*0.3), 1):
        s += random.choice(numbers)
    for loop in range(0, l-round(l*0.3)-round(l*0.4), 1):
        s += random.choice(specialChars)
    return s

def generate():
    length = int(chooseLabel.entry.get())
    if radioVar.get() == 'low':
        passVar.set(low(length))
    elif radioVar.get() == 'medium':
        passVar.set(medium(length))
    elif radioVar.get() == 'high':
        passVar.set(high(length))

class LabelWithEntry:
    def __init__(self, text, row):
        self.label = Label(root, text = text)
        self.entry = Spinbox(root, from_=4,to=36)
        self.label.grid(row=row, column=0)
        self.entry.grid(row=row, column=1, columnspan=3)

passVar = StringVar()

genLabel = Label(text="Generated password:", fg="blue").grid(row=0, column=0, columnspan=2)
passLabel = Label(textvariable=passVar, ).grid(row=0, column=2, columnspan=2)
chooseLabel = LabelWithEntry("Length", 3)
strengthLabel = Label(text="Password Strength").grid(row=2, column=0)

radioVar = StringVar()

radioLvl1 = Radiobutton(root, text="Low", variable = radioVar, value='low').grid(row=2,column=1)
radioLvl2 = Radiobutton(root, text="Medium", variable = radioVar, value='medium').grid(row=2,column=2)
radioLvl3 = Radiobutton(root, text="High", variable = radioVar, value='high').grid(row=2,column=3)

submitBtn = Button(text="Submit", bg="lightgreen", command=generate).grid(row=8, column=1)

root.mainloop()
