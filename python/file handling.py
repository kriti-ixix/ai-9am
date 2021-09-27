vacationPlaces = ['London', 'Los Angeles', 'Paris', 'Rome', 'New York']

myFile = open('Vacation.txt', 'w') #Write mode

for city in vacationPlaces:
    myFile.write(city + '\n')

myFile.close()


myFile = open('Vacation.txt', 'a') #Append mode
myFile.write('Tokyo')
myFile.close()


myFile = open('Vacation.txt', 'r') #Read mode
fileContent = myFile.read()
print(fileContent)