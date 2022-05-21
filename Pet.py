# -*- coding: utf-8 -*-
"""
Created on Mon May 16 22:24:24 2022

@author: Lucien
"""

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

from PIL import Image
import random
import sys
import os
import configparser

#交互，位置
petname = '麦'
petscale = 0.25
bottomfix = 0.0
dragspeedx = 0
dragspeedy = 0
throwout = False
intotray = True
dropspeed = 0
gravity = 10
t = 4
gamespeed = 400.0
petactions = ['stand','walkleft','walkright','drag','falling']
petspeed = 6.0
petactionnum = [1,4,4,1,1]
#petactionrate = [0.8,0.2,0.2]
petactionrate = [0.2,0.4,0.4]
dragingfixx = 0.0
dragingfixy = 1000.0
standaction = ['kiss','lay','sit']
standactionnum = [2,4,4]
standactionrate = [0.32,0.32,0.36]
mirror = False

#动作
action = 0 #0:随机， 1：左右走，爬框框（移动）； 2：站立； 3：坐下； 4：亲亲； 5：趴趴； 
stopdrop = 0 #1：禁用掉落，移动不会掉回桌面。 0：开启掉落
onfloor = 1
onwall = 0
drop=1
dragging=0
playid=1 #图片编号，例如sit2.png中的2
playtime = 0 # 动作次数
playstand = -1 #detail?
petaction,petaction2=0,0
imgpath='sit1.png'
image_url = 'compress_img/'
image = image_url + 'sit1.png'
im = Image.open(image)
petwidth=im.size[0]
petheight=im.size[1]
mouseposx1,mouseposx2,mouseposx3,mouseposx4,mouseposx5=0,0,0,0,0
mouseposy1,mouseposy2,mouseposy3,mouseposy4,mouseposy5=0,0,0,0,0



class Pet(object):
    def __init__(self, width=1400, height=800):
        self.image_url = 'compress_img/'
        self.image_id = 2
        self.image_action = 'sit'
        self.image = self.image_url + self.image_action + str(self.image_id) + '.png'
        self.rect_x = width
        self.rect_y = height


class Label(QLabel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #右键菜单
        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.rightMenu)

    def rightMenu(self):
        menu = QMenu(self)
        #addAction定义菜单内容
        #menu.addAction(QAction(QIcon('img/net.png'), '浏览器', self, triggered=self.net))
        #menu.addAction(QAction(QIcon('images/music.ico'), '网易云', self, triggered=self.music))
        menu.addAction(QAction(QIcon('compress_img/kiss2.png'), '姐姐亲亲', self, triggered=self.kiss))
        menu.addAction(QAction(QIcon('compress_img/sit1.png'), '坐下歇会儿', self, triggered=self.sit))
        menu.addAction(QAction(QIcon('compress_img/lay3.png'), '趴姐姐身上歇会儿', self, triggered=self.lay))
        menu.addAction(QAction(QIcon('compress_img/walkright1.png'), '始终移动', self, triggered=self.wander))
        menu.addAction(QAction(QIcon('compress_img/stand1.png'), '站立不动', self, triggered=self.stand))
        menu.addAction(QAction(QIcon('img/gift.png'), '随机', self, triggered=self.randommove))
        
        menu.addSeparator()
        
        menu.addAction(QAction(QIcon('img/parachute.png'), '开启掉落', self, triggered=self.parachute))
        menu.addAction(QAction(QIcon('img/non_parachute.png'), '禁用掉落', self, triggered=self.non_parachute))
        
        menu.addSeparator()
        
        menu.addAction(QAction(QIcon('img/hide.png'), '隐藏', self, triggered=self.hide))
        menu.addAction(QAction(QIcon('img/exit.png'), '退出', self, triggered=self.quit))
        menu.exec_(QCursor.pos())
    
    def lay(self):
        global action
        action = 5
        
    def kiss(self):
        global action
        action = 4
    
    def sit(self):
        global action
        action = 3
    
    def stand(self):
        global action
        action = 2
        
    def wander(self):
        global action
        action = 1
        
    def randommove(self):
        global action
        action = 0
        
    def parachute(self):
        global stopdrop
        stopdrop = 0 
        
    def non_parachute(self):
        global stopdrop
        stopdrop = 1

    def quit(self):
        self.close()
        sys.exit()

    def hide(self):
        self.setVisible(False)


    @staticmethod
    def net():
        try:
            webbrowser.open('http://baidu.com')
        except:
            print('路径不正确')
            


