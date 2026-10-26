# List = [] ordered and changeable. Duplicate OK

fruits = ["Apple", "Orange", "Coconut", "Pineapple"]
print(fruits)
print(dir(fruits))
print(help(fruits))
print(len(fruits))
# If string contains in the list. return true else false
print("Pineapple" in (fruits))

for fruit in fruits:
    print(fruit)

# Like String indexing
print(fruits[2])
print(fruits[0:2])
print(fruits[:2])
print(fruits[::-1])
print(fruits[::2])

fruits[0] = "Banana"

for i in range(len(fruits)):
    print(f"{i}-{fruits[i]}-{len(fruits[i])}")
