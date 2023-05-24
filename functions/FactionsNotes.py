import math


def performOperation(num1, num2, operation):
    if operation == 'sum':
        print(num1 + num2)
        return num1 + num2
    if operation == 'multiply':
        print(num1 * num2)
        return num1 * num2


performOperation(2, 3, 'sum')
performOperation(2, 4, 'multiply')


# if we do not want the operation to have to name it every time we put a default
def performOperation(num1, num2, operation='sum'):
    if operation == 'sum':
        print(num1 + num2)
        return num1 + num2
    if operation == 'multiply':
        print(num1 * num2)
        return num1 * num2


performOperation(2, 3)


# if we put more than one args like 3,4 we get error because it is expecting 1
def kk(args):
    print(args)


kk(3)


# but... (asterisk is a pointer that tells python that variable name is not literally args, but a reference
def kk(*args):  # !!!!!!!!!!!!!!!!!
    print(args)


kk(3, 5, 'fff')


# also:
def k(*args, **kwargs):  # !!!!!!!!!!!!!!!!!
    print(args)
    print(kwargs)


k(3, 5, 'fff', oper='sum')


# that means that with the single asterisk it lets a tuple but ** means let you a dictionary

# some math:
def perform(*args, operation='sum'):
    if operation == 'sum':
        print(sum(args))
        return sum(args)
    if operation == 'multiply':
        print(math.prod(args))
        return math.prod(args)


perform(2, 4, 6, 7, 2, operation='multiply')


# if we do not write something in operation, we have the default sum, so it will sum them

# locals and globals variables!!!
def perfor(num1, num2, operation='sum'):
    print(locals())  # it prints what we write as a dictionary


#     those locals are only visible inside the function and not outside


perfor(1, 2, operation='multiply')

# all the globals I did not know
print(globals())


# scope is the kind of access of variables in a particular line of code (local or global)
def function1(varA, varB):
    print(locals())


def function2(varC, varB):
    print(locals())

function1(1,2)
function2(3,4)

# lamda!!!
(lambda x: x+3)(5)
print((lambda x: x+3)(5))

# sorts the values
myList = [5, 4, 3, 2]
print(sorted(myList))

# but:
# myL = ({'num': 3}, {'num': 2}, {'num': 1})
# print(sorted(myL))
# it cant do it, but:...


myL = ({'num': 3}, {'num': 2}, {'num': 1})
print(sorted(myL, key=lambda x: x['num']))
# he lamda is a way to write mini functions as values
