# Author: Burak Dogancay

from queue import Queue
from sympy import Q
from collections import deque


def queueExample():
    #The Queue module implements multi-producer, multi-consumer queues. It is especially useful in threaded
    #programming when information must be exchanged safely between multiple threads. There are three types of
    #queues provides by queue module,Which are as following : 1. Queue 2. LifoQueue 3. PriorityQueue
    question_queue=Queue()
    
    for x in range(1,3):
        tempDict  = ('uav',x)
        question_queue.put(tempDict)
    
    print("--QUEUE VARIABLES--")
    while(not question_queue.empty()):
        item = question_queue.get()
        print("Items are : ",item)
    print("---------------------")    
    
def dequeBasicExample():
    d = deque([1, 2, 3])
    p = d.popleft() # p = 1, d = deque([2, 3])
    d.appendleft(5) # d = deque([5, 2, 3])
    print("--DEQUE TYPES--")
    print(d)
    print("---------------------")   

def limitDeque():
    dVar = deque(maxlen=3) # only holds 3 items
    dVar.append(1) # deque([1])
    dVar.append(2) # deque([1, 2])
    dVar.append(3) # deque([1, 2, 3])
    dVar.append(4) # deque([2, 3, 4]) (1 is removed because its maxlen is 3)
    print("--DEQUE TYPES--")
    print(dVar)
    print("---------------------")  

def dequeMethodes():
    dl = deque() # deque([]) creating empty deque
    dl = deque([1, 2, 3, 4]) # deque([1, 2, 3, 4]) , Creating deque with some elements
    dl.append(5) # deque([1, 2, 3, 4, 5]) , Adding element to deque
    dl.appendleft(0) # deque([0, 1, 2, 3, 4, 5]) ,  Adding element left side of deque
    dl.extend([6, 7]) # deque([0, 1, 2, 3, 4, 5, 6, 7]) , Adding list of elements to deque
    dl.extendleft([-2, -1]) # deque([-1, -2, 0, 1, 2, 3, 4, 5, 6, 7]) , Adding list of elements to from the left side
    dl.pop() # 7 => deque([-1, -2, 0, 1, 2, 3, 4, 5, 6]) , Using .pop() element will naturally remove an item from the right side
    dl.popleft() # -1 deque([-2, 0, 1, 2, 3, 4, 5, 6]) , Using .popleft() element to remove an item from the left side
    dl.remove(1) # deque([-2, 0, 2, 3, 4, 5, 6]) , Remove element by its value
    dl.reverse() # deque([6, 5, 4, 3, 2, 0, -2]) , Reverse the order of the elements in deque
    
def main():
    queueExample()
    dequeBasicExample()
    limitDeque()
    dequeMethodes()
    

if __name__ == '__main__':
    main()