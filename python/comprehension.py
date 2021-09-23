inputList = [1, 2, 3, 4, 5]

'''
outputList = []

for item in inputList:
    outputList.append(item ** 2)

for item in inputList:
    if item % 2 == 0:
        outputList.append(item ** 2)
'''

outputList = [item ** 2 for item in inputList if item % 2 == 0]
print(outputList)

outputDict = {item:item**2 for item in inputList}
print(outputDict)