# threads:
import threading
import time


# istantiations:
# tuple ()
# list []
# dictionary {}


def longSquare(num, result):
    time.sleep(0.5)
    result[num] = num ** 2


result = {}

# [longSquare(n) for n in range(0, 5)]
# print([longSquare(n) for n in range(0, 5)])

# t1 = threading.Thread(target=longSquare, args=(1, result))  # target and args are the keyword arguments
# t2 = threading.Thread(target=longSquare, args=(2, result))

# t1.start()
# t2.start()

# t1.join()  # this join function checks if the thread is completed in execution yet
# t2.join()

# print(result)

threads = [threading.Thread(target=longSquare, args=(n, result)) for n in range(0,10)]
[t.start() for t in threads]
[t.join() for t in threads]
print(result)



