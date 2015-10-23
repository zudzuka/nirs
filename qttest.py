import sys


from matplotlib.figure import Figure

from matplotlib.backends.backend_qt4agg import (
    FigureCanvasQTAgg as FigureCanvas,
    NavigationToolbar2QT as NavigationToolbar)
from matplotlib.backends import qt4_compat



from PyQt4.QtCore import *
from PyQt4.QtGui import *


class AppForm(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        #self.x, self.y = self.get_data()
        self.main_frame = QWidget() 
        self.fig = Figure((5.0, 4.0), dpi=100)
        self.canvas = FigureCanvas(self.fig)
        #self.canvas.setParent(self.main_frame)
        #self.canvas.setFocusPolicy(Qt.StrongFocus)
        #self.canvas.setFocus()
        self.mpl_toolbar = NavigationToolbar(self.canvas, self.main_frame)

        vbox = QVBoxLayout()
        vbox.addWidget(self.canvas)  # the matplotlib canvas
        vbox.addWidget(self.mpl_toolbar)
        self.main_frame.setLayout(vbox)
        self.setCentralWidget(self.main_frame)



app = QApplication(sys.argv)
form = AppForm()
form.show()
app.exec_()
