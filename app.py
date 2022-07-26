import sys
import random as rd
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
        
    

    def initUI(self):
        self.setWindowTitle('Rock Scissors Paper')
        
        # scissors
        self.lbl = QLabel(self)
        self.lbl.resize(300,300)
        scissors = QPixmap('./image/가위.png')
        self.lbl.move(100,0)
        self.lbl.setPixmap(QPixmap(scissors))
        
        # scissors2
        self.sci = QLabel(self)
        self.sci.resize(300,300)
        scissors2 = QPixmap('./image/가위.png')
        
        btn = QPushButton('가위',self)
        btn.move(100,270)
        
        # rock
        self.lbl2 = QLabel(self)
        self.lbl2.resize(300,300)
        rock = QPixmap('./image/바위.png')
        self.lbl2.move(320,0)
        self.lbl2.setPixmap(QPixmap(rock))
        btn2 = QPushButton('바위',self)
        btn2.move(350,270)
        
        # paper
        self.lbl3 = QLabel(self)
        self.lbl3.resize(300,300)
        paper = QPixmap('./image/보.png')
        self.lbl3.move(630,0)
        self.lbl3.setPixmap(QPixmap(paper))
        btn3 = QPushButton('보',self)
        btn3.move(670,270)
        
        # 버튼 클릭시 0,1,2 전달
        btn.clicked.connect(self.go_zero)
        btn2.clicked.connect(self.go_one)
        btn3.clicked.connect(self.go_two)
        
        self.move(300, 300)
        self.resize(1000, 700)
        self.show()
        

        
        
    def go_zero(self):
        # 가위 0 바위 1 보 2
        a = 0
        
        
        com = rd.choice([0, 1, 2])
        if com == a:
            
            scissors2 = QPixmap('./image/가위.png')
            self.sci.move(0,200)
            self.sci.setPixmap(QPixmap(scissors2))

            print('무승부')
        elif a == 0 and com == 1: 
            print('패배')
        else:
            print('승리')

    
    def go_one(self):
        a = 1
        com = rd.choice([0, 1, 2])
        if com == a:
            print('무승부')
        elif a == 1 and com == 2: 
            print('패배')
        else:
            print('승리')
    
    def go_two(self):
        a = 2
        com = rd.choice([0, 1, 2])
        if com == a:
            print('무승부')
        elif a == 2 and com == 0:
            print('패배')
        else:
            print('승리')        

if __name__ == '__main__':
   app = QApplication(sys.argv)
   ex = MyApp()
   sys.exit(app.exec_())