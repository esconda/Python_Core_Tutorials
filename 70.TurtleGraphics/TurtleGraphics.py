#Author: Burak Dogancay
import turtle
import multiprocessing
def exampleGraph():
    ninja = turtle.Turtle()
    ninja.speed(30)
    ninja.pencolor("red")
    for i in range(180):
        ninja.forward(100)
        ninja.right(30)
        ninja.forward(20)
        ninja.left(30)
        ninja.forward(50)
        ninja.right(30)
        ninja.penup()
        ninja.setposition(0, 0)
        ninja.pendown()
        ninja.right(2)
    turtle.done()
    
def exampleGraph2():
    ninja = turtle.Turtle()
    ninja.speed(30)
    ninja.pencolor("green")
    for i in range(180):
        ninja.forward(100)
        ninja.right(70)
        ninja.forward(60)
        ninja.left(80)
        ninja.forward(50)
        ninja.right(30)
        ninja.penup()
        ninja.setposition(0, 0)
        ninja.pendown()
        ninja.right(2)
    turtle.done()
    
    
    
def main():
  #Multiprocessing
  workerProcess1 = multiprocessing.Process(target=exampleGraph)
  workerProcess2 = multiprocessing.Process(target=exampleGraph2)
  
  #startWorkers
  workerProcess1.start()
  workerProcess2.start()
  
  #Join workers this will block parent main process
  #until the workes are complete
  workerProcess1.join()
  workerProcess2.join()


if __name__ == '__main__':
    main()
