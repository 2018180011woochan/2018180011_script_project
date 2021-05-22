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

    def RenderCity(self):
        global RenderCity

        CityFont = font.Font(g_daywindow, size=10)
        RenderCity = Text(g_daywindow, width=31, height=5)
        RenderCity.pack()
        RenderCity.place(x=31,y=120)

    def __init__(self):
        self.InitSearchEntry()
        self.InitSearchButton()
        self.RenderCity()

        g_daywindow.mainloop()
MainGUI()
