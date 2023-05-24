# if the number is divisible by 3 print ok, divisible by 5 print fine else print minas
from datetime import datetime
def Number(num):
    if num%3==0:
        print("ok")
    elif num%5==0:
        print("fine")
    else:
        print("minas")

print(Number(3))

for n in range(1,100):
    if n % 15 ==0:
        print('ok')
    elif n % 3 == 0:
        print('fine')
    else:
        print(n)

# a simple if in the same row
m = 7
print('fiz' if m % 3 == 0 else m)

# the while loop
print(datetime.now().second)
wait_until = datetime.now().second + 2

# in order to avoid doing uneeded computational power...
while datetime.now().second != wait_until:
    print("still waiting")
print(f'we are at {wait_until} seconds')

# we just press pass:
while datetime.now().second != wait_until:
    pass
print(f'we are at {wait_until} seconds')
# pass also works as placeholder (pass = line to be fixed after)


# SOS!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# while true!!! Break: breaks out of the current loop that is in it. Stops the while true and any other loop (if is not
# a loop!!! break only works for one loop)
while True:
    if datetime.now().second == wait_until:
        print(f'we are at {wait_until} seconds')
        break

# the way to end 2 while loops
while True:
    while datetime.now().second == wait_until:
        print(f'we are at {wait_until} seconds')
        break
    break

# and now continue!!!
while datetime.now().second == wait_until:
    continue
    print("continue")                      #this line will continue and will not be printed
# so it will exit the loop and print the other ones down
print(f'we are at {wait_until} seconds')
print(datetime.now())

# For loop
myList = [1,2,3,4,5]
for item in myList:
    print(item)

animalsLookup = {
    'a' : ['avard', 'antilope'],
    'b' : ['bear'],
    'c' : ['cat'],}

for letter, animals in animalsLookup.items():
    if len(animals) > 1:
        continue
    print(f'only one animal: {animals[0]}')

for letter, animals in animalsLookup.items():
    if len(animals) > 1:
        print(f'Found: {len(animals)} animals: {animals}')
        break

# finding primes from 2 to 100, for and else statement!!!
for number in range(2, 100):
    for factor in range(2, int(number ** 0.5) + 1):
        if number % factor == 0:
            break
    else:
        print(f'{number} is prime!')

# a more difficult way, but comprehensive to programmers:
for number in range(2, 100):
    found_factor = False
    for factor in range(2, int(number ** 0.5) + 1): # ** is for power, eg. 2**5 = 32
        if number % factor == 0:
            found_factor = True
    if not found_factor:
        print(f'{number} is prime!')




