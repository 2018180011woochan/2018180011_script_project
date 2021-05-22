from tkinter import *
from tkinter import font
from Search import *

g_daywindow = Tk()
g_daywindow.title("Weather_Reminder")
g_daywindow.geometry("500x600")

class MainGUI:
    def __init__(self):
        InitSearchEntry()
        InitSearchButton()

    g_daywindow.mainloop()

MainGUI()