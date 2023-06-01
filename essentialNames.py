print(type(1.4455))
# we get the type here of the number and it is float
# variables are containers for storing data values

# data structures:
# List: is an array of values, (we can also have a list of lists, list[[1,2,4,8], False, True]
# set's ({}) elements all have to be unique (like set{1,2,2,1,4} will print out 3 elements and not 5 since it is taking out the unecessary ones)
# tuples: are like lists (but we cant append or add things in tuples). we use tuple for memory efficiency
# dictionaries: and sets are defined with curly brackets {} and both of them have unique values, order doesnt matter

# operators perform operations on variables and data

# control flow: (loops and if statements)
a = True
if a:  # this will be executed if a is true
    print('bla bla')

a = [1,2,3,4]
for item in a:
    print(item)

# in the class, the class instances such as def speak:, they are called objects (for example Dog object)
# And the variables inside these classes are called attributes of the objects (for ex. self.name=...)
# the functions are called methods (the class methods)
#  for example we say the Dog object has the method speak