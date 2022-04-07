# Author: Burak Dogancay
import asyncio


import asyncio
from concurrent.futures import ThreadPoolExecutor

async def funCor1():
    print("Corroutine1 Started")
    for i in range(5):
        await asyncio.sleep(2)
        print("Corroutine 1:" , i)
        
async def funCor2():
    print("Corroutine2 Started")
    for i in range(5):
        await asyncio.sleep(2)
        print("Corroutine 2:" , i)
        
def simpleFunction(x,y):
    for a in range(20):
        print(x+y)
    
#Call functions asynchronously with asyncio
def callFunctionAsync():
    loop = asyncio.get_event_loop()
    cors = asyncio.wait([funCor1(), funCor2()])
    loop.run_until_complete(cors)
    
#Asyncronous Executors
async def executeFunct(loop):
    executor = ThreadPoolExecutor()
    result = await loop.run_in_executor(executor, simpleFunction, "Hello,", " world!")
    print(result)

    
def main():
   #callFunctionAsync()
   
   #run function with concurrency
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(executeFunct(loop))
   #----------------------------
    

if __name__ == '__main__':
    main()