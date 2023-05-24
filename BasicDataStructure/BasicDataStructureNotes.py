# list declaration:
myList = [1,2,3,4,5]
print(myList[3:])
print(myList[0:6:2])
print(myList[::2])

for i in range (100):
    print(i)

myList = list(range(100))
print(myList[::6])
print(myList[::-6])

myList = [1,2,3,4]
myList.append(6)
myList.insert(4, 'new value')
print(myList)
myList.remove('new value')
print(myList)
# pop removes the last one
myList.pop()
print(myList)

# while the len is not 0, pop and pop
while len(myList):
    print(myList.pop())

print(myList)

# a set is declared like that:
mySet = {"a", "b", "c", "b", "a"}
print(mySet)
print(mySet)

avoidDuplication = list(set(mySet))
print(mySet)
mySet.add('d')
print(mySet)

# difference between add and append is that add just adds and append puts it in the end
print(len(mySet))

# tuple:
myTuple = ('a', 'b', 'c')

def returnMultipleValues():
    return 1,2,3,4,5
print(type(returnMultipleValues()))
print(type(mySet))
# type represents the type of the function
# A list is a collection of ordered data. A tuple is an ordered collection of data. A set is an unordered collection

# Dictionaries
animals = {
    'a' : ['avard'],
    'b' : ['bear'],
    'c' : ['cat'],
}
print(animals)
print(animals['a'])
animals['d'] = 'dog'
print(animals)
# keys and values of the dictionary
print(animals.keys())
print(animals.values())
print(type(animals))

# an if
if 'c' not in animals:
    print("fine")

# 1-100
print(list(range(100)))

ml = list(range(100))
# this is giving us item and if item%10=0 then give item
filtml = [item for item in ml if item % 10 == 0]
print(filtml)

# split
string = 'my name is minas, hey'
print(string.split())
print(string.split(','))

#makes all letters lower case and dot in every word
def cleanWord(word):
    return word.replace('.', '').lower()

print([cleanWord(word) for word in string.split()])

# we can also do this that shows every animal in list:
animalList = [('a', 'aaa'), ('b', 'bear')]
animals = {item[0]: item[1] for item in animalList}
print(animals)

# instead of that we can also do: (that also goes for more than one values
animals = {key: value for key, value in animalList}
print(animals)

# that is to properly organize the way we want
print([{'letter': key, 'name': value} for key, value in animalList])
