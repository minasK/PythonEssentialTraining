import os
# this project is causing the file compression and makes it smaller in size and shows it
import json

# Encodes as a list of (char, count) tuples
def encodeString(stringVal):
    encodedList = []
    prevChar = None
    count = 0
    for char in stringVal:
        if prevChar != char and prevChar is not None:
            encodedList.append((prevChar, count))
            count = 0
        prevChar = char
        count = count + 1
    encodedList.append((prevChar, count))
    return encodedList

def decodeString(encodedList):
    decodedStr = ''
    for item in encodedList:
        try:
            decodedStr = decodedStr + item[0] * item[1]
        except:
            print(item)
    return decodedStr


def encodeFile(filename, newFilename):
    with open(filename) as f:
        data = encodeString(f.read())

    with open(newFilename, 'w') as f:
        f.write(json.dumps(data))


def decodeFile(filename):
    with open(filename) as f:
        data = f.read()
    return decodeString(json.loads(data))



print(f'Original file size: {os.path.getsize("10_04_challenge_art.txt")}')
encodeFile('10_04_challenge_art.txt', '10_04_challenge_art_encoded.txt')
print(f'New file size: {os.path.getsize("10_04_challenge_art_encoded.txt")}')
print(decodeFile('10_04_challenge_art_encoded.txt'))





