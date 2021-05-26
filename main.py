from tkinter import *
from tkinter import font
import urllib
import http.client
from xml.dom.minidom import parse, parseString
from xml.etree import ElementTree

g_daywindow = Tk()
g_daywindow.title("Weather_Reminder")
g_daywindow.geometry("500x600")
DataList = []

class MainGUI:
    def InitSearchEntry(self):
        global SearchListBox
        ListBoxScrollBar = Scrollbar(g_daywindow)
        ListBoxScrollBar.pack()
        ListBoxScrollBar.place(x=130,y=70)

        myFont =font.Font(g_daywindow, size=10, weight='bold')
        SearchListBox = Listbox(g_daywindow, font=myFont, activestyle='none',
                                width=10, height=1, borderwidth=12, relief='ridge',
                                yscrollcommand=ListBoxScrollBar.set)
        SearchListBox.insert(1, "시흥시")
        SearchListBox.insert(2, "안산시")
        SearchListBox.insert(3, "서울시")
        SearchListBox.pack()
        SearchListBox.place(x=30, y=70)

    def InitSearchButton(self):
        myFont =font.Font(g_daywindow, size=10, weight='bold')
        SearchButton = Button(g_daywindow, font=myFont, text="검색",
                              command=self.SearchButtonAction)
        SearchButton.pack()
        SearchButton.place(x=210, y=80)

    def SearchButtonAction(self):
        myListBox = SearchListBox.curselection()[0]
        if myListBox == 0:
            self.SearchSiheung()
            self.TemperatureGraph()
            self.TemperatureResult()
        elif myListBox == 1:
            a = 2
        elif myListBox == 2:
            a = 3

    def SearchSiheung(self):
        conn = http.client.HTTPConnection("apis.data.go.kr")
        conn.request("GET", "/1360000/LivingWthrIdxService01/getSenTaIdx?serviceKey=JeJzrQJprx9UjQkk7hibZqu2lXn9btXlpDpGp3KZL%2F8yEytBMzILptb4RUnKav%2FNndTc3oz6JVuKNfHsxehLuQ%3D%3D&pageNo=1&numOfRows=10&dataType=XML&areaNo=4139058900&time=2021052506&requestCode=A41")
        req = conn.getresponse()

        global DataList
        DataList.clear()

        if req.status == 200:
            TempDoc =req.read().decode('utf-8')
            if TempDoc == None:
                print("에러")
            else:
                parseData = parseString(TempDoc)
                response = parseData.childNodes
                body = response[0].childNodes
                items = body[1].childNodes
                item = items[1].childNodes

                for temp in item:
                    subitem = temp.childNodes
                    #print(subitem[0].firstChild.nodeValue)
                    DataList.append(int(subitem[3].firstChild.nodeValue))
                    DataList.append(int(subitem[4].firstChild.nodeValue))
                    DataList.append(int(subitem[5].firstChild.nodeValue))
                    DataList.append(int(subitem[6].firstChild.nodeValue))
                    DataList.append(int(subitem[7].firstChild.nodeValue))
                    DataList.append(int(subitem[8].firstChild.nodeValue))
                    DataList.append(int(subitem[9].firstChild.nodeValue))
                    DataList.append(int(subitem[10].firstChild.nodeValue))

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

    def TemperatureResult(self):
        myFont = font.Font(g_daywindow, size=15, weight='bold')
        DataList.sort()
        UpTemparature = Label(g_daywindow, font=myFont, text=str(DataList[7]))
        DownTemparature = Label(g_daywindow, font=myFont, text=str(DataList[0]))
        UpTemparature.pack()
        DownTemparature.pack()
        UpTemparature.place(x=151, y=210)
        DownTemparature.place(x=151, y=260)

    def TemperatureGraph(self):
        myFont = font.Font(g_daywindow, size=10, weight='bold')
        self.canvas = Canvas(g_daywindow, bg='white', width='250', height='200')
        self.canvas.pack()
        self.canvas.place(x=31, y=300)

        y_stretch = 15
        y_gap = 20
        x_stretch = 10
        x_width = 20
        x_gap = 20
        for x, y in enumerate(DataList):
            x0 = x * x_stretch + x * x_width + x_gap
            y0 = 350 - (y * y_stretch + y_gap)
            x1 = x * x_stretch + x * x_width + x_width + x_gap
            y1 = 350 - y_gap
            # Here we draw the bar
            self.canvas.create_rectangle(x0, y0, x1, y1, fill="red")
            self.canvas.create_text(x0+10, y0-10, text=str(y))
        timeText = Label(g_daywindow, font=myFont, text="06시 09시 12시 15시 18시 21시 24시 3시")
        timeText.pack()
        timeText.place(x=40, y=500)

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
