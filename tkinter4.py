from tkinter import *
root = Tk()
root.title("social media")

value = 'Press a button'

def facebook():
    value.set("Facebook: JohnSmithFacebook")
    root.update()

def instagram():
    value.set("Instagram: JohnSmithInsta")
    root.update()

def snapchat():
    value.set("Snapchat: JohnSmithSnap")
    root.update()

def twitter():
    value.set("Twitter: JohnSmithTwitter")
    root.update()

value = StringVar()

value.set("Press a Button")

Button(root, bg="blue", text="Facebook", command=facebook).grid(row=0, column=0)
Button(root, bg="yellow", text="Snapchat", command=snapchat).grid(row=0, column=1)
Button(root, bg="red", text="Instagram", command=instagram).grid(row=1, column=0)
Button(root, bg="gray", text="Twitter", command=twitter).grid(row=1, column=1)
Label(root, textvariable=value).grid(row=2, column=0, columnspan=10)

root.mainloop()
