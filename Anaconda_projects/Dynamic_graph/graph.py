import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time
import random

class dyn_graph():
    
    def __init__(self):
        self.fig = plt.figure()
        self.ax1 = self.fig.add_subplot(1,1,1)
    def __del__(self):
        pass
    def animate(self,i):
        localtime = time.asctime(time.localtime(time.time()))
        localtime = localtime.split(' ')
        f_write = open("sampleText.txt","a").write(localtime[3]+","+str(random.randint(0,50))+"\n")
        pullData = open("sampleText.txt","r").read()
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
                y.rstrip('\r\n')
                xar.append(x)
                yar.append(int(y))
        self.ax1.clear()
        plt.xticks(x_label, xar)
        plt.gcf().subplots_adjust(bottom=0.15)
        self.ax1.plot(yar)
        self.ax1.set_xticklabels(xar, rotation=90)
    
if __name__ == "__main__":
    graph_obj = dyn_graph()
    ani = animation.FuncAnimation(graph_obj.fig, graph_obj.animate, interval=1000)
    plt.show()