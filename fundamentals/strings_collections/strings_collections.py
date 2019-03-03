print("------- string (str) -------")
# strings in python are immutable sequence of unicode code points

# This is a multi line string without using \n
multiLine = """This string
spans over
multiple lines"""
print(multiLine)

# raw strings (escape sign is ignored) are prefixed by 'r'
# what you see is what you get
path = r"C:\User\name\Desktop"
print(path)

# Accessing char at a given position in a string
print("'abcd'[0]: ", 'abcd'[0])

print("------- byte -------")
# bytes in python are immutable sequence of bytes
# byte literals are prefixed by letter b
sampleBytes = b"I'm byte"
print(sampleBytes)

print("------- list -------")
sampleList = ['apple', 66]
print("sampleList = ['apple', 66]", sampleList)
sampleList.append('banana')
print("sampleList.append('banana'): ", sampleList)

print("------- dict (maps) -------")
# mutable maps of key-value pairs
sampleDict = {'key': 'value', 'Mary': '14', 'John': '13', 'Billy': '19'}
# Accessing values of the dict
print("Mary's age:", sampleDict.get("Mary"))
print("Billy's age:", sampleDict["Billy"])
# Updating values of the dict
sampleDict["key"] = "newVal"
print("Key's updated value:", sampleDict["key"])
