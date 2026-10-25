# Nested Loop = A loop within another loop (outer, inner)

for x in range(3):
    for y in range(1, 10):
        print(y, end="")
    print()

rows = int(input("Please enter row of rectangle: "))
columns = int(input("Please enter columns of rectangle: "))
symbol = input("Please enter symbol to use: ")
for row in range(rows):
    for column in range(columns):
        print(symbol, end="")
    print()