class App(QWidget):
    def __init__(self):
        super(App, self).__init__()
        screen = QDesktopWidget().screenGeometry()
        self.tray()
        
        
        self.pet = Pet()
        self.is_follow_mouse = False
        self.setGeometry(0, 0, screen.width(), screen.height())

        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.SubWindow)
        self.setAutoFillBackground(False)
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        #self.showMaximized()

    
        #刷新qwidget
        self.repaint()
        
        screen = QDesktopWidget().screenGeometry()
        global screenwidth,screenheight,petleft,pettop
        screenwidth=screen.width()
        screenheight=screen.height()
        petleft = screenwidth-petwidth
        pettop = screenheight-petheight
        
        
        #初始图像
        pix = QPixmap(self.pet.image)
        self.pm_pet = QPixmap(self.pet.image)
        
        # 宠物标签
        self.lb_pet = Label(self)
        self.lb_pet.setPixmap(self.pm_pet)
        self.lb_pet.move(self.pet.rect_x, self.pet.rect_y)
        
        
        
        
        #self.lb_pet.setPixmap(pix)
        #self.lb_pet.setContextMenuPolicy(Qt.CustomContextMenu)
        #self.lb_pet.customContextMenuRequested.connect(self.rightMenu)
        #self.show()
        
        #self.init_ui()
        
        self.show()
        timer = QTimer(self)
        timer.timeout.connect(self.game)
        timer.start(400)

    def game(self):
        # 宠物实现gif效果
        #self.pet.gif()
        
        global petaction, petaction2, playstand, playnum, imgpath, playtime, playstand, playid
        global onfloor, drop, onwall
        global petwidth,petleft,pettop
        
        if drop==1 and onfloor==0: 
            playnum = 1
            if dragging==1:#实现拖拽
                imgpath='17.png'
                playid=1
            
            elif dragging==0 and stopdrop == 0:#实现掉落
                
                imgpath='18.png'
                playid=1
    
            self.drop()
            
            
            
            
        #1：左右走，爬框框（移动）；    
        elif action == 1:
            
            if playtime==0: #换动作
                petaction = random.random()
                playstand = -1
                playid = 1 
                
            #向右走    
            if petaction >= 0.5 and (petleft+petwidth+petspeed)<screenwidth:
                playnum = 4
                if playid < playnum:
                    imgpath=petactions[2]+str(playid)+'.png'
                    playid=playid+1
                    
                else:
                    imgpath=petactions[2]+str(playid)+'.png'
                    playid=1
                    
                petleft = petleft + petspeed

                
                self.lb_pet.move(int(petleft),int(pettop))
                
                if playtime == 0:
                    playtimemin = 3 
                    playtimemax = int((((screenwidth-(petleft+petwidth)))/petspeed)/playnum)
                    if playtimemax<=3:
                        playtimemax=3
                playtime = int(playtime)-1 
                
            #向左走
            elif petaction < 0.5 and petaction>=float(petactionrate[0]) and petleft>petspeed: 
                playnum = 4
                if playid<int(petactionnum[1]):
                    imgpath=petactions[1]+str(playid)+'.png'
                    playid=playid+1
                    
                else:
                    imgpath=petactions[1]+str(playid)+'.png'
                    playid=1
                    
                petleft = petleft - petspeed
                self.lb_pet.move(int(petleft),int(pettop))
                
                if playtime==0:
                    playtimemin=3
                    playtimemax=int((petleft)/petspeed/playnum)
                    if playtimemax<=1:
                        playtimemax=1
                playtime=int(playtime)-1
                
                if playtime==-1:
                    playtime=random.randint(1,playtimemax)*playnum

        #2：站立；     
        elif action == 2:
            playnum=3
            playstand=2
            
            if playstand < 4: 
                #imgpath=standaction[i]+str(playid)+'.png'
                imgpath='stand'+ str(playstand) +'.png'
                playstand = playstand + 1
            else:
                imgpath='stand' + str(playstand) + '.png'
                playstand = 1
                playid = 1
            
            if playtime==0:
                playtime = 10
                playtimemax=20
                
            playtime=int(playtime)-1 
            
        
                

        # 3：坐下；     
        elif action == 3:
             playnum=3
             playstand=1
             
             if playstand < 4: 
                 #imgpath=standaction[i]+str(playid)+'.png'
                 imgpath='sit'+ str(playstand) +'.png'
                 playstand = playstand + 1
             else:
                 imgpath='sit' + str(playstand) + '.png'
                 playstand = 1
                 playid = 1
             
             if playtime==0:
                 playtime = 10
                 playtimemax=20
                 
             playtime=int(playtime)-1 
             
             
        #4：亲亲；      
        elif action == 4:
            playnum=2
            playstand=1
            
            if playstand < 3: 
                imgpath='kiss'+ str(playstand) +'.png'
                playstand = playstand + 1
            else:
                imgpath='kiss' + str(playstand) + '.png'
                playstand = 1
                playid = 1
            
            if playtime==0:
                playtime = 10
                playtimemax=20
                
            playtime=int(playtime)-1 
            
        #5：趴趴；    
        elif action == 5:
             playnum=4
             playstand=1
             
             if playstand < 4: 
                 imgpath='lay'+ str(playstand) +'.png'
                 playstand = playstand + 1
             else:
                 imgpath='lay' + str(playstand) + '.png'
                 playstand = 1
                 playid = 1
             
             if playtime==0:
                 playtime = 10
                 playtimemax=20
                 
             playtime=int(playtime)-1 

            
        #0:随机
        elif action == 0:
            
            if playtime==0: #换动作
                petaction = random.random()
                playstand = -1
                playid = 1 
                
                
            #右    
            #if petaction >= (float(petactionrate[0])+float(petactionrate[1])) and (petleft+petwidth+petspeed)<screenwidth:
            if petaction >= (float(petactionrate[0])+float(petactionrate[1])):
                #向右走
                if petleft < (screenwidth - 0.75 * petwidth) and pettop > petheight:
                    playnum = 4
                    if playid < playnum:
                        imgpath=petactions[2]+str(playid)+'.png'
                        playid=playid+1
                    
                    else:
                        imgpath=petactions[2]+str(playid)+'.png'
                        playid=1
                    
                    petleft = petleft + petspeed                
                    self.lb_pet.move(int(petleft),int(pettop))
                 
                
                elif petleft >= (screenwidth - 0.75 * petwidth) and (pettop - petspeed) >= 0 and stopdrop == 0:
                    #爬上右墙
                    
                    playnum = 2
                    
                    if playid < playnum:
                        imgpath='rightclimb'+str(playid)+'.png'
                        playid=playid+1
                    
                    else:
                        imgpath='rightclimb'+str(playid)+'.png'
                        playid=1
                    
                    petleft = screenwidth - 0.75 * petwidth
                    pettop = pettop - petspeed
                    self.lb_pet.move(int(petleft),int(pettop))
                    
                    #从右往左爬天花板
                elif (pettop - petspeed) < 0 and stopdrop == 0:
                    playnum = 2
                        
                    if playid < playnum:
                        imgpath='lefttop'+str(playid)+'.png'
                        playid=playid+1
                    
                    else:
                        imgpath='lefttop'+str(playid)+'.png'
                        playid=1
                        
                    petleft = petleft - petspeed  
                    pettop = -0.25 * petheight
                    self.lb_pet.move(int(petleft),int(pettop))
                
                
                if playtime == 0:

                    playtimemin = 10
                    playtimemax = 50
                
                    if playtimemax<=3:
                        playtimemax=3
                playtime = int(playtime)-1 
                
            #左
            elif petaction<(float(petactionrate[0])+float(petactionrate[1])) and petaction>=float(petactionrate[0]) and petleft>petspeed: 
                #向左走
                if petleft < (-0.25 * petwidth) and pettop > height:
                    playnum = 4
                    if playid < playnum:
                        imgpath=petactions[1]+str(playid)+'.png'
                        playid=playid+1
                    
                    else:
                        imgpath=petactions[1]+str(playid)+'.png'
                        playid=1
                    
                    petleft = petleft - petspeed
                    self.lb_pet.move(int(petleft),int(pettop))
                    
                elif petleft <= (-0.25 * petwidth) and (pettop - petspeed) >= 0 and stopdrop == 0:
                    #爬上左墙
                    playnum = 2
                    
                    if playid < playnum:
                        imgpath='leftclimb'+str(playid)+'.png'
                        playid=playid+1
                    
                    else:
                        imgpath='leftclimb'+str(playid)+'.png'
                        playid=1
                    
                    petleft = -0.25 * petwidth
                    pettop = pettop - petspeed
                    self.lb_pet.move(int(petleft),int(pettop))
                    
                    #从左往右爬天花板
                elif (pettop - petspeed) < 0 and stopdrop == 0:
                    playnum = 2
                        
                    if playid < playnum:
                        imgpath='righttop'+str(playid)+'.png'
                        playid=playid+1
                    
                    else:
                        imgpath='righttop'+str(playid)+'.png'
                        playid=1
                        
                    petleft = petleft + petspeed  
                    pettop = -0.25 * petheight
                    self.lb_pet.move(int(petleft),int(pettop))
                
                if playtime==0:
                    playtimemin=3
                    playtimemax=50
                    if playtimemax<=1:
                        playtimemax=1
                playtime=int(playtime)-1
                
             #原地动作   
            elif petaction<float(petactionrate[0]):
                
                if playstand==-1:
                    temp=random.random()
                    temp2=0

                    for i in range(len(standactionrate)):
                        
                        if float(standactionrate[i])==0:
                            continue
                        temp2=temp2+float(standactionrate[i])
                        
                        if temp<temp2:
                            petaction2=i
                            playnum=int(standactionnum[i])
                            playstand=1
                            break
                            
                    
                    if playstand==-1:
                        playnum=int(standactionnum[0])
                        playstand=1
                
                if playstand<int(standactionnum[petaction2]):
                    #imgpath=standaction[i]+str(playid)+'.png'
                    imgpath=standaction[petaction2]+str(playstand)+'.png'
                    playstand=playstand+1
                else:
                    imgpath=standaction[petaction2]+str(playstand)+'.png'
                    playstand=1
                    playid=1
                
                if playtime==0:
                    playtimemin=10
                    playtimemax=20
                    
                playtime=int(playtime)-1
                ##print("Stand:"+str(petaction)+".Playid:"+str(playid)+"."+str(petaction2)+".Playstand:"+str(playstand)+".Playtime:"+str(playtime)+"Playnum:"+str(playnum))
                
            
                
            else:
                petaction=random.random()
                playstand=-1
            
            if playtime==-1:
                playtime=random.randint(1,playtimemax)*playnum
                
                
        petimage = image_url + imgpath
        self.pet.image = petimage
        pix = QPixmap(petimage)
        
        pix=pix.scaled(petwidth, petheight, aspectRatioMode=Qt.KeepAspectRatio)
        self.lb_pet.setPixmap(pix)
        pass
                
    
        #else:
         #   self.pm_pet = QPixmap(self.pet.image)
         #   self.lb_pet.setPixmap(self.pm_pet)
         #   pass

    def init_ui(self):

        self.setGeometry(0, 0, screen.width(), screen.height())

        # 宠物标签
        self.lb_pet.setPixmap(self.pm_pet)
        self.lb_pet.move(self.pet.rect_x, self.pet.rect_y)

        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.SubWindow)
        self.setAutoFillBackground(False)
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.showMaximized()

    #def mouseDoubleClickEvent(self, QMouseEvent):
     #   self.hide()

    def mousePressEvent(self, event):
        
        if event.button() == Qt.LeftButton:
            self.is_follow_mouse = True
            global onfloor, dragging, playid 
            dragging = 1 
            onfloor = 1
            if stopdrop == 0:
                onfloor=0
                playid = 1
            event.accept()
            self.setCursor(QCursor(Qt.OpenHandCursor))

    def mouseMoveEvent(self, event):
        global mouseposx1,mouseposx2,mouseposx3,mouseposx4,mouseposx5
        global mouseposy1,mouseposy2,mouseposy3,mouseposy4,mouseposy5
        global petleft,pettop,stopdrop
        
        if Qt.LeftButton and self.is_follow_mouse:
            self.pet.rect_x = QCursor.pos().x() - 77
            self.pet.rect_y = QCursor.pos().y() - 63
            self.lb_pet.move(self.pet.rect_x, self.pet.rect_y)
            petleft = self.pet.rect_x
            pettop = self.pet.rect_y 
            event.accept()
            if stopdrop == 0:
                mouseposx4=mouseposx3
                mouseposx3=mouseposx2
                mouseposx2=mouseposx1
                mouseposx1=QCursor.pos().x()
                mouseposy4=mouseposy3
                mouseposy3=mouseposy2
                mouseposy2=mouseposy1
                mouseposy1=QCursor.pos().y()
            
            
            

    def mouseReleaseEvent(self, event):
        global onfloor,dragging, playid, stopdrop
        global dragspeedx,dragspeedy,mouseposx1,mouseposx3,mouseposy1,mouseposy3
        if stopdrop == 0: #允许降落
            playid = 1 #播放降落图片 8.png
            onfloor = 0 
            dragging = 0 
        else:
            onfloor = 1 
            dragging = 0 
            
        
        self.is_follow_mouse = False
        self.setCursor(QCursor(Qt.ArrowCursor))
        
        if stopdrop == 0:
            dragspeedx = (mouseposx1-mouseposx3)/t
            #dragspeedy = (mouseposy1-mouseposy3)/t
            dragspeedy = 0
            mouseposx1=mouseposx3=0
            mouseposy1=mouseposy3=0
            
            
    def drop(self):
        global petleft,pettop
        global onfloor, dragging, dragspeedy
        if onfloor==0 and dragging==0:
            #算新坐标
            dropnext = pettop + dragspeedy * t + 0.5 * gravity * t**2 #y位移
            movenext = petleft + dragspeedx * t #x位移

            if movenext > screenwidth-petwidth:
                movenext = (screenwidth-petwidth)
            
            elif movenext <= 0:
                movenext = 0
            
            
            if dropnext >= (screenheight-petheight):
                dropnext = screenheight-petheight
                onfloor=1
                
            elif dropnext <= 0:
                dropnext = 0 
                dragspeedy = 0
            
            petleft = movenext
            pettop = dropnext
            self.lb_pet.move(int(petleft),int(pettop))

            

    def tray(self):
        
        tray = QSystemTrayIcon(self)
        tray.setIcon(QIcon('img/4.png'))

        display = QAction(QIcon('img/eye.png'), '显示', self, triggered=self.display)
        quit = QAction(QIcon('img/exit.png'), '退出', self, triggered=self.quit)
        menu = QMenu(self) 
        menu.addAction(quit)
        menu.addAction(display)        
        tray.setContextMenu(menu)
        tray.show()

    def quit(self):
        self.close()
        sys.exit()

    def hide(self):
        self.lb_pet.setVisible(False)

    def display(self):
        self.lb_pet.setVisible(True)
                
                
            


if __name__ == '__main__':
    app = QApplication(sys.argv)
    pet = App()
    sys.exit(app.exec_())