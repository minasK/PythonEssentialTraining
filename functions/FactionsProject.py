# this is a project where random is in charge.

import random
import time

servicesAreUp = True


def getData50():
    if servicesAreUp and random.random() < 0.5:
        return 'You got the data! That only happens 50% of the time!'


def getData25():
    if servicesAreUp and random.random() < 0.25:
        return 'You got the data! That only happens 25% of the time!'


def getData10():
    if servicesAreUp and random.random() < 0.1:
        return 'You got the data! That only happens 10% of the time!'


# code here!
def getWithRetry(dataFunc):
    numberOfTries = 5
    for _ in range(1, numberOfTries): #we dont need anything to put in _
        response = dataFunc
        if response:
            return response


# Should return 'You got the data! That only happens 50% of the time!'
print(getWithRetry(getData50()))
# Should return 'You got the data! That only happens 25% of the time!'
print(getWithRetry(getData25()))
# Should return 'You got the data! That only happens 10% of the time!'
print(getWithRetry(getData10()))

# here services are false
servicesAreUp = False
# Returns None
getWithRetry(getData50)
# Returns None
getWithRetry(getData25)
# Returns None
getWithRetry(getData10)


def getData50():
    time.sleep(.1)
    if servicesAreUp and random.random() < 0.5:
        return 'You got the data! That only happens 50% of the time!'


def getData25():
    time.sleep(.1)
    if servicesAreUp and random.random() < 0.25:
        return 'You got the data! That only happens 25% of the time!'


def getData10():
    time.sleep(.1)
    if servicesAreUp and random.random() < 0.1:
        return 'You got the data! That only happens 10% of the time!'


# Returns None
print(getWithRetry(getData50()))
print(getWithRetry(getData25()))
print(getWithRetry(getData10()))


