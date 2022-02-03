from tkinter import *
import pytz
from datetime import datetime
root = Tk()
root.title("Frames")

timezone = pytz.timezone('US/Pacific')
usa = datetime.now(timezone)

timezone = pytz.timezone('America/Toronto')
canada = datetime.now(timezone)

timezone = pytz.timezone('Europe/Paris')
france = datetime.now(timezone)

timezone = pytz.timezone('Asia/Calcutta')
india = datetime.now(timezone)

USFinalTime = usa.strftime('%Y-%m-%d %I:%M:%S %p %Z')
CanadaFinalTime = canada.strftime('%Y-%m-%d %I:%M:%S %p %Z')
FranceFinalTime = france.strftime('%Y-%m-%d %I:%M:%S %p %Z')
IndiaFinalTime = india.strftime('%Y-%m-%d %I:%M:%S %p %Z')

image1 = PhotoImage(file = "usa.png")
image2 = PhotoImage(file = "india.png")
image3 = PhotoImage(file = "france.png")
image4 = PhotoImage(file = "canada.png")

usaFlag = Label(image=image1).grid(row=0, column=0)
indiaFlag = Label(image=image2).grid(row=0, column=1)
franceFlag = Label(image=image3).grid(row=2, column=1)
canadaFlag = Label(image=image4).grid(row=2, column=0)

label = Label(root, text=USFinalTime).grid(row=1, column=0)
label = Label(root, text=CanadaFinalTime).grid(row=3, column=1)
label = Label(root, text=FranceFinalTime).grid(row=3, column=0)
label = Label(root, text=IndiaFinalTime).grid(row=1, column=1)

root.mainloop()
