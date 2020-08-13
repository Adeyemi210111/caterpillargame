import json
import tkinter
from tkinter import *

data = json.load(open("data.json"))
def translate():
    item = w.get()
    if item in data:
        name = data[item]
        for i in name:
            c = Label.configure(word, text=i)
            return c
    elif item.title() in data:
        name = data[item.title()]
        c = Label.configure(word, text=name)
        return c
    elif item.upper() in data:
        name = data[item.upper()]
        c = Label.configure(word, text=name)
        return c
    else:
        name = "Oops, the word does not exist"
        c = Label.configure(word, text=name)
        return c


win = Tk()
win.geometry("800x300")
win.resizable(height=FALSE, width=FALSE)
win.title("Dictionary")

frame = Frame(win)
frame.pack()

frame2 = Frame(win)
frame2.pack(side=BOTTOM)

first = Label(frame, text='Enter the word you want to search for', font="arial", pady=20)
first.pack()
w = Entry(frame, bd=5)
w.pack()

word = Label(frame, text='', height=5, bd=5, font="arial")
word.pack()

btn = Button(frame2, text='Search', command=translate, relief='raised', padx=10, pady=5)
btn.pack()
btn2 = Button(frame2, text='Exit', command=quit, relief='raised', padx=10, pady=5)
btn2.pack()

win.mainloop()