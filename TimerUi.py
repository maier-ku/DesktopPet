# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TimerUi.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class TimerUi(object):
    def setupUi(self, TimerUi):
        TimerUi.setObjectName("TimerUi")
        TimerUi.resize(426, 158)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/clock.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        TimerUi.setWindowIcon(icon)
        TimerUi.setStyleSheet("background-color: rgb(0, 170, 127);")
        self.lcdNumber = QtWidgets.QLCDNumber(TimerUi)
        self.lcdNumber.setGeometry(QtCore.QRect(160, 50, 111, 51))
        self.lcdNumber.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lcdNumber.setObjectName("lcdNumber")
        self.progressBar = QtWidgets.QProgressBar(TimerUi)
        self.progressBar.setGeometry(QtCore.QRect(20, 10, 301, 23))
        self.progressBar.setStyleSheet("font: 10pt \"Bauhaus 93\";\n"
"color: rgb(255, 255, 255);")
        self.progressBar.setProperty("value", 23)
        self.progressBar.setObjectName("progressBar")
        self.pushButton = QtWidgets.QPushButton(TimerUi)
        self.pushButton.setGeometry(QtCore.QRect(20, 120, 93, 28))
        self.pushButton.setStyleSheet("font: 10pt \"Bauhaus 93\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 124, 91);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(TimerUi)
        self.pushButton_2.setGeometry(QtCore.QRect(120, 120, 93, 28))
        self.pushButton_2.setStyleSheet("background-color: rgb(0, 124, 91);\n"
"font: 10pt \"Bauhaus 93\";\n"
"color: rgb(255, 255, 255);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(TimerUi)
        self.pushButton_3.setGeometry(QtCore.QRect(320, 120, 93, 28))
        self.pushButton_3.setStyleSheet("font: 10pt \"Bauhaus 93\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 124, 91);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.lcdNumber_2 = QtWidgets.QLCDNumber(TimerUi)
        self.lcdNumber_2.setGeometry(QtCore.QRect(300, 50, 111, 51))
        self.lcdNumber_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lcdNumber_2.setObjectName("lcdNumber_2")
        self.label = QtWidgets.QLabel(TimerUi)
        self.label.setGeometry(QtCore.QRect(280, 60, 21, 31))
        self.label.setStyleSheet("font: 75 25pt \"Berlin Sans FB Demi\";\n"
"color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(TimerUi)
        self.label_2.setGeometry(QtCore.QRect(140, 60, 21, 31))
        self.label_2.setStyleSheet("font: 75 25pt \"Berlin Sans FB Demi\";\n"
"color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.lcdNumber_3 = QtWidgets.QLCDNumber(TimerUi)
        self.lcdNumber_3.setGeometry(QtCore.QRect(20, 50, 111, 51))
        self.lcdNumber_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lcdNumber_3.setObjectName("lcdNumber_3")
        self.label_3 = QtWidgets.QLabel(TimerUi)
        self.label_3.setGeometry(QtCore.QRect(320, 0, 31, 31))
        self.label_3.setStyleSheet("font:10pt \"MS Shell Dlg 2\";")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(TimerUi)
        self.label_4.setGeometry(QtCore.QRect(350, 10, 61, 21))
        self.label_4.setStyleSheet("font: 10pt \"Bauhaus 93\";\n"
"color: rgb(255, 255, 255);")
        self.label_4.setObjectName("label_4")

        self.retranslateUi(TimerUi)
        QtCore.QMetaObject.connectSlotsByName(TimerUi)

    def retranslateUi(self, TimerUi):
        _translate = QtCore.QCoreApplication.translate
        TimerUi.setWindowTitle(_translate("TimerUi", "Timer"))
        self.pushButton.setText(_translate("TimerUi", "Pause"))
        self.pushButton_2.setText(_translate("TimerUi", "Continue"))
        self.pushButton_3.setText(_translate("TimerUi", "Back"))
        self.label.setText(_translate("TimerUi", ":"))
        self.label_2.setText(_translate("TimerUi", ":"))
        self.label_3.setText(_translate("TimerUi", "🧭 "))
        self.label_4.setText(_translate("TimerUi", "TextLabel"))
