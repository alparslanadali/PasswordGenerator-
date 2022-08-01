import sys

from PyQt5.QtWidgets import QWidget,QApplication,QCheckBox,QLabel,QPushButton,QVBoxLayout
from PyQt5 import QtWidgets


class Pencere(QWidget):
    def __init__(self):

        super().__init__()

        self.init_ui()

    def init_ui(self):

        self.checkbox = QCheckBox("Özel karakter olsun mu?")
        self.basamak1 = QLabel("Şifre Kaç basamaklı olsun")
        self.basamak = QtWidgets.QLineEdit()
        self.yazi_alani = QLabel("")
        self.buton = QPushButton("Şifre oluştur")

        v_box = QVBoxLayout()

        v_box.addWidget(self.checkbox)
        v_box.addWidget(self.yazi_alani)
        v_box.addWidget(self.buton)
        v_box.addWidget(self.basamak1)
        v_box.addWidget(self.basamak)

        self.setLayout(v_box)

        self.setWindowTitle("Check Box")

        self.buton.clicked.connect(lambda : self.click(self.checkbox.isChecked(),self.yazi_alani,self.basamak))

        self.show()

    def click(self,checkbox,yazi_alani,basamak):
        if checkbox:
            yazi_alani.setText("Python'ı seviyorsun çok güzel","basamak sayın")
        else:
            yazi_alani.setText("Niye Sevmiyorsun ? ")

app = QApplication(sys.argv)

pencere = Pencere()

sys.exit(app.exec_())
