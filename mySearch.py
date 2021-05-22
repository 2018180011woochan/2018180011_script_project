from tkinter import *
from tkinter import font

class mySearch:
    global g_daywindow
    def InitSearchEntry(self, g_daywindow):
        myFont =font.Font(g_daywindow, size=15, weight='bold')
        InputLabel =Entry(g_daywindow, font=myFont, width=15)
        InputLabel.pack()
        InputLabel.place(x=30, y=80)

    def InitSearchButton(self, g_daywindow):
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