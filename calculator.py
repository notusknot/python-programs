import tkinter
from tkinter import *

root = Tk()
root.title("Calculator")

value = ""
equation = StringVar()
expressionBox = Entry(root, textvariable=equation).grid(columnspan=4)

def numPress(num):
    global value
    value = value + str(num)
    equation.set(value)

def equalPress():
    global value
    total = str(eval(value))
    equation.set(total)

def clear():
    global value
    value = ""
    equation.set("")

button1 = Button(root, text=' 1 ', fg='black', command=lambda: numPress(1), height=1, width=3).grid(row=2, column=0)
button2 = Button(root, text=' 2 ', fg='black', command=lambda: numPress(2), height=1, width=3).grid(row=2, column=1)
button3 = Button(root, text=' 3 ', fg='black', command=lambda: numPress(3), height=1, width=3).grid(row=2, column=2)
button4 = Button(root, text=' 4 ', fg='black', command=lambda: numPress(4), height=1, width=3).grid(row=3, column=0)
button5 = Button(root, text=' 5 ', fg='black', command=lambda: numPress(5), height=1, width=3).grid(row=3, column=1)
button6 = Button(root, text=' 6 ', fg='black', command=lambda: numPress(6), height=1, width=3).grid(row=3, column=2)
button7 = Button(root, text=' 7 ', fg='black', command=lambda: numPress(7), height=1, width=3).grid(row=4, column=0)
button8 = Button(root, text=' 8 ', fg='black', command=lambda: numPress(8), height=1, width=3).grid(row=4, column=1)
button9 = Button(root, text=' 9 ', fg='black', command=lambda: numPress(9), height=1, width=3).grid(row=4, column=2)
button0 = Button(root, text=' 0 ', fg='black', command=lambda: numPress(0), height=1, width=3).grid(row=5, column=1)

plus = Button(root, text=' + ', fg='black', command=lambda: numPress("+"), height=1, width=3).grid(row=2, column=3)
minus = Button(root, text=' - ', fg='black', command=lambda: numPress("-"), height=1, width=3).grid(row=3, column=3)
multiply = Button(root, text=' * ', fg='black', command=lambda: numPress("*"), height=1, width=3).grid(row=4, column=3)
divide = Button(root, text=' / ', fg='black', command=lambda: numPress("/"), height=1, width=3).grid(row=5, column=3)

equal = Button(root, text=' = ', fg='black', command=equalPress, height=1, width=3).grid(row=5, column=2)
clear = Button(root, text='C', fg='black', command=clear, height=1, width=3).grid(row=0, column=3, columnspan=1)
decimal= Button(root, text='.', fg='black', command=lambda: numPress('.'), height=1, width=3).grid(row=5, column=0)

root.mainloop()

