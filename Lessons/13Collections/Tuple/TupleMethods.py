# print(help(fruits))
# Tuple has only 2 methods: count(), index(). Because you cannot add or remove elements in tuples
fruits = ("Apple", "Orange", "Coconut", "Pineapple", "Apple")
print(fruits)
print(fruits.count("Apple"))
print(fruits.index("Apple"))
print(fruits.index("Apple", 2))

for fruit in fruits:
    print(fruit)
