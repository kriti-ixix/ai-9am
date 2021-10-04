try:
    length = float(input("Enter length: "))
    breadth = float(input("Enter breadth: "))

    if length < 0:
        raise ValueError
    elif breadth < 0:
        raise TypeError

    area = length * breadth
    print(area)

except ValueError:
    print("Length and breadth cannot be negative")

except:
    print("Error")