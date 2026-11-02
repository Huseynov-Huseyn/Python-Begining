# List comprehension =compact and easier way to create a list
# [Expression for value in iterable if condition]

fruits = ["Apple", "Banana", "Orange"]
fruits = [fruit.lower() for fruit in fruits]
fruit_chars = [fruit[0] for fruit in fruits]
print(fruits)
print(fruit_chars)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
double = [x * 2 for x in numbers if x % 2 == 0]
print(double)
