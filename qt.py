#!/usr/bin/python
import sys
import cv2 as cv
import random
from PyQt4 import QtGui, QtCore

from matplotlib.backends.backend_qt4agg import (
    FigureCanvasQTAgg as FigureCanvas,
    NavigationToolbar2QT as NavigationToolbar)

from numpy import array

import matplotlib.pyplot as plt

import getdata


class MainWindow(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self)
        self.mainWidget = QtGui.QWidget()

        #Объекты фигуры, поля, инструментов и слайдеров
        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        self.toolbar = NavigationToolbar(self.canvas, self)
        self.button = QtGui.QPushButton('Plot')
        self.slider1 = QtGui.QSlider(QtCore.Qt.Horizontal, self)
        self.slider2 = QtGui.QSlider(QtCore.Qt.Horizontal, self)
        self.lcd1 = QtGui.QLCDNumber(self)
        self.lcd2 = QtGui.QLCDNumber(self)
        #Расположение в сетке
        grid = QtGui.QGridLayout()

        grid.addWidget(self.toolbar, 0, 0)
        grid.addWidget(self.canvas, 1, 0)
        grid.addWidget(self.button, 2, 0)
        grid.addWidget(self.slider1, 3, 0)
        grid.addWidget(self.slider2, 4, 0)
        grid.addWidget(self.lcd1, 3, 1)
        grid.addWidget(self.lcd2, 4, 1)
        self.mainWidget.setLayout(grid)
        self.setCentralWidget(self.mainWidget)

        #события
        self.connect(self.slider1,  QtCore.SIGNAL('valueChanged(int)'),     self.lcd1, QtCore.SLOT('display(int)') )
        self.connect(self.slider2,  QtCore.SIGNAL('valueChanged(int)'),     self.lcd2, QtCore.SLOT('display(int)') )
        self.button.clicked.connect(self.plot)

    def plot(self):
        #a=main.update()
        #img=cv.imread('5.jpg', 1) 
        img=getdata.update()
        #print(type(img))
        # ax = self.figure.add_subplot(111)
        # ax.imshow(img, cmap = 'gray', interpolation = 'bicubic')
        # self.canvas.show()
        self.figure.clear()
        self.axes = self.figure.add_subplot(111)
        #self.axes.plot(self.x, self.y, 'ro')
        self.axes.imshow(img, cmap = 'gray', interpolation = 'bicubic')
        #self.axes.xticks([]), self.axes.yticks([])
        #self.axes.plot([1,2,3])
        self.canvas.draw()


app = QtGui.QApplication(sys.argv)
main = MainWindow()
main.show()
sys.exit(app.exec_())