#Sohel Tamboli

import tkinter as tool
from tkinter import *

win= tool.Tk()
def colorchange():
    win.configure(bg="red")
    
l1 = Label(win, text = 'JSPM University')
b1 = Button(win, text = "Click ME", command = colorchange)
l1.pack()
b1.pack()
win.mainloop()
