rows = 5
spaces = rows - 1
stars = 1

# Outer loop to control the rows
for row in range(1, rows+1):

    # Inner loop for spaces
    for space in range(1, spaces+1):
        print(" ", end="")

    # Inner loop for stars
    for star in range(1, stars+1):
        print("*", end="")

    stars += 2
    spaces -= 1

    print()