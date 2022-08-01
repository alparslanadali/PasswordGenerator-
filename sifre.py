import random
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QWidget,QApplication,QCheckBox,QLabel,QPushButton,QVBoxLayout
import sys
class pencere(QWidget):

    def __init__(self):
        super().__init__()
        self.init_ui()


    def init_ui(self):
        self.harfler = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        self.sayılar = '0123456789'
        self.ozelkarakter = "!#$%&'()*+,-./:;<=>?@[\]^_`{|}~"
        self.sifre =""
        self.kontrol = QCheckBox('Özel Karakter olsun mu ?')
        self.basamak1 = QtWidgets.QLabel('Şifre Kaç Basamaklı olsun ?')
        self.basamak = QtWidgets.QLineEdit()
        self.buton = QPushButton('Şifreyi oluştur!')
        self.parola_alanı = QtWidgets.QLineEdit()
        self.sahip = QtWidgets.QLabel("#Alparslan Adalı saygıyla Sunar.... 07.2022")
        v_box = QVBoxLayout()
        v_box.addWidget(self.kontrol)
        v_box.addWidget(self.basamak1)
        v_box.addWidget(self.basamak)
        v_box.addWidget(self.buton)
        v_box.addWidget(self.parola_alanı)
        v_box.addWidget(self.sahip)
        self.buton.clicked.connect(lambda :self.click(self.kontrol.isChecked(),self.basamak,self.parola_alanı,self.sifre,self.sayılar,self.harfler,self.ozelkarakter))
        self.setLayout(v_box)
        self.setWindowTitle("Şifre Oluşturucu!")
        self.show()

    def click(self,kontrol,basamak,parola_alanı,sifre,sayılar,harfler,ozelkarakter):
        basamakx = int(basamak.text())
        Baskı = ''
        if kontrol:
            for i in range(0, basamakx):
                sifre =random.choice(harfler+sayılar+ozelkarakter)
                Baskı= Baskı+sifre

        else:
            for i in range(0, basamakx):
                sifre =random.choice(harfler+sayılar)
                Baskı = Baskı + sifre
        parola_alanı.setText(Baskı)

app = QApplication(sys.argv)
pencere = pencere()
sys.exit(app.exec_())