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
import spam

g_daywindow = Tk()
g_daywindow.title("Weather_Reminder")
g_daywindow.geometry("550x600")
DataList = []
DustState = []
Dust10 = []
Dust25 = []
DustInfo = []
myimagelabel = []
now = datetime.datetime.now()

class MainGUI:
    def InitSearchEntry(self):
        global SearchListBox

        myFont2 = font.Font(g_daywindow, size=20, weight='bold')
        MainName = Label(g_daywindow, font = myFont2, text="Weather_Reminder")
        MainName.place(x=140,y=20)

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
        global SearchSiteListBox
        ListBoxScrollBar = Scrollbar(g_daywindow)
        ListBoxScrollBar.pack()
        ListBoxScrollBar.place(x=130,y=70)

        myFont =font.Font(g_daywindow, size=10, weight='bold')
        SearchSiteListBox = Listbox(g_daywindow, font=myFont, activestyle='none',
                                width=15, height=3, borderwidth=2,
                                yscrollcommand=ListBoxScrollBar.set)
        SearchSiteListBox.insert(0,str(spam.start()))
        conn = http.client.HTTPConnection("apis.data.go.kr")
        hangul_utf8 = urllib.parse.quote("경기")
        conn.request("GET", "/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?serviceKey=JeJzrQJprx9UjQkk7hibZqu2lXn9btXlpDpGp3KZL%2F8yEytBMzILptb4RUnKav%2FNndTc3oz6JVuKNfHsxehLuQ%3D%3D&returnType=xml&numOfRows=100&pageNo=1&sidoName="+hangul_utf8+"&ver=1.0")
        req = conn.getresponse()

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

                i = 1

                for temp in item:
                    if temp.nodeName == "item":
                        realnode = temp.childNodes
                        SearchSiteListBox.insert(i, str(realnode[41].firstChild.nodeValue))
                        i += 1

        SearchSiteListBox.insert(i+1,str(spam.end()))

        SearchSiteListBox.pack()
        SearchSiteListBox.place(x=310, y=70)

        myFont = font.Font(g_daywindow, size=15, weight='bold')
        DustText = Label(g_daywindow, font=myFont, text="미세먼지 정보")
        DustText.pack()
        DustText.place(x=310,y=310)

        #self.canvas = Canvas(g_daywindow, bg='white', width='150', height='150')
        #self.canvas.pack()
        #self.canvas.place(x=300, y=350)

    def InitSearchDustButton(self):
        myFont =font.Font(g_daywindow, size=10, weight='bold')
        SearchButton = Button(g_daywindow, font=myFont, text="검색",
                              command=self.SearchDustButtonAction)
        SearchButton.pack()
        SearchButton.place(x=450, y=80)

    def SearchDustButtonAction(self):
        myListBox = SearchSiteListBox.curselection()[0]
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
                            DustInfo.append(str(realnode[5].firstChild.nodeValue))
                            DustInfo.append(str(realnode[7].firstChild.nodeValue))
                            DustInfo.append(str(realnode[9].firstChild.nodeValue))
                            DustInfo.append(str(realnode[39].firstChild.nodeValue))
                            DustInfo.append(str(realnode[45].firstChild.nodeValue))
                            print(DustInfo[0])
                            print(DustInfo[1])
                            print(DustInfo[2])
                            print(DustInfo[3])
                            print(DustInfo[4])


        myFont =font.Font(g_daywindow, size=10, weight='bold')

        self.info1 = Label(g_daywindow, font=myFont, text="통합대기환경수치 : "+DustInfo[0])
        self.info1.pack()
        self.info1.place(x=320, y=150)
        self.info2 = Label(g_daywindow, font=myFont, text="이황산가스 농도 : "+DustInfo[1])
        self.info2.pack()
        self.info2.place(x=320, y=180)
        self.info3 = Label(g_daywindow, font=myFont, text="일산화탄소 농도 : "+DustInfo[2])
        self.info3.pack()
        self.info3.place(x=320, y=210)
        self.info4 = Label(g_daywindow, font=myFont, text="이산화질소 농도 : "+DustInfo[3])
        self.info4.pack()
        self.info4.place(x=320, y=240)
        self.info5 = Label(g_daywindow, font=myFont, text="오존 농도 : "+DustInfo[4])
        self.info5.pack()
        self.info5.place(x=320, y=270)

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
        DustText.place(x=300,y=530)
        DustText2 = Label(g_daywindow, font=myFont, text="초미세먼지: "+str(Dust25[0]))
        DustText2.pack()
        DustText2.place(x=300,y=550)

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
        imagelabel.place(x=300, y=340)

        self.canvas = Canvas(g_daywindow, bg='white', width='150', height='150', image=imagelabel)
        self.canvas.pack()
        #self.canvas.place(x=300, y=350)
        #self.canvas.create_text(50, 125, text="미세먼지:  "+str(Dust10[0]))
        #self.canvas.create_text(50, 140, text="초미세먼지: "+str(Dust25[0]))


    def GMail(self):
        global InputEntry
        TempFont = font.Font(g_daywindow, size=12, weight='bold', family = 'Consolas')
        InputEntry = Entry(g_daywindow, font = TempFont, width = 15, borderwidth = 12, relief = 'ridge')
        InputEntry.pack()
        InputEntry.place(x=13, y=535)

        GMailButton = Button(g_daywindow, width='6', height='3', command=self.SendMail)
        GMailButton.place(x=200,y=530)

    def SendMail(self):
        #global value
        host = "smtp.gmail.com" # Gmail STMP 서버 주소.
        port = "587"
        htmlFileName = "logo.html"

        senderAddr = "kimwoochan1996@gmail.com"     # 보내는 사람 email 주소.
        recipientAddr = str(InputEntry.get())  # 받는 사람 email 주소.

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


    def __init__(self):
        #wall = PhotoImage(file = 'back.png')
        #wall_label = Label(image = wall)
        #wall_label.place(x = 0,y = 0)
        self.UpTemparature = 0
        self.DownTemparature = 0
        self.canvas = Canvas(g_daywindow, bg='azure', width='550', height='600')
        self.canvas.pack()
        self.canvas.place(x=0,y=0)
        self.InitSearchEntry()
        self.InitSearchButton()

        self.TemperatureInfo()
        self.TemperatureGraph()
        self.DustInfo()
        self.InitSearchDustButton()

        self.GMail()

        g_daywindow.mainloop()


MainGUI()
