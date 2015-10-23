#embedding matplotlib in qt4 for dummies
import sys
from PyQt4 import QtGui

from matplotlib.backends.backend_qt4agg import (
    FigureCanvasQTAgg as FigureCanvas,
    NavigationToolbar2QT as NavigationToolbar)

import matplotlib.pyplot as plt

import random

class Window(QtGui.QDialog):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)

        # объект figure, который показываем на графике
        self.figure = plt.figure()

        # Объект поля canvas
        self.canvas = FigureCanvas(self.figure)

        # объект инструментов
        self.toolbar = NavigationToolbar(self.canvas, self)

        # Соединение кнопки
        self.button = QtGui.QPushButton('Plot')
        self.button.clicked.connect(self.plot)

        # установка сетки
        layout = QtGui.QVBoxLayout()
        layout.addWidget(self.toolbar)
        layout.addWidget(self.canvas)
        layout.addWidget(self.button)
        self.setLayout(layout)

    def plot(self):
        self.figure.clear()
        self.axes = self.figure.add_subplot(111)
        #self.axes.plot(self.x, self.y, 'ro')
        self.axes.imshow(self.data, interpolation='nearest')
        #self.axes.plot([1,2,3])
        self.canvas.draw()

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)

    main = Window()
    main.show()

    sys.exit(app.exec_())