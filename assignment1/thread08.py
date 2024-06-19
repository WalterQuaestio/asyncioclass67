# Race Conditions
import concurrent.futures
import logging
import time

class FakeDatebase:
    def __init__(self):
        self.value = 0
        
    def update(self, name):
        logging.info("Thread %s: starting update", name)
        local_copy = self.value
        local_copy += 1
        time.sleep(0.1)
        self.value = local_copy
        logging.info("Thrread %s: finishing update", name)
        
if __name__ == '__main__':
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")
    
    database = FakeDatebase()
    logging.info("Testing update. Starting value is %d.", database.value)
    with concurrent.futures.ThreadPoolExecutor(max_workers=2)as exeutor:
        for index in range(2):
            exeutor.submit(database.update, index)
    logging.info("Testing update. Ending value is %d", database.value)