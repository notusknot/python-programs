from tkinter import *
root = Tk()
root.title("Buttons")

def writeToFile():
    name = nameInput.entry.get()
    age = ageInput.entry.get()
    level = radioVar.get()
    f = open("studentLevel.txt", "w")
    f.write(str([name, age, level]))
    f.close()


class LabelWithEntry:
    def __init__(self, text, row):
        self.label = Label(root, text = text)
        self.entry = Entry(root)
        self.label.grid(row=row, column=0)
        self.entry.grid(row=row, column=1)

nameInput = LabelWithEntry("Name",0)
ageInput = LabelWithEntry("Age",1)

chooseLabel = Label(text="Choose your level").grid(row=2, column=1)

radioVar = StringVar()

radioLvl1 = Radiobutton(root, text="Level 1", variable = radioVar, value=0).grid(row=3)
radioLvl2 = Radiobutton(root, text="Level 2", variable = radioVar, value=1).grid(row=4)
radioLvl3 = Radiobutton(root, text="Level 3", variable = radioVar, value=2).grid(row=5)
radioLvl4 = Radiobutton(root, text="Level 4", variable = radioVar, value=3).grid(row=6)
radioLvl5 = Radiobutton(root, text="Level 5", variable = radioVar, value=4).grid(row=7)

submitBtn = Button(text="Submit", bg="lightblue", command=writeToFile).grid(row=8, column=1)

root.mainloop()
