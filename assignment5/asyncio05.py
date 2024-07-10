import asyncio
from random import random

async def make_rice():
    value = random() * 2
    print(f'Microwave (rice) : Cooking {value} seconds')
    await asyncio.sleep(value)
    return f'Microwave (rice)', value

async def make_noodle():
    value = random() * 2
    print(f'Microwave (noodle) : Cooking {value} seconds')
    await asyncio.sleep(value)
    return f'Microwave (noodle)', value

async def make_curry():
    value = random() * 2
    print(f'Microwave (curry) : Cooking {value} seconds')
    await asyncio.sleep(value)
    return f'Microwave (curry)', value

async def main():
    tasks = [
        asyncio.create_task(make_rice()),
        asyncio.create_task(make_noodle()),
        asyncio.create_task(make_curry())
    ]

    done, pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)

   

    # Determine the first completed task
    first_completed = done.pop()
    food, time = first_completed.result()

    print(f'\nFirst completed task: {food} is completed')

    
    print(f'\nCompleted tasks: {len(done) +1}')
    print(f'- {food} is completed time {time}')

    # Print uncompleted tasks
    print(f'\nUncompleted: {len(pending)}')
    

asyncio.run(main())

