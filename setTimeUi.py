# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'setTime.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class SetTimeUi(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(318, 159)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/clock.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setStyleSheet("background-color: rgb(0, 177, 130);\n"
                             "")
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.spinBox_2 = QtWidgets.QSpinBox(Dialog)
        self.spinBox_2.setGeometry(QtCore.QRect(180, 54, 71, 41))
        self.spinBox_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                     "font: 16pt \"Bauhaus 93\";")
        self.spinBox_2.setMaximum(59)
        self.spinBox_2.setObjectName("spinBox_2")
        self.spinBox_3 = QtWidgets.QSpinBox(Dialog)
        self.spinBox_3.setGeometry(QtCore.QRect(50, 54, 81, 41))
        self.spinBox_3.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                     "font: 16pt \"Bauhaus 93\";")
        self.spinBox_3.setObjectName("spinBox_3")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 20, 131, 21))
        self.label.setStyleSheet("font: 16pt \"Bauhaus 93\";\n"
                                 "color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(140, 59, 21, 31))
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);\n"
                                   "font: 14pt \"Bauhaus 93\";")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(260, 59, 41, 31))
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);\n"
                                   "font: 14pt \"Bauhaus 93\";")
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(100, 120, 93, 28))
        self.pushButton.setStyleSheet("font: 10pt \"Bauhaus 93\";\n"
                                      "color: rgb(255, 255, 255);\n"
                                      "background-color: rgb(0, 124, 91);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(200, 120, 93, 28))
        self.pushButton_2.setStyleSheet("font: 10pt \"Bauhaus 93\";\n"
                                        "color: rgb(255, 255, 255);\n"
                                        "background-color: rgb(0, 124, 91);")
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "SetTime"))
        self.label.setText(_translate("Dialog", "SET TIME:"))
        self.label_2.setText(_translate("Dialog", "H"))
        self.label_3.setText(_translate("Dialog", "MIN"))
        self.pushButton.setText(_translate("Dialog", "OK"))
        self.pushButton_2.setText(_translate("Dialog", "CANCEL"))
