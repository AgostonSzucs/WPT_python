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
from PyQt4 import QtGui, uic

import graph
 
# Thse QWidget widget is the base class of all user interface objects in PyQt4.
class QT_window(QtGui.QMainWindow):
    validLetters = "ABCDEF0123456789"
    def __init__(self, parent=None):
        super(QT_window, self).__init__(parent)
        uic.loadUi('WPT_manual.ui', self)
        
        
        self.initUI()
        
    def initUI(self):
        
        self.setGeometry(100, 100, 1000, 1000)
        self.setWindowTitle('WPT Manual interface')
        # self.setWindowIcon(QtGui.QIcon('web.png')) 
        self.figure = plt.figure()
        BoxLayout = QtGui.QVBoxLayout()
        self.graph_area.canvas = FigureCanvas(self.figure)
        button_x = 1
        button_y = 1
        for name in glob.glob('dynamic/*'):
            name_raw = name.split('\\')[1].split('.')[0]
            self.button = QtGui.QPushButton(name_raw,self)
            self.button.setObjectName(name_raw)
            self.button.clicked.connect(self.initGraph)
            self.button.setFixedWidth(80)
            self.button.setFixedHeight(30)
            self.gridLayout.addWidget(self.button,button_x,button_y)
            button_x += 1
            if(button_x % 3 == 1 and button_x != 1):
                button_y += 1
                button_x = 1
        
        self.graph_area.setGeometry(10, 250, 980, 500)
        BoxLayout.addWidget(self.graph_area.canvas)
        self.graph_area.setLayout(BoxLayout)
        self.show()
    def initGraph(self):        
        # create an axis
        self.ax = self.figure.add_subplot(111)
        self.file_name =  str(self.sender().objectName())
        # plot data
        ani = animation.FuncAnimation(self.figure,self.animate, interval=200)
        self.graph_area.canvas.draw()
        
    def animate(self,i):
        self.ax.clear()
        pullData = open('/Users/agoston_dev/WPT_python/Anaconda_projects/Dynamic_graph/dynamic/'+self.file_name+'.txt',"r").read();
        dataArray = pullData.split('\n')
        xar = []
        yar = []
        x_label = []
        i = 0
        for eachLine in dataArray:
            x_label.append(int(i))
            i+=1
            if len(eachLine)>1:
                x,y = eachLine.split('-')
                newString=''
                for char in y:
                    if char in self.validLetters:
                        newString += char
                y = newString
                xar.append(x)
                yar.append(int(y,16))
                    
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
    