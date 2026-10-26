foods = []
prices = []
total = 0

while True:
    food = input("Enter a food to buy(q to quit): ")
    if food.lower() == "q":
        break
    price = float(input("Enter a price of the food: "))
    foods.append(food)
    prices.append(price)

total = sum(prices)
print("Your shopping card:")
for i in range(1, (len(foods) + 1)):
    print(f"{i}. {foods[i - 1]} - {prices[i - 1]}$")
print(f"Bill: {total}$")
