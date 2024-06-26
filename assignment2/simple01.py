# Synchronous cooking
# 1 kitchen 1 chefs 1 dish
from time import sleep,ctime,time

# Cooking synchronous
def cooking(index):
    print(f'{ctime()} Kitchen-{index}    : Begin cooking...')
    sleep(2)
    print(f'{ctime()} Kitchen-{index} :basket')