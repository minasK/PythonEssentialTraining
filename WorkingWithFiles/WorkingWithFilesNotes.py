f = open('10_01_file.txt', 'r')
print(f)  # it does not read the file but showing the object

# print(f.readlines())
# for line in f.readlines():
#     print(line)

# and they are double spaced and we fix this by doing this:
for line in f.readlines():
    print(line.strip())  # the .strip

# and now write:
f = open('10_01_output.txt', 'w')  # the file is not there yet but by running it we create it
f.write('line 1\n')
f.write('line 2\n')
f.close()  # and it is overwritting on that every time we run

# to avoid overwritting we append:
f = open('10_01_output.txt', 'a')  # a for append
f.write('line 3\n')
f.write('line 4\n')
f.close()

with open('10_01_output.txt', 'a') as f:
    f.write('some stuff\n')
    f.write('some other stuff\n')
print(f)


# csv and excel!!!!!!!!!!!!!!!!!!!!!!!!!!!!
import csv

with open('10_02_us.csv', 'r') as f:
    reader = csv.reader(f, delimiter='\t')  # before \t was there and we want to remove it
    next(reader)  # this is removing the header
    for row in reader:
        print(row)

# if we make this a list we can easily modify it, like:
with open('10_02_us.csv', 'r') as f:
    reader = list(csv.reader(f, delimiter='\t'))  # before \t was there and we want to remove it
    for row in reader[1:]:
        print(row)

with open('10_02_us.csv', 'r') as f:
    reader = csv.DictReader(f, delimiter='\t')
    for row in reader:
        print(row)  # and that to make it as dictionaries and we remove the [] making it list

# filtering data: (making it from reader object to a list object)!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!'''''''
with open('10_02_us.csv', 'r') as f:
    data = list(csv.DictReader(f, delimiter='\t'))

primes = []
for number in range(2, 9999):
    for factor in range(2, int(number ** 0.5)):
        if number % factor == 0:
            break
    else:
        primes.append(number)
data = [row for row in data if int(row['postal code']) in primes and row['state code'] == 'MA']
# for every row having postal code in prime and state code that we print the length of the data
# for row in data:
#     print(row) !!!!!!!this is for printing every row in the data that have the postal code etc...
print(data)

# and now lets write!!!!!!!!!!!!
with open('10_02_ma_prime.csv', 'w',
          newline='') as f:  # the new line is used to terminate each unused line. this newline ensures that no additional line break are added
    writer = csv.writer(f)  # by default , (comma) is used
    for row in data:
        writer.writerow([row['place name'], row['county']])  # this way we are writing the filtered files



# json!!!!!!!!!!!!!!!!!!!!!!!!!!!
# loading JSON:
import json
from json import JSONDecodeError, JSONEncoder

jsonString = '{"a": "apple", "b": "bear", "c": "cat"}'  # this is a string in a json format
try:
    json.loads(jsonString)
except JSONDecodeError:
    print("could not parse JSON")
    print(jsonString)

# custom json decoders
class animal:
    def __init__(self, name):
        self.name = name

class animalEncoder(JSONEncoder):
    def default(self, o):  # o is the object that is being passed in animal class and needs to be decoded in JSON
        if type(o) == animal:
            return o.name
        return super().default(o)  # this is like else:..., super is the parent JSONEncoder class

# dumping json
pythonDict = {"a": animal('aadv'), "b": animal('bear'), "c": animal('cat')}
json.dumps(pythonDict, cls=animalEncoder)  # cls is essential, see what it does
print(json.dumps(pythonDict, cls=animalEncoder) )
