# Author: Burak Dogancay
#Graph generating tool for creating flowcart and fow diagram
#pip install pydotplus
import pydotplus
import pygraphviz as pgv

def exampleChart():
   graph_tb2 = pydotplus.graph_from_dot_file('demo.dot')
   graph_tb2.write_svg('test.svg') # generate graph in svg.

def pyGraphizFunct():
   G = pgv.AGraph("demo.dot")
   G.draw('test', format='svg', prog='dot')
    
def main():
  exampleChart()
    

if __name__ == '__main__':
    main()