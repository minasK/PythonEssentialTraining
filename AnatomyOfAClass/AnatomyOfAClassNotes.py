class Dog:
    legs = 4
    def __init__(self, name):  # init is a constructor method.  self and name are its parameters
        self.name = name  # name and legs are the instance attributes
        self.legs = 4

    def speak(self):
        print(self.name + ' says: Bark!')
# self ensures that the method can operate on the specific instance it is called on
myDog = Dog('Rover')
print(myDog.name, myDog.legs)

# I could not access the Dog.legs b4 putting legs=4 before def init
print(Dog.legs)

# continue 1 48