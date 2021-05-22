from tkinter import *
from tkinter import font

def InitSearchEntry(self):
    myFont =font.Font(self.daywindow, size=15, weight='bold')
    InputLabel =Entry(self.daywindow, font=myFont, width=15)
    InputLabel.pack()
    InputLabel.place(x=30, y=80)

def InitSearchButton(self):
    myFont =font.Font(self.daywindow, size=10, weight='bold')
    SearchButton = Button(self.daywindow, font=myFont, text="검색",
                          command=self.SearchButtonAction)
    SearchButton.pack()
    SearchButton.place(x=210,y=80)

def SearchButtonAction(self):
    pass