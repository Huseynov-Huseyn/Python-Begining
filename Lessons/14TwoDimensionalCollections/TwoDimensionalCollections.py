fruits = ["Apple", "Banana", "Orange"]
vegetables = ["Potato", "Carrot", "Tomato"]
meats = ["Chicken", "Fish", "Beef"]

groceries = [fruits, vegetables, meats]
print(groceries)
print(groceries[0])
print(groceries[0][1])
# for grocerie in groceries:
#     print(grocerie)
for collection in groceries:
    for meal in collection:
        print(meal, end=" ")
    print()

users = [["Huseynov Huseyn", "Farid Abaszada"],
         ["huseyn", "farid"]]
print(users)

# 2D collections can be different inner and outer collections
users = [{"Huseynov Huseyn", "Farid Abaszada"},
         {"huseyn", "farid"}]
users = ({"Huseynov Huseyn", "Farid Abaszada"},
         {"huseyn", "farid"})
