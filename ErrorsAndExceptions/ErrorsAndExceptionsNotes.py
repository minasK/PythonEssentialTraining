import time


# first part:
def causeError():
    return 1 / 0


def callCauseError():
    return causeError


callCauseError()

# try/except
try:
    1 / 0
except Exception as e:
    print(type(e))  # so this is printing the type of error


# second part:
def CauseError():
    try:
        return 1 / 0
    except Exception as e:  # or else we just print there was an error
        print(e)
        return e


CauseError()


# finally:
def CaauseError():
    start = time.time()
    try:
        time.sleep(0.5)
        return 1 / 0
    except Exception as e:  # or else we just print there was an error
        print(e)
        return e
    finally:  # finally always executes no matter what the try block is, so there is no need for except statement
        print(f"this took {time.time() - start} seconds to execute")


CaauseError()


def Error():
    try:
        return 1 + 'a'
    except TypeError:  # depending on the error, it will print the right one
        print('type error')
    except Exception as e:
        print(e)
        return e
    # finally:  # finally always executes no matter what the try block is, so there is no need for except statement
    #     print(f"this took {time.time() - start} seconds to execute")


Error()


# custom Decorators: (like @staticmethod)
def handleException(func):  # the argument to be passed on is the func
    def wrapper():  # this is an inner function
        try:
            func()
        except TypeError:
            print('type error')
        except ZeroDivisionError:
            print("zero division error")
        except Exception:
            print("there was an error")

    return wrapper


@handleException  # our decorator that is a design pattern in Python that allows a user to add new functionality to
# an existing object without modifying its structure
def causeErr():
    return 1 / 0


causeErr()


# raising exceptions
@handleException
def raiseError():
    raise Exception()

raiseError()


# and now for the difficult part is this:
def handleException(func):  # the argument to be passed on is the func
    def wrapper(*args):  # this is an inner function
        try:
            func(*args)
        except TypeError:
            print('type error')
        except ZeroDivisionError:
            print("zero division error")
        except Exception:
            print("there was an error")

    return wrapper


@handleException
def raiseError(n):
    if n == 0:
        raise Exception()
    print(n)

raiseError(0)


# third part:
class CustomException(Exception): #it extends the Exception
    pass

def Errr():
    raise CustomException()

Errr()

# adding attributes to that:
class httpException(Exception):
    statusCode = None
    message = None
    def __init__(self):
        super().__init__(f'status code: {self.statusCode} and message is: {self.message} ')

class NotFound(httpException):
    statusCode = 404
    message = 'resource not found'

class ServerError(httpException):
    statusCode = 500
    message = 'server not available'

def RaiseServerError():
    raise ServerError()

RaiseServerError()
