# those def functions are showing the number of letters there are in the words
def encodeString(stringVal):
    encodedList = []
    prevChar = stringVal[0]
    count = 0
    for char in stringVal:
        if prevChar != char:
            encodedList.append((prevChar, count))
            count =0
        prevChar = char
        count = count + 1

    encodedList.append((prevChar, count))
    return encodedList
def decodeString(encodedList):
    decodeStr = ''
    for item in encodedList:
        decodeStr = decodeStr + item[0] * item[1]
    return decodeStr

print(encodeString("ASDAAAA okdeokd"))
print(decodeString(encodeString("ASDAAAA")))