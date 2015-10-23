import sys
import cv2 as cv
import random
from PyQt4 import QtGui, QtCore

from matplotlib.backends.backend_qt4agg import (
    FigureCanvasQTAgg as FigureCanvas,
    NavigationToolbar2QT as NavigationToolbar)

from numpy import array

import matplotlib.pyplot as plt

class Coins:
    summ=0
    def addcoin(self, r):
        if r>82:
            value=5
            self.summ=self.summ+5
        elif 75<=r<=82:
            value=2
            self.summ=self.summ+2
        elif r<75:
            value=1
            self.summ=self.summ+1
        return value

def update(p1, p2):
    img = cv.imread('6.jpg', 1) 
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    gray = cv.GaussianBlur(gray, (7, 7), 0.5)
    #edges = cv.Canny(gray, 0, 50) #есть в HoughCircles
    circles = cv.HoughCircles(gray,cv.HOUGH_GRADIENT,1,120,
                                param1=p1,param2=p2,minRadius=60,maxRadius=100)
    #circles = np.uint16(np.around(circles))
    money = Coins()
    for i in circles[0,:]:
        # Нарисовать окружности
        cv.circle(img, (i[0], i[1]), i[2], (0,255,0), 2)
        # Нарисовать их центры
        cv.circle(img, (i[0], i[1]), 2, (0,0,255), 3)

        v = money.addcoin(i[2])

        font = cv.FONT_HERSHEY_SIMPLEX
        cv.putText(img, str(v), (i[0],i[1]), font, 2, (255,0,0), 2, cv.LINE_AA)

    cv.putText(img, str(money.summ), (50,100), font, 2, (255,255,0), 2,         cv.LINE_AA)
    #print(type(img), 'AAAAAAAAA')
    return img


# plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
# plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
# plt.show()