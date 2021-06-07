from tkinter import *
from tkinter import font
from tkinter import messagebox
import tkinter
import urllib
import http.client
from xml.dom.minidom import parse, parseString
from xml.etree import ElementTree
import datetime
#import folium
# pip install cefpython3==66.0
import sys
#from cefpython3 import cefpython as cef
import threading
#import gmail
#import internetbook
import mimetypes
import mysmtplib
from email.mime.base import MIMEBase
from email.mime.text import MIMEText


g_daywindow = Tk()
g_daywindow.title("Weather_Reminder")
g_daywindow.geometry("500x600")
DataList = []
DustState = []
Dust10 = []
Dust25 = []
myimagelabel = []
now = datetime.datetime.now()



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
        SearchButton.place(x=170, y=80)

    def SearchButtonAction(self):
        myListBox = SearchListBox.curselection()[0]
        if myListBox == 0:
            self.SearchSiheung()
            self.TemperatureGraph()
            self.TemperatureResult()
            self.SearchDust10()
            self.SearchDustInfo()
            self.DrawDustInfo()
        elif myListBox == 1:
            a = 2
        elif myListBox == 2:
            a = 3

    def SearchSiheung(self):
        conn = http.client.HTTPConnection("apis.data.go.kr")
        nowDate = now.strftime('%Y%m%d')
        conn.request("GET", "/1360000/LivingWthrIdxService01/getSenTaIdx?serviceKey=JeJzrQJprx9UjQkk7hibZqu2lXn9btXlpDpGp3KZL%2F8yEytBMzILptb4RUnKav%2FNndTc3oz6JVuKNfHsxehLuQ%3D%3D&pageNo=1&numOfRows=10&dataType=XML&areaNo=4139058900&time="+nowDate+"06&requestCode=A41")
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
                    if subitem.length != 0:
                        DataList.append(int(subitem[3].firstChild.nodeValue))
                        DataList.append(int(subitem[4].firstChild.nodeValue))
                        DataList.append(int(subitem[5].firstChild.nodeValue))
                        DataList.append(int(subitem[6].firstChild.nodeValue))
                        DataList.append(int(subitem[7].firstChild.nodeValue))
                        DataList.append(int(subitem[8].firstChild.nodeValue))
                        DataList.append(int(subitem[9].firstChild.nodeValue))
                        DataList.append(int(subitem[10].firstChild.nodeValue))

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
        myFont = font.Font(g_daywindow, size=20, weight='bold')
        DataInfo = now.strftime('%Y-%m-%d')
        day = Label(g_daywindow, font=myFont, text=DataInfo)
        UpTemperatureInfo = Label(g_daywindow, font = myFont, text="최고 기온")
        DownTemperatureInfo = Label(g_daywindow, font=myFont, text="최저 기온")

        day.pack()
        UpTemperatureInfo.pack()
        DownTemperatureInfo.pack()

        day.place(x=70, y=135)
        UpTemperatureInfo.place(x=31,y=190)
        DownTemperatureInfo.place(x=31,y=240)

    def TemperatureResult(self):
        myFont = font.Font(g_daywindow, size=15, weight='bold')
        DataList.sort()
        self.UpTemparature = Label(g_daywindow, font=myFont, text=str(DataList[7]))
        self.DownTemparature = Label(g_daywindow, font=myFont, text=str(DataList[0]))
        self.UpTemparature.pack()
        self.DownTemparature.pack()
        self.UpTemparature.place(x=200, y=195)
        self.DownTemparature.place(x=200, y=245)

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
            y0 = 400 - (y * y_stretch + y_gap)
            x1 = x * x_stretch + x * x_width + x_width + x_gap
            y1 = 400 - y_gap
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
        DustText.place(x=310,y=280)

        #self.canvas = Canvas(g_daywindow, bg='white', width='150', height='150')
        #self.canvas.pack()
        #self.canvas.place(x=300, y=350)

    def SearchDust10(self):
        conn = http.client.HTTPConnection("apis.data.go.kr")
        DataInfo = now.strftime('%Y-%m-%d')
        conn.request("GET", "/B552584/ArpltnInforInqireSvc/getMinuDustFrcstDspth?serviceKey=JeJzrQJprx9UjQkk7hibZqu2lXn9btXlpDpGp3KZL%2F8yEytBMzILptb4RUnKav%2FNndTc3oz6JVuKNfHsxehLuQ%3D%3D&returnType=xml&numOfRows=100&pageNo=1&searchDate="+DataInfo+"&InformCode=PM10")
        req = conn.getresponse()

        global DustState
        DustState.clear()
        print(req.status)
        if req.status == 200:
            TempDoc =req.read().decode('utf-8')
            if TempDoc == None:
                print("에러")
            else:
                parseData = parseString(TempDoc)
                response = parseData.childNodes
                body = response[0].childNodes
                items = body[3].childNodes
                item = items[1].childNodes

                for temp in item:
                    if temp.nodeName == "item":
                        realnode = temp.childNodes
                        DustState.append(str(realnode[13].firstChild.nodeValue))

    def SearchDustInfo(self):
        conn = http.client.HTTPConnection("apis.data.go.kr")
        hangul_utf8 = urllib.parse.quote("경기")
        conn.request("GET", "/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?serviceKey=JeJzrQJprx9UjQkk7hibZqu2lXn9btXlpDpGp3KZL%2F8yEytBMzILptb4RUnKav%2FNndTc3oz6JVuKNfHsxehLuQ%3D%3D&returnType=xml&numOfRows=100&pageNo=1&sidoName="+hangul_utf8+"&ver=1.0")
        req = conn.getresponse()

        global DustState
        DustState.clear()
        print(req.status)
        if req.status == 200:
            TempDoc =req.read().decode('utf-8')
            if TempDoc == None:
                print("에러")
            else:
                parseData = parseString(TempDoc)
                response = parseData.childNodes
                body = response[0].childNodes
                items = body[3].childNodes
                item = items[1].childNodes

                for temp in item:
                    if temp.nodeName == "item":
                        realnode = temp.childNodes
                        if realnode[41].firstChild.nodeValue == "고잔동":
                            print(int(realnode[17].firstChild.nodeValue))
                            print(int(realnode[21].firstChild.nodeValue))
                            Dust10.append(int(realnode[17].firstChild.nodeValue))
                            Dust25.append(int(realnode[21].firstChild.nodeValue))

    def DrawDustInfo(self):
        myFont = font.Font(g_daywindow, size=10, weight='bold')
        #DustText = Label(g_daywindow, font=myFont, text=DustState[0])
        #DustText.pack()
        #DustText.place(x=280,y=500)

        DustText = Label(g_daywindow, font=myFont, text="미세먼지:  "+str(Dust10[0]))
        DustText.pack()
        DustText.place(x=300,y=500)
        DustText2 = Label(g_daywindow, font=myFont, text="초미세먼지: "+str(Dust25[0]))
        DustText2.pack()
        DustText2.place(x=300,y=520)

        if Dust10[0] < 31:
            photo = PhotoImage(file="image/good.png")
        elif Dust10[0] >= 31 and Dust10[0] < 81:
            photo = PhotoImage(file="image/nomal.png")
        elif Dust10[0] >= 81 and Dust10[0] < 151:
            photo = PhotoImage(file="image/bad.png")
        else:
            photo = PhotoImage(file="image/shit.png")
        imagelabel = Label(g_daywindow, image=photo)
        imagelabel.pack()
        imagelabel.place(x=300, y=310)

        self.canvas = Canvas(g_daywindow, bg='white', width='150', height='150', image=imagelabel)
        self.canvas.pack()
        #self.canvas.place(x=300, y=350)
        #self.canvas.create_text(50, 125, text="미세먼지:  "+str(Dust10[0]))
        #self.canvas.create_text(50, 140, text="초미세먼지: "+str(Dust25[0]))

    def GoogleMap(self):
        #p = PhotoImage(file="image/Clubs1.png")
        myimage=PhotoImage(file="image/Clubs1.png")
        self.GooglemapButton = Button(g_daywindow, width=6, height=3, command=self.OpenMap)
        self.GooglemapButton.place(x=30,y=530)

    def OpenMap(self):
        print("오픈맵")

    def GMail(self):
        GMailButton = Button(g_daywindow, width='6', height='3', command=self.SendMail)
        GMailButton.place(x=100,y=530)

    def SendMail(self):
        #global value
        host = "smtp.gmail.com" # Gmail STMP 서버 주소.
        port = "587"
        htmlFileName = "logo.html"

        senderAddr = "kimwoochan1996@gmail.com"     # 보내는 사람 email 주소.
        recipientAddr = "wc5427@naver.com"   # 받는 사람 email 주소.

        DataInfo = now.strftime('%Y-%m-%d')

        text = DataInfo+" 오늘의 최고기온은 "+str(DataList[7])+" 이고 최저기온은 "+str(DataList[0])+"입니다\n또한 미세먼지 수치는 "+str(Dust10[0])+"이며 초미세먼지는 "+str(Dust25[0])+"입니다"
        #msg = MIMEBase("multipart", "alternative")
        msg = MIMEText(text)
        msg['Subject'] = DataInfo+" 오늘의 날씨 정보"
        msg['From'] = senderAddr
        msg['To'] = recipientAddr

        s = mysmtplib.MySMTP(host,port)
        s.ehlo()
        s.starttls()
        s.ehlo()
        s.login("kimwoochan1996@gmail.com","dkdldb127!!")
        s.sendmail(senderAddr , [recipientAddr], msg.as_string())
        s.close()

    def Telegram(self):
        pass


    def __init__(self):
        #wall = PhotoImage(file = 'back.png')
        #wall_label = Label(image = wall)
        #wall_label.place(x = 0,y = 0)
        self.UpTemparature = 0
        self.DownTemparature = 0
        self.canvas = Canvas(g_daywindow, bg='azure', width='500', height='600')
        self.canvas.pack()
        self.canvas.place(x=0,y=0)
        self.InitSearchEntry()
        self.InitSearchButton()

        self.WeatherInfoText()
        self.WeatherInfoPicture()
        self.TemperatureInfo()
        self.TemperatureGraph()
        self.DustInfo()

        self.GoogleMap()
        self.GMail()
        self.Telegram()

        g_daywindow.mainloop()


MainGUI()
