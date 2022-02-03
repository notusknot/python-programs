import tkinter
import time
from tkinter import *
from tkinter import messagebox
root = Tk()

class Question:
    def __init__(self, question, correct, options):
        self.question = question
        self.correct = correct
        self.options = options
        self.marked = None

q1 = Question("What is the capital of the USA?", "Washington DC", "California, Washington DC, San Francisco, Nevada".split(", "))
q2 = Question("Who invented Python?", "Guido van Rossum", "Dennis Ritchie, James Gosling, Guido van Rossum".split(", "))
q3 = Question("What language is this program written in?", "Python", "Javascript, C++, Python, Java".split(", "))

questions = [q1, q2, q3]

del q1, q2, q3

def startTime():
    global s
    s = time.time()

def stopTime():
    global stop, quizTime
    stop = time.time()
    sec = stop - s
    mins = sec // 60
    sec = round(sec%60, 3)
    quizTime = "{}:{}".format(int(mins), sec)

def start():
    global score, currentQuestion
    score = 0
    currentQuestion = 0
    welcomeFrame.destroy()
    quizFrame.grid()
    questionFrame.grid(row=1, columnspan=3)
    prevBtn["state"] = DISABLED
    displayQuestion()
    startTime()

def previous():
    global currentQuestion
    if currentQuestion == 0:
        prevBtn["state"] = DISABLED
    else:
        currentQuestion -= 1
        displayQuestion()

def submit():
    stopTime()
    global score
    prevBtn["state"] = NORMAL
    nextBtn["state"] = NORMAL
    if questions[currentQuestion].marked == None:
        questions[currentQuestion].marked = radioVar.get()

        if str(radioVar.get()) == questions[currentQuestion].correct:
            score += 1
            Score2.set("Score: {}".format(score))
    TimeVar.set("Time: {}".format(quizTime))

def displayQuestion():
    global questionFrame
    questionFrame.destroy()
    questionFrame = Frame(quizFrame)
    questionFrame.grid(row=1, columnspan=3)
    question = questions[currentQuestion]
    questionVar.set(question.question)
    Label(questionFrame, textvariable=questionVar).grid(row=0)
    root.update()
    counter = 1
    for loop in question.options:
        optionRadio = Radiobutton(questionFrame, text=loop, variable=radioVar, value=loop).grid(row=counter)
        counter +=1
    

def next():
    global currentQuestion
    if currentQuestion == len(questions)-1:
        messagebox.showinfo("Quiz result", "You got {}/{} points".format(score,len(questions)))
        nextBtn["text"] = "Exit"
        nextBtn["command"] = exit
    else:
        currentQuestion += 1
        displayQuestion()

welcomeFrame = Frame(root)
welcomeFrame.grid()
quizFrame = Frame(root)
endFrame = Frame(root)
questionFrame = Frame(quizFrame)

quizTime = s = stop = 0
score = 0
currentQuestion = 0

# Displays score on screen 
Score2 = StringVar()
Score2.set("Score: {}".format(score))
scoreLabel = Label(quizFrame, textvariable=Score2).grid(row=0, column=0, columnspan=2)

TimeVar = StringVar()
TimeVar.set("Time: {}".format(quizTime))
timeLabel = Label(quizFrame, textvariable=TimeVar).grid(row=0, column=2, columnspan=2)

questionVar = StringVar()
questionLabel = Label(questionFrame, textvariable=questionVar).grid(row=0)

prevBtn = Button(quizFrame, text="Previous", command=previous)
prevBtn.grid(row=2, column=1, columnspan=1)
submitBtn = Button(quizFrame, text="Submit", command=submit).grid(row=2, column=2, columnspan=1)
nextBtn = Button(quizFrame, text="Next", command=next)
nextBtn.grid(row=2, column=3, columnspan=1)

generalKnowledgeLabel = Label(welcomeFrame, text="General Knowledge Quiz", fg="blue", font=("Arial", 20, "bold")).grid(columnspan=3)

startButton = Button(welcomeFrame, text="Start", command=start).grid(row=3, column=0)
exitButton = Button(welcomeFrame, text="Exit", command=exit).grid(row=3, column=2)

radioVar = StringVar()

root.mainloop()
