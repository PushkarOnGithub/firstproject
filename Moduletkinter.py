import tkinter as tk
from tkinter import Button
from tkinter import Message
from tkinter import Canvas
from tkinter import Checkbutton
from tkinter import Entry
import subprocess
import time
import sys

window = tk.Tk()
window.title("First GUI")

window.geometry("500x500")
# stop = tk.Button(master=window, activebackground='red',
            # activeforeground='green',bg='blue',command=quit, text="Stop", bd=2, image=None, width=20, height=1)  # Button method can be used to make a button

# active : when the cursor is on the button
# bg : color of the button in normal condition
# command : the process which will be processed when the button is pressed
# text : what should the button display
# bd : maybe the border diameter
# image : the image to display on the button


# def start_New_Window():
    # subprocess.run(['.\Moduletkinter.py'], shell=True)

# def printhi():
    # print("Hi!")
# begin = tk.Button(master=window, activebackground='red',activeforeground='green',bg='blue',command=start_New_Window, text="Click To Start A New Window", bd=2)
# Hi = tk.Button(master=window, activebackground='red',activeforeground='green',bg='blue',command=printhi, text="Click To print Hi!", bd=2)


#stop.pack()   # pack arranges all the windows in blocks format
# printHi.pack()

# stop.grid()   # grid arranges all the widgets in the grid form
# printHi.grid()

# stop.place(x=100, y=100) # place takes the exact position of the button to place it
# Hi.place(x=100, y=150)

# img = Canvas(master=window)  # creates images with dots provided

# chekbutton = Checkbutton(master=window, text="check", command=None)
# chekbutton.place(x=10, y=10)

# entry_ = Entry(master=window, textvariable="Enter Your Name", cursor="heart",)
# entry_.place(x=10, y=125)

def current_time():
    hour = str(time.gmtime(time.time()+19800).tm_hour%12).zfill(2)
    if hour == "00":
        hour = "12"
    min = str(time.gmtime(time.time()+19800).tm_min).zfill(2)
    sec = str(time.gmtime(time.time()+19800).tm_sec).zfill(2)
    return str(hour + ":" + min + ":" + sec)


# window.after(0, time.place(x=200, y=200))

while(True):
    timeshow = Message(master=window, text=current_time(), width=50)
    timeshow.place(x=200, y=200)
    time.sleep(0.1)
    window.update()

# window.mainloop()


# from tkinter import *

# root = Tk()
# root.geometry("500x500")
# root.title("My App")
# root.config(bg="#ff0000")

# def printhi(*args):
# 	print("Hi!")
    
# btn = Button(root, text="Click to print hi", command=printhi)
# btn.place(x=200, y=200)

# root.mainloop()