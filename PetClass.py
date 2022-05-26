# -*- coding: utf-8 -*-
"""
Created on Tue May 24 22:40:58 2022

@author: Lucien
"""

class Pet(object):
    def __init__(self, width=1400, height=800):
        self.image_url = 'compress_img/'
        self.image_id = 2
        self.image_action = 'sit'
        self.image = self.image_url + self.image_action + str(self.image_id) + '.png'
        self.rect_x = width
        self.rect_y = height