try:
    myList = [1, 2, 3, 4, 5]
    print(myList[0])
    #print(myList[10])

except IndexError:
    print("Index does not exist")

except KeyError:
    print("Key does not exist")

except:
    print("Error")

finally:
    print("End of program")