from tkinter import *
import webcolors
root = Tk()
root.title("Scale")

redVar = IntVar()
redScale = Scale(root, label='red', variable=redVar,from_=0,to=255,orient=VERTICAL)
redScale.grid(row=0,column=0)

greenVar = IntVar()
greenScale = Scale(root, label='green', variable=greenVar,from_=0,to=255,orient=VERTICAL)
greenScale.grid(row=0,column=2)

blueVar = IntVar()
blueScale = Scale(root, label='blue', variable=blueVar,from_=0,to=255,orient=VERTICAL)
blueScale.grid(row=0,column=4)

while True:
    hexVal = webcolors.rgb_to_hex((redVar.get(), greenVar.get(), blueVar.get()))
    clrLabel = Label(text="", bg=hexVal, width=50).grid(row=10, column=0, columnspan=10)
    root.update()
    
root.mainloop()
