from tkinter import *
import time
root=Tk()
root.title("Stopwatch")

def start():
    global startTime
    startTime = time.time()

def stop():
    seconds = round(time.time() - startTime, 3)
    hours = int(seconds//3600)
    minutes = int((seconds%3600)//60)
    seconds = seconds%60
    num.set('{}:{}:{}'.format(hours, minutes, seconds))

def reset():
    num.set("0")

num = StringVar()
num.set("0")

Label(root, textvariable=num).grid(row=0, column=0, columnspan=3)

startButton = Button(root, text="Start", fg="green", command=start).grid(row=1, column=0)
stopButton = Button(root, text="Stop", fg="red", command=stop).grid(row=1, column=1)
resetButton = Button(root, text="Reset", fg="blue", command=reset).grid(row=1, column=2)

root.mainloop()
