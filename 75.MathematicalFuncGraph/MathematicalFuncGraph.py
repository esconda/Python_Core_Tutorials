#Author: Burak Dogancay
#This script shows some of the mathematical plots
import matplotlib.pyplot as plt
import numpy as np
class EasingBase:
    limit = (0, 1)

    def __init__(self, start: float = 0, end: float = 1, duration: float = 1):
        self.start = start
        self.end = end
        self.duration = duration

    def process(self, t: float) -> float:
        raise NotImplementedError

    def ease(self, alpha: float) -> float:
        t = self.limit[0] * (1 - alpha) + self.limit[1] * alpha
        t /= self.duration
        a = self.process(t)
        return self.end * a + self.start * (1 - a)

    def __call__(self, alpha: float) -> float:
        return self.ease(alpha)

class EaseInQuad(EasingBase):
    def process(self, t: float) -> float:
        return t * t
    
class EaseOutQuad(EasingBase):
     def process(self, t: float) -> float:
        return 1 - (1 - t) * (1 - t)
    
class EaseCubicOut(EasingBase):
    def process(self, t: float) -> float:
        return t * t * t

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
    easeInQuad = EaseInQuad(start=0, end=1, duration=1)
    plotProcess(easeInQuad,"EaseInQuad")
    
    #EaseOutQuadProcess
    easeOutQuad = EaseOutQuad(start=0, end=1, duration=1)
    plotProcess(easeOutQuad,"EaseOutQuad")
    
    
    
if __name__ == '__main__':
    main()
