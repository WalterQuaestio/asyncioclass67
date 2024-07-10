# extending the Thread class and return values
<<<<<<< HEAD
=======
# extending the Thread class and return values
>>>>>>> 75d0705d5d8523cc369aa85ede9b4deb8668db5a
from time import sleep, ctime
from threading import Thread

class CustomThread(Thread):
    def run(self):
        #block for a moment
        sleep(1)
        #display a message
        print(f'{ctime()}This is coming from another thread')
        # store return value
        self.value = 99

#create the thread
thread= CustomThread()
# start the thread
thread.start()
# wait for the tread to finish
print(f'{ctime()}Waiting for the thread to finish')
thread.join()
#get the value retruned