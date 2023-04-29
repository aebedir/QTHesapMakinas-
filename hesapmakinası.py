import random
import string
import sqlite3
import sys
import time
from PyQt5 import QtWidgets
from hesap import Ui_MainWindow



class Window(QtWidgets.QMainWindow):       
    
    def __init__(self):
        super(Window, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.btn_1.clicked.connect(lambda:self.btn("1"))
        self.ui.btn_2.clicked.connect(lambda:self.btn("2"))
        self.ui.btn_3.clicked.connect(lambda:self.btn("3"))
        self.ui.btn_4.clicked.connect(lambda:self.btn("4"))
        self.ui.btn_5.clicked.connect(lambda:self.btn("5"))
        self.ui.btn_6.clicked.connect(lambda:self.btn("6"))
        self.ui.btn_7.clicked.connect(lambda:self.btn("7"))
        self.ui.btn_8.clicked.connect(lambda:self.btn("8"))
        self.ui.btn_9.clicked.connect(lambda:self.btn("9"))
        self.ui.btn_0.clicked.connect(lambda:self.btn("0"))
        self.ui.topla.clicked.connect(lambda:self.btn("topla"))
        self.ui.cikar.clicked.connect(lambda:self.btn("çıkar"))
        self.ui.carp.clicked.connect(lambda:self.btn("çarp"))
        self.ui.bol.clicked.connect(lambda:self.btn("böl"))
        self.ui.esit.clicked.connect(lambda:self.btn("esit"))
        self.ui.temizle.clicked.connect(lambda:self.btn("temizle"))



    def btn(self,deger):        
        if deger == "1":
            self.ui.txt_Ekran.setText(self.ui.txt_Ekran.text() + deger)
        if deger == "2":
            self.ui.txt_Ekran.setText(self.ui.txt_Ekran.text() + deger)
        if deger == "3":
            self.ui.txt_Ekran.setText(self.ui.txt_Ekran.text() + deger)
        if deger == "4":
            self.ui.txt_Ekran.setText(self.ui.txt_Ekran.text() + deger)
        if deger == "5":
            self.ui.txt_Ekran.setText(self.ui.txt_Ekran.text() + deger)
        if deger == "6":
            self.ui.txt_Ekran.setText(self.ui.txt_Ekran.text() + deger)
        if deger == "7":
            self.ui.txt_Ekran.setText(self.ui.txt_Ekran.text() + deger)
        if deger == "8":
            self.ui.txt_Ekran.setText(self.ui.txt_Ekran.text() + deger)
        if deger == "9":
            self.ui.txt_Ekran.setText(self.ui.txt_Ekran.text() + deger)
        if deger == "0":
            self.ui.txt_Ekran.setText(self.ui.txt_Ekran.text() + deger)
        if deger == "temizle":
            self.ui.txt_Ekran.setText("")
            self.ui.lblDeger.setText("")
            self.ui.lblDeger_2.setText("")
        if deger == "topla":                       
            if self.ui.lblDeger.text() == "":
                self.ui.lblDeger.setText(self.ui.txt_Ekran.text()) 
                self.ui.txt_Ekran.setText("")
            else:
                self.ui.lblDeger_2.setText(self.ui.txt_Ekran.text())     
        if deger == "çıkar":                       
            if self.ui.lblDeger.text() == "":
                self.ui.lblDeger.setText(self.ui.txt_Ekran.text()) 
                self.ui.txt_Ekran.setText("")
            else:
                self.ui.lblDeger_2.setText(self.ui.txt_Ekran.text())                  
        if deger == "esit":
            self.ui.lblDeger_2.setText(self.ui.txt_Ekran.text()) 
            self.ui.txt_Ekran.setText("") 
            deger1=self.ui.lblDeger.text()
            deger2=self.ui.lblDeger_2.text()            
            sonuc=int(deger1) + int(deger2)                       
            self.ui.txt_Ekran.setText(str(sonuc))
            
            
            
        

app = QtWidgets.QApplication(sys.argv)
win=Window()
win.show()
sys.exit(app.exec_())