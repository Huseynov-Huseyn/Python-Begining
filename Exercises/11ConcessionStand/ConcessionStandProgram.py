menu = {"pizza": 9.99,
        "popcorn": 6.99,
        "cola": 1.99,
        "hotdog": 3.99}

cart = []
total = 0

print("========== Menu ==========")
for key, value in menu.items():
    print(f"{key:.<20} {value:.2f}$")
print("==========================")

while True:
    selection = input("Which item do you want to buy (q for quit): ").lower()
    if selection == "q":
        break
    elif menu.get(selection) is not None:
        total += menu.get(selection)
        cart.append(selection)
    else:
        print("This food is not on the Menu!")

print("========== Your cart ==========")
for item in cart:
    print(item, end=" ")
print()
print(f"Total price is: {total:.2f}$")
