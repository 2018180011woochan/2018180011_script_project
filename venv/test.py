'''#9.6 ~ 11.49
from tkinter import *
import random
class MainGUI:
    def __init__(self):
        window = Tk()
        window.title('Tic-Tac-Toe')
        frame = Frame(window)
        frame.pack()
        self.imageX = PhotoImage(file='image/x.gif')
        self.imageO = PhotoImage(file='image/o.gif')
        self.matrix = []
        for i in range(3):
            self.matrix.append([])
            for j in range(3):
                if random.randint(0,1):
                    img = self.imageX
                else:
                    img = self.imageO
                self.matrix[i].append(Label(frame, image=img))
                self.matrix[i][j].grid(row=i,column=j)
        Button(window,text='다시생성',command=self.refresh).pack()
        window.mainloop()
    def refresh(self):
        for i in range(3):
            for j in range(3):
                if random.randint(0,1):
                    img = self.imageX
                else:
                    img = self.imageO
                self.matrix[i][j]['image'] = img
MainGUI()'''

#12.5
from tkinter import *
class MainGUI:
    def __init__(self):
        window = Tk()
        window.title('Tic-Tac-Toe')
        frame = Frame(window)
        frame.pack()
        self.imageX = PhotoImage(file='image/x.gif')
        self.imageO = PhotoImage(file='image/o.gif')
        self.imageE = PhotoImage(file='image/empty.gif')
        self.matrix = []
        self.turn = True # 차례 O, X
        self.done = False
        for i in range(3):
            self.matrix.append([])
            for j in range(3):
                self.matrix[i].append(Button(frame, image=self.imageE, text=' ',
                                             command=lambda row=i,col=j:self.pressed(row,col)))
                self.matrix[i][j].grid(row=i,column=j)
        self.explain = StringVar()
        self.explain.set('플레이어 X 차례')
        Label(window, textvariable=self.explain).pack()
        Button(window, text='다시시작', command=self.refresh).pack()
        window.mainloop()
    def pressed(self,row,col):
        if not self.done and self.matrix[row][col]['text'] == ' ':
            if self.turn:
                self.matrix[row][col]['image'] = self.imageX
                self.matrix[row][col]['text'] = 'X'
            else:
                self.matrix[row][col]['image'] = self.imageO
                self.matrix[row][col]['text'] = 'O'
            self.turn = not self.turn
            if self.check() == '@':
                self.explain.set('비김')
            elif self.check() != ' ': #승자가 있음
                self.explain.set(self.check()+'가 이겼습니다.')
                self.done = True
            elif self.turn:
                self.explain.set('플레이어 X 차례')
            else:
                self.explain.set('플레이어 O 차례')
    def check(self):    #가로 3줄 세로 3줄 대각선 2줄 검사해서 같은 글자가 나오면 그 글자를 반환 아니면 ' '
        for i in range(3):  #각 행과 열에 대해서 검사
            ch = self.matrix[i][0]['text'] # i행 0열의 문자
            if ch != ' ' and ch == self.matrix[i][1]['text'] and ch == self.matrix[i][2]['text']:
                return ch
            ch = self.matrix[0][i]['text'] # i행 0열의 문자
            if ch != ' ' and ch == self.matrix[1][i]['text'] and ch == self.matrix[2][i]['text']:
                return ch
        ch = self.matrix[1][1]['text'] #1행 1열 문자
        if ch != ' ' and ch == self.matrix[0][0]['text'] and ch == self.matrix[2][2]['text']:
            return ch
        if ch != ' ' and ch == self.matrix[0][2]['text'] and ch == self.matrix[2][0]['text']:
            return ch
        flag = True
        for i in range(3):
            for j in range(3):
                if self.matrix[i][j]['text'] == ' ':
                    flag = False
                    break
            if flag == False:
                break
        if flag:
            return '@'
            #self.explain.set('비김')
        return ' '

    def refresh(self):
        self.turn = True
        self.done = False
        self.explain.set('플레이어 X차례')
        for i in range(3):
            for j in range(3):
                self.matrix[i][j]['image'] = self.imageE
                self.matrix[i][j]['text'] = ' '
MainGUI()
