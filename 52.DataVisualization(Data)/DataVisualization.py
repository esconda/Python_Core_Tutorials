# Author: Burak Dogancay
import numpy as np
import os
import matplotlib.pyplot as plt
import seaborn as sns

def getSpecFile(pFileName):
  location = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__))) #it gets the folder location
  fileName= os.path.join(location,pFileName)#add file name to folder location
  return fileName

#Seaborn is a wrapper around Matplotlib that makes creating common statistical plots easy. The list of supported
#plots includes univariate and bivariate distribution plots, regression plots, and a number of methods for plotting
#categorical variables.
def seaBornExample():
  global myData
  myData = np.random.randn(1000)
  
  # Plot a histogram with both a rugplot and kde graph superimposed
  
  sns.displot(myData, kde=True, rug=True)
  # Use a dark background with no grid.
  sns.set_style('dark')
  # Create the plot again
  sns.displot(myData, kde=True, rug=True)
  plt.savefig(getSpecFile('Seaborn.png'))
  
def matPlotFunc():
 # Generate some data for plotting.
  x = [0, 1, 2, 3, 4, 5, 6]
  y = [i**2 for i in x]
  
  # Plot the data x, y with some keyword arguments that control the plot style.
  # Use two different plot commands to plot both points (scatter) and a line (plot).
  
  plt.scatter(x, y, c='blue', marker='x', s=100) # Create blue markers of shape "x" and size 100
  plt.plot(x, y, color='red', linewidth=2) # Create a red line with linewidth 2.
  
  # Add some text to the axes and a title.
  plt.xlabel('x data')
  plt.ylabel('y data')
  plt.title('An example plot')
  
  # Generate the plot and show to the user.
  plt.savefig(getSpecFile('Matplot.png'))
  
def main():
  seaBornExample()
  matPlotFunc()
  

if __name__ == '__main__':
    main()