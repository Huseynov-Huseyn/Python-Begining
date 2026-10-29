# print(help(fruits))
# Set elements always generate randomly, that is why all these methods have random outputs
fruits = {"Apple", "Orange", "Coconut", "Pineapple"}
print(fruits)
fruits.add("Melon")
fruits.remove("Apple")
fruits.pop()
fruits.clear()
print(fruits)

fruits = {"Apple", "Orange", "Coconut", "Pineapple"}
fruits2 = {"Melon", "Watermelon", "Apple"}
# fruits+fruits2
fruits_all = fruits | fruits2
print(fruits_all)
# same value in fruits +fruits2
fruits_all2 = fruits & fruits2
print(fruits_all2)
# fruits-fruits2
fruits_all3 = fruits - fruits2
print(fruits_all3)
# different values in fruits_+fruits2
fruits_all4 = fruits ^ fruits2
print(fruits_all4)

names = ["Huseyn", "Vali", "Ali"]
users = set(names)
print(names)
print(users)

fruits_all5 = fruits.union(fruits2)
print(fruits_all5)
