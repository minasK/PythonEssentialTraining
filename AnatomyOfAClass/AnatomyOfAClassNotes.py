# first part:
class Dog:
    legs = 4

    def __init__(self, name):  # init is a constructor method.  self and name are its parameters
        self.name = name  # name and legs are the instance attributes

    def getLegs(self):
        return self.legs

    def speak(self):
        print(self.name + ' says: Bark!')


# self ensures that the method can operate on the specific instance it is called on
myDog = Dog('Rover')
print(myDog.name, myDog.legs)

# I could not access the Dog.legs b4 putting legs=4 before def init
print(Dog.legs)


# second part:
class wordSet:
    def __init__(self):
        self.words = set()  # empty set

    def addText(self, text):
        text = self.cleanText(text)
        for word in text.split():  # split function is splitting a string on a space and transforms that into a list
            self.words.add(word)

    def cleanText(self, text):  # those are called chaining functions
        text = text.replace('!', "").replace('.', '').replace(',', '').replace('/',
                                                                               '')  # the replace is replacing something with something else. eg, replaces ! with empty string
        return text.lower()


wordSet = wordSet()
# we do not actually need self but if we remove we get error, because we need 2 parameters and not one
wordSet.addText('hi, my name is Minas!. Hi')
print(wordSet.words)


# third part: (a class can extend another class and the original class is called the parent class when the child class is the other one extented)
class chihuahua(Dog):
    def speak(self):
        print(
            f'{self.name} says: yaa')  # that means that Dog class is overwritten if chihuahua class is taking the place


dog = chihuahua('Roxy')
dog.speak()
# !!!!!!!!!!!
myD = Dog('Rov')
myD.speak()

# extending built-in classes:
myList = list()


class UniqueList(list):

    def __init__(self):
        super().__init__() #this is making sure that the parent constructor is getting called first and then add the someproperty
        self.someProperty = 'unique list'
    def append(self, item):
        if item in self:
            return # return is essential and super must be in the same row as if!!!
        super().append(item)  # we want to append in the parent class, so we use super


uniqueList = UniqueList()
uniqueList.append(1)
uniqueList.append(1)
uniqueList.append(2)

print(uniqueList.someProperty)
