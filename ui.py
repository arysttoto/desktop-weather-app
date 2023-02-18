from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(650, 550)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 650, 131))
        self.frame.setStyleSheet(u"background-color: #111111;\n"
"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(240, 40, 418, 61))
        font = QFont()
        font.setFamily(u"Arial")
        font.setPointSize(40)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: #f5b342;")
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(30, 10, 101, 111))
        self.label_2.setPixmap(QPixmap(u"2862807.png"))
        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(0, 129, 650, 421))
        font1 = QFont()
        font1.setFamily(u"American Typewriter")
        font1.setPointSize(18)
        font1.setBold(True)
        font1.setWeight(75)
        self.frame_2.setFont(font1)
        self.frame_2.setStyleSheet(u"background-color: #333333")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.pushButton = QPushButton(self.frame_2)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(360, 20, 191, 41))
        font2 = QFont()
        font2.setFamily(u"Arial")
        font2.setPointSize(18)
        font2.setBold(True)
        font2.setWeight(75)
        self.pushButton.setFont(font2)
        self.pushButton.setStyleSheet(u"border: 2px solid  #f5b342;\n"
"border-radius: 20;\n"
"\n"
"\n"
"")
        self.comboBox = QComboBox(self.frame_2)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(100, 20, 151, 41))
        self.comboBox.setFont(font2)
        self.comboBox.setStyleSheet(u"border: 2px solid  #f5b342;\n"
"border-radius: 20;\n"
"padding:10px;\n"
"")
        self.label_3 = QLabel(self.frame_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 200, 261, 191))
        self.label_3.setFont(font2)
        self.label_3.setStyleSheet(u"background-color:#222222;\n"
"border-radius: 30px;\n"
"color: #682fa8;\n"
"padding: 10px;")
        self.label_4 = QLabel(self.frame_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(370, 200, 261, 191))
        self.label_4.setFont(font2)
        self.label_4.setStyleSheet(u"background-color:#222222;\n"
"border-radius: 30px;\n"
"color: #682fa8;\n"
"padding: 10px;")
        self.label_5 = QLabel(self.frame_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(140, 70, 391, 31))
        font3 = QFont()
        font3.setFamily(u"Arial")
        font3.setPointSize(36)
        font3.setBold(True)
        font3.setWeight(75)
        self.label_5.setFont(font3)
        self.label_5.setStyleSheet(u"color: #f5b342;\n"
"")
        self.label_6 = QLabel(self.frame_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(250, 120, 71, 71))
        self.label_6.setPixmap(QPixmap(u"3183342 copy.png"))
        self.label_7 = QLabel(self.frame_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(350, 120, 71, 71))
        self.label_7.setPixmap(QPixmap(u"3183342.png"))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Weather Now App", None))
        self.label_2.setText("")
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Find by country!", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Amsterdam", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Almaty", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Berlin", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"Dublin", None))
        self.comboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"Moscow", None))
        self.comboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"Kiev", None))
        self.comboBox.setItemText(6, QCoreApplication.translate("MainWindow", u"Kairo", None))
        self.comboBox.setItemText(7, QCoreApplication.translate("MainWindow", u"Rome", None))
        self.comboBox.setItemText(8, QCoreApplication.translate("MainWindow", u"Saint Petersburg", None))
        self.comboBox.setItemText(9, QCoreApplication.translate("MainWindow", u"Abu Dhabi", None))
        self.comboBox.setItemText(10, QCoreApplication.translate("MainWindow", u"Aktau", None))
        self.comboBox.setItemText(11, QCoreApplication.translate("MainWindow", u"Saratov", None))
        self.comboBox.setItemText(12, QCoreApplication.translate("MainWindow", u"Paris", None))

        self.label_3.setText("")
        self.label_4.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Weather in Amsterdam", None))
        self.label_6.setText("")
        self.label_7.setText("")
    # retranslateUi

