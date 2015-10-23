#!/usr/bin/python
import sys

from PyQt4 import QtGui, QtCore

from matplotlib.backends.backend_qt4agg import (
    FigureCanvasQTAgg as FigureCanvas,
    NavigationToolbar2QT as NavigationToolbar)

import matplotlib.pyplot as plt

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

        #Расположение в сетке
        grid = QtGui.QGridLayout()

        grid.addWidget(self.toolbar, 0, 0)
        grid.addWidget(self.canvas, 1, 0)
        grid.addWidget(self.button, 2, 0)
        grid.addWidget(self.slider1, 3, 0)
        grid.addWidget(self.slider2, 4, 0)

        self.mainWidget.setLayout(grid)
        self.setCentralWidget(self.mainWidget)

app = QtGui.QApplication(sys.argv)
main = MainWindow()
main.show()
sys.exit(app.exec_())