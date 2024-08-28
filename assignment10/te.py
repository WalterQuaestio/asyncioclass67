from random import random
import asyncio
import time

# Coroutine to generate work
async def producer(queue):
    print('Producer: Running')
    # Generate work
    for i in range(10):
        # Generate a value
        value = i
        # Block to simulate work
        sleeptime = random()
        print(f"> Producer {value} sleep {sleeptime:.2f}")
        await asyncio.sleep(sleeptime)
        # Add to the queue
        print(f"> Producer put {value}")
        await queue.put(value)
    # Send an all done signal
    await queue.put(None)
    print('Producer: Done')

# Coroutine to consume work
async def consumer(queue):
    print('Consumer: Running')
    # Start time
    start_time = time.monotonic()

    # Consume work
    while True:
        # Get a unit of work
        item = await queue.get()
        # Check for stop
        if item is None:
            # Break the loop on termination signal
            break
        # Report
        print(f'\t> Consumer got {item}')

    # End time
    end_time = time.monotonic()
    # Calculate the use time
    use_time = end_time - start_time
    print(f'Consumer: Done in {use_time:.2f} seconds')
    
    return use_time

# Entry point coroutine
async def main():
    # Create the shared queue
    queue = asyncio.Queue()
    # Run the producer and consumer
    await asyncio.gather(producer(queue), consumer(queue))

# Start the asyncio program
asyncio.run(main())
