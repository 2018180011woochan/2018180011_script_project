from tkinter import *
from tkinter import font
import urllib
import http.client

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
        self.canvas.place(x=300, y=110)

    def TemperatureInfo(self):
        myFont = font.Font(g_daywindow, size=15, weight='bold')
        UpTemperatureInfo = Label(g_daywindow, font = myFont, text="최고 기온")
        DownTemperatureInfo = Label(g_daywindow, font=myFont, text="최저 기온")
        UpTemperatureInfo.pack()
        DownTemperatureInfo.pack()
        UpTemperatureInfo.place(x=31,y=210)
        DownTemperatureInfo.place(x=31,y=260)

    def TemperatureGraph(self):
        self.canvas = Canvas(g_daywindow, bg='white', width='250', height='200')
        self.canvas.pack()
        self.canvas.place(x=31, y=300)

    def DustInfo(self):
        myFont = font.Font(g_daywindow, size=15, weight='bold')
        DustText = Label(g_daywindow, font=myFont, text="미세먼지 정보")
        DustText.pack()
        DustText.place(x=310,y=320)

        self.canvas = Canvas(g_daywindow, bg='white', width='150', height='150')
        self.canvas.pack()
        self.canvas.place(x=300, y=350)

    def __init__(self):
        self.InitSearchEntry()
        self.InitSearchButton()
        self.RenderCity()
        self.WeatherInfoText()
        self.WeatherInfoPicture()
        self.TemperatureInfo()
        self.TemperatureGraph()
        self.DustInfo()

        g_daywindow.mainloop()
MainGUI()
