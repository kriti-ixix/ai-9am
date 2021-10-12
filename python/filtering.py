l1 = list(range(1, 101))
print(l1)


def checkForEven(x):
    if x%2 == 0:
        return True
    else:
        return False


print(list(filter(checkForEven, l1)))
print(list(filter(lambda x : x %2 == 0, l1)))