"""
@Project :tool
@File    :getHSV_2.py
@IDE     :PyCharm
@Author  :xiaoj
@Date    :2023/10/23 14:21
"""
import cv2
import numpy as np
from matplotlib import pyplot as plt

image=cv2.imread('D:\Desktop\\flower\\fake_flowers\\1698043024.png')
HSV=cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
def getpos(event,x,y,flags,param):
    if event==cv2.EVENT_LBUTTONDOWN: #定义一个鼠标左键按下去的事件
        print(HSV[y,x])

cv2.imshow("imageHSV",HSV)
cv2.imshow('image',image)
cv2.setMouseCallback("imageHSV",getpos)
cv2.waitKey(0)