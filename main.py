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

    def WeatherInfoText(self):
        myFont = font.Font(g_daywindow, size=15, weight='bold')
        WeatherInfoText = Label(g_daywindow, font = myFont, text="날씨 정보")
        WeatherInfoText.pack()
        WeatherInfoText.place(x=325,y=80)

    def WeatherInfoPicture(self):
        self.canvas = Canvas(g_daywindow, bg='white', width='150', height='150')
        self.canvas.pack()
        self.canvas.place(x=300, y=130)

    def TempatureInfo(self):
        myFont = font.Font(g_daywindow, size=15, weight='bold')
        UpTempatureInfo = Label(g_daywindow, font = myFont, text="최고 기온")
        DownTempatureInfo = Label(g_daywindow, font=myFont, text="최저 기온")
        UpTempatureInfo.pack()
        DownTempatureInfo.pack()
        UpTempatureInfo.place(x=31,y=210)
        DownTempatureInfo.place(x=31,y=260)

    def __init__(self):
        self.InitSearchEntry()
        self.InitSearchButton()
        self.RenderCity()
        self.WeatherInfoText()
        self.WeatherInfoPicture()
        self.TempatureInfo()

        g_daywindow.mainloop()
MainGUI()
