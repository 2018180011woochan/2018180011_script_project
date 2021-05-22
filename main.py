from tkinter import *
from tkinter import font

g_daywindow = Tk()
g_daywindow.title("Weather_Reminder")
g_daywindow.geometry("500x600")

class MainGUI:
    def InitSearchEntry(self):
        myFont =font.Font(g_daywindow, size=15, weight='bold')
        InputLabel =Entry(g_daywindow, font=myFont, width=15)
        InputLabel.pack()
        InputLabel.place(x=30, y=80)

    def InitSearchButton(self):
        myFont =font.Font(g_daywindow, size=10, weight='bold')
        SearchButton = Button(g_daywindow, font=myFont, text="검색",
                              command=self.SearchButtonAction)
        SearchButton.pack()
        SearchButton.place(x=210,y=80)

    def SearchButtonAction(self):
        pass

    def __init__(self):
        self.InitSearchEntry()
        self.InitSearchButton()

        g_daywindow.mainloop()
MainGUI()
