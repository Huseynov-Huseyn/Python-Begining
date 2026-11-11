column = int(input("Column: "))
for i in range(column):
    for empty in range(column - 1 - i):
        print(" ", end="")
    for filled in range(i * 2 + 1):
        print("*", end="")
    print()
for i in reversed(range(column - 1)):
    for empty in range(column - 1 - i):
        print(" ", end="")
    for filled in range(i * 2 + 1):
        print("*", end="")
    print()


column = int(input("Column: "))
for i in range(column):
    print(" " * (column - 1 - i) + "*" * (i * 2 + 1))
for i in reversed(range(column - 1)):
    print(" " * (column - 1 - i) + "*" * (i * 2 + 1))