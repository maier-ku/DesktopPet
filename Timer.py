# -*- coding: utf-8 -*-
"""
Created on Thu May 26 22:09:35 2022

@author: Lucien
"""
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from setTimeUi import SetTimeUi 
from TimerUi import TimerUi
import time
from datetime import datetime

class Timer(QWidget, TimerUi):
    _startPos = None
    _endPos = None
    _isTracking = False
    setHour = 0
    setMin = 0
    def __init__(self, parent=None):
        super(Timer, self).__init__(parent)
        
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAutoFillBackground(False)
        
        self.setupUi(self)
        
        
    def mouseMoveEvent(self, e: QMouseEvent):  # 重写移动事件
        self._endPos = e.pos() - self._startPos
        self.move(self.pos() + self._endPos)

    def mousePressEvent(self, e: QMouseEvent):
        if e.button() == Qt.LeftButton:
            self._isTracking = True
            self._startPos = QPoint(e.x(), e.y())

    def mouseReleaseEvent(self, e: QMouseEvent):
        if e.button() == Qt.LeftButton:
            self._isTracking = False
            self._startPos = None
            self._endPos = None
    
    def countdown(self):
        hour = self.setHour
        minute = self.setMin 
        second = 0
        while True:
            self.lcdNumber_3.display(hour)
            self.lcdNumber.display(minute)
            self.lcdNumber_2.display(second)
            self.repaint()
            if hour == 0 and minute == 0 and second == 0:
                # 改变背景颜色？
                break
            time.sleep(1)
            second -= 1 
            if second == -1:
                minute -= 1 
                second = 59
            if minute == -1:
                hour -= 1
                minute -= 1
            
    
            
            
        
class setTime(QDialog, SetTimeUi):
    _startPos = None
    _endPos = None
    _isTracking = False
    def __init__(self, parent=None):
        super(setTime, self).__init__(parent)
        
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAutoFillBackground(False)
        
        self.setupUi(self)
        
        self.timer = Timer()
        self.pushButton.clicked.connect(self.toTimer)
        self.pushButton_2.clicked.connect(self.cancel)
        
        self.timer.pushButton_3.clicked.connect(self.backtosetting)
        
        
    def mouseMoveEvent(self, e: QMouseEvent):  # 重写移动事件
        self._endPos = e.pos() - self._startPos
        self.move(self.pos() + self._endPos)

    def mousePressEvent(self, e: QMouseEvent):
        if e.button() == Qt.LeftButton:
            self._isTracking = True
            self._startPos = QPoint(e.x(), e.y())

    def mouseReleaseEvent(self, e: QMouseEvent):
        if e.button() == Qt.LeftButton:
            self._isTracking = False
            self._startPos = None
            self._endPos = None
            
    def toTimer(self):
        self.timer.move(self.pos())
        self.timer.setHour = self.spinBox_3.value()
        self.timer.setMin = self.spinBox_2.value()
        self.countdown_timer()

        self.timer.show()
        self.setVisible(False)
        self.timer.countdown()
        
    def cancel(self):
        self.setVisible(False)
        
    def backtosetting(self):
        self.move(self.timer.pos())
        self.timer.setVisible(False)
        self.setVisible(True)
        
    def countdown_timer(self):
        setHour = self.spinBox_3.value()
        setMin = self.spinBox_2.value()
        
        now = datetime.now()
        future_min = (now.minute + setMin) % 60
        future_hour = (now.hour + (now.minute + setMin) // 60 + setHour) % 24
        target_time = str(future_hour)+":"+str(future_min)
        
        self.timer.label_4.setText(target_time)
        
        