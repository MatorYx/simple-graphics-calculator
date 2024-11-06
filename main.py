from tkinter import *

def summ():
    lbl.configure(text = str(float(firstSummary.get()) + float(secondSummary.get())))
def subtract():
    lbl.configure(text = str(float(firstSummary.get()) - float(secondSummary.get())))
def multiply():
    lbl.configure(text = str(float(firstSummary.get()) * float(secondSummary.get())))
def division():
    lbl.configure(text = str(float(firstSummary.get()) / float(secondSummary.get())))
def power():
    lbl.configure(text = str(float(firstSummary.get()) ** float(secondSummary.get())))

window = Tk()
window.geometry('400x250')
window.title("Calc")

lbl = Label(window, text = "0", font=("Times New Roman", 24))
lbl.grid(column = 0, row = 3)

plus = Button(window, text="+", command = summ)
plus.grid(column = 1, row = 1)

mines = Button(window, text="-", command = subtract)
mines.grid(column = 2, row = 1)

mult = Button(window, text="*", command = multiply)
mult.grid(column = 3, row = 1)

div = Button(window, text="/", command = division)
div.grid(column = 4, row = 1)

po = Button(window, text="^", command = power)
po.grid(column = 5, row = 1)

firstSummary = Entry(window)
firstSummary.grid(column = 0, row = 0)

secondSummary = Entry(window)
secondSummary.grid(column = 0, row = 2)

window.mainloop()
