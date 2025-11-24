# Dictionaries are used to store data values in key:value pairs.
# A dictionary is a collection which is ordered*, changeable and do not allow duplicates
# Duplicate values will overwrite existing values

thisDict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
    "year": 2024
}

print(thisDict)
print(thisDict["brand"])
print(len(thisDict))
print(type(thisDict))

anotherDict = dict(name = "Dictionary", type="Dict")
print(anotherDict)

x = thisDict.get("model")
print(x)

kees = thisDict.keys()
print(kees)

thisDict["new"] = "new"

print(thisDict.values())
print(thisDict.items())