# running a function in another thread
from time import sleep,ctime
from threading import Thread

# a custom function that block for a moment
def task(sleep_time,message):
    #block for a moment 
    sleep(1)
    #display a massage
    print(f'{ctime()} {message}')

#create a thread
thread = Thread(target =task,args=(1.5, 'New massage from another thread'))
#run the thread
thread.start()
# wait for the htread to finish

print(f'{ctime()}Waiting for the thread...')
thread.join()