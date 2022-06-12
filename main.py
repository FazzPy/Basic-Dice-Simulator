from tkinter import *
import random

root = Tk()
root.geometry("500x500")
root.title("Dice Simulator")
root.config(bg="#12DEED")
root.resizable(width=False, height=False)
color = "#12DEED"

def ROLL():
    v = random.randint(1,6)
    LABEL2["text"] = "Sonuç : {0}".format(v)

LABEL1 = Label(text="Fazz | Dice Simulator v0.1", bg=color, fg="black", font="Arial 16")
LABEL1.place(x=10, y=10)

LABEL2 = Label(text="Sonuç : ", bg=color, fg="black", font="Arial 16")
LABEL2.place(x=10, y=50)

BUTTON1 = Button(bg="green", fg="white", font="Arial 16", text="Roll", command=ROLL)
BUTTON1.place(x=10, y=100)


root.mainloop()
