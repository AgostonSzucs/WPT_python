import sys
import threading
import time
import random
import serial
import glob
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.animation as animation
from PyQt4.QtCore import pyqtSlot
from PyQt4 import QtGui     

import graph
 
# The QWidget widget is the base class of all user interface objects in PyQt4.
class QT_window(QtGui.QDialog):
    def __init__(self, parent=None):
        super(QT_window, self).__init__(parent)
        
        self.initUI()
        
    def initUI(self):
        
        self.setGeometry(500, 300, 500, 500)
        self.setWindowTitle('WPT Manual interface')
        # self.setWindowIcon(QtGui.QIcon('web.png')) 
        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        self.button = QtGui.QPushButton('Plot')
        self.button.clicked.connect(self.initGraph)
        
        layout = QtGui.QVBoxLayout()
        layout.addWidget(self.button)
        layout.addWidget(self.canvas)
        self.setLayout(layout)
    
        self.show()
    def initGraph(self):        
        # create an axis
        self.ax = self.figure.add_subplot(111)
        # plot data
        ani = animation.FuncAnimation(self.figure, self.animate, interval=200)
        self.canvas.draw()
        
    def animate(self,i):
        self.ax.clear()
        for name in glob.glob('/Users/agoston_developer/Anaconda_projects/Dynamic_graph/dynamic/*'):
            pullData = open(name,"r").read();
            dataArray = pullData.split('\n')
            xar = []
            yar = []
            x_label = []
            i = 0
            for eachLine in dataArray:
                x_label.append(int(i))
                i+=1
                if len(eachLine)>1:
                    x,y = eachLine.split(',')
                    y.replace(' ','')
                    y.replace("\r","")
                    y.replace("\x1d","")
                    y.rstrip('\r\n')
                    if y.strip(): 
                        print y
                    xar.append(x)
                    yar.append(int(y))
                    
            plt.xticks(x_label, xar)
            plt.gcf().subplots_adjust(bottom=0.15)
            self.ax.plot(yar)
            self.ax.set_xticklabels(xar, rotation=90)
         
if __name__ == "__main__":
        
    app = QtGui.QApplication(sys.argv)
    window = QT_window()
    #graph_obj = dyn_graph() 
    #ani = animation.FuncAnimation(QT_window.figure, graph_obj.animate, interval=1000)
    sys.exit(app.exec_())
    