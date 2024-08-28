# example of using an asyncio queue without blocking
from random import random
import asyncio
import time

# coroutine to generate work
async def producer(queue):
    print('Producer: Running')
    ProStart = time.perf_counter()
    # generate work
    for i in range(10):
        # generate a value
        value = i
        # block to simulate work
        sleeptime = random()
        print(f"> Producer {value} sleep {sleeptime}")
        await asyncio.sleep(sleeptime)
        # add to the queue
        print(f"> Producer put {value}")
        await queue.put(value)
    # send an all done signal
    await queue.put(None)
    print('Producer: Done')
    ProDone = time.perf_counter() - ProStart
    print(f"Producer work {ProDone} s")
 
# coroutine to consume work
async def consumer(queue):
    print('Consumer: Running')
    
    ConStart = time.perf_counter()
    
    # consume work
    while True:
        # get a unit of work without blocking
        try:
            item = queue.get_nowait()
        except asyncio.QueueEmpty:
            print('Consumer: got nothing, waiting a while...')
            
            
            
            await asyncio.sleep(0.5)
            continue
        # check for stop
        if item is None:
            break
        # report
        print(f'\t> Consumer got {item}')
    # all done
    print('Consumer: Done')
    
    ConDone = time.perf_counter() - ConStart
    print(f"Consumer work {ConDone} s")
    
    
    
 
# entry point coroutine
async def main():
    # create the shared queue
    queue = asyncio.Queue()
    # run the producer and consumers
    await asyncio.gather(producer(queue), consumer(queue))
    
 
# start the asyncio program
asyncio.run(main())