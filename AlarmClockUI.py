# modules required: time, tkinter, os, csv,

# TO DO
# adding a clock at the center of the Window
# adding a functionality to see current alarms
#   adding, deleting, editing
# adding a set a new alarm functionality
#   settime, settone, setRingtime, set isSnoozable,
# functionality to edit an alarm
# functionality to remove an alarm
# maybe add different ringtone options

# adding a stopwatch
#   lap, start ,stop

# import datetime as dt
import time
import tkinter as tk
# from tkinter import *
import os

mainWindow_geometry = '500x500'

mainWindow = tk.Tk()
mainWindow.geometry(mainWindow_geometry)
mainWindow.title("Clock")

runClock = True
fps = 1/5

try:
    while (runClock):
        date_time = time.gmtime(time.time() + 19800)

        def timeAsString():
            hour = str(date_time.tm_hour % 12).zfill(2)
            if (hour == "00"):
                hour = "12"
            min = str(date_time.tm_min).zfill(2)
            sec = str(date_time.tm_sec).zfill(2)
            return (hour+":"+min+":"+sec)

        mainTimer_font = 'Terminal'
        mainTimer_fontsize = 30

        mainTimer = tk.Message(master=mainWindow, font=(
            mainTimer_font, mainTimer_fontsize), text=timeAsString(), width=210, justify='center')
        mainTimer.place(x=100, y=80)


        menu = tk.Menu(master=mainWindow)
        mainWindow.config(menu=menu)
        filemenu = tk.Menu(menu)
        filemenu.add_cascade(label='File', menu=filemenu)
        filemenu.add_command(label='New Alarm')
        filemenu.add_command(label='Open Alarms')
        filemenu.add_separator()

        time.sleep(fps)
        mainWindow.update()
except:
    print("Bye Bye!!")

# print(date_time,current_date, current_time)
