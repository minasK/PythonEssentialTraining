# multiprocessing:
from multiprocess import Process
import time


def longSquare(num, result):
    time.sleep(0.5)
    result[num] = num ** 2


result = {}

p1 = Process(target=longSquare, args=(1, result))  # target and args are the keyword arguments
p2 = Process(target=longSquare, args=(2, result))

p1.start()
p2.start()

p1.join()  # this join function checks if the thread is completed in execution yet
p2.join()

print(result)