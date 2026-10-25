setir = int(input("Setir: "))
for i in range(setir):
    for empty in range(setir - i - 1):
        print(" ", end="")
    for f in range(i * 2 + 1):
        print("*", end="")
    print()

# 2 / 1 / 2
# 1 / 3 / 1
# 0 / 5 / 0
