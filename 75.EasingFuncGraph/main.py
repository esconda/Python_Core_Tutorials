#Author : Burak Dogancay
import matplotlib.pyplot as plt
import numpy as np
import EasingFuncGraph as EaseClass

def mathPlot(xVar,yVar,pMainTitle):
    plt.plot(xVar,yVar,color = "red" , label = pMainTitle)
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title(pMainTitle)
    plt.legend()# it puts all elemnts in the graph
    plt.grid(True, linestyle = "--", alpha = 0.5) #draw grid in the graph
    plt.show()

def plotProcess(easeObject, easeName):
    x = np.arange(start = 0, stop = 1, step = 0.001)
    y = list(map(easeObject, x))
    mathPlot(x,y,easeName)
       
def main():
    #EaseInQuadProcess
    easeInQuad = EaseClass.EaseInQuad(start=0, end=1, duration=1)
    plotProcess(easeInQuad,"EaseInQuad")
    
    #EaseOutQuadProcess
    easeOutQuad = EaseClass.EaseOutQuad(start=0, end=1, duration=1)
    plotProcess(easeOutQuad,"EaseOutQuad")
    
    #EaseInOutQuad
    easeInOutQuad = EaseClass.EaseInOutQuad(start = 0, end = 1, duration = 1)
    plotProcess(easeInOutQuad,"EaseInOutQuad")
    
    
    
if __name__ == '__main__':
    main()