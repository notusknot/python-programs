from tkinter import *
root=Tk()
root.title("hello world")

def clear():
    fahrenheitInput.entry.delete(0, END)
    celciusInput.entry.delete(0, END)

def calculate():
    if len(fahrenheitInput.entry.get()) > 0:
        f=float(fahrenheitInput.entry.get())
        c = (f-32)*5/9
        celciusInput.entry.insert(0, str(c))
    else:
        c=float(celciusInput.entry.get())
        f = c * 9/5 + 32
        fahrenheitInput.entry.insert(0, str(f))


class LabelWithEntry:
    def __init__(self, text, row):
        self.label = Label(root, text = text)
        self.entry = Entry(root)
        self.label.grid(row=row, column=0)
        self.entry.grid(row=row, column=1)


Label(root, text="Please enter the following").grid(row=0, column=0, columnspan=2)

fahrenheitInput = LabelWithEntry("Fahrenheit", 1)
celciusInput = LabelWithEntry("Celcius", 2)

calculateButton = Button(root, text="calculate", fg="blue", command=calculate)
calculateButton.grid(row=6, column=0)

clearButton = Button(root, text="Clear", fg="red", command=clear)
clearButton.grid(row=6, column=1)

root.mainloop()
