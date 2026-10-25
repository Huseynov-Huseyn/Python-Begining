rows = int(input("Please enter row of rectangle: "))
columns = int(input("Please enter column of rectangle: "))
for row in range(rows):
    for column in range(columns):
        if row == rows - 1 or row == 0 or column == (columns - 1) or column == 0:
            print("*", end="")
        else:
            print(" ", end="")
    print()
