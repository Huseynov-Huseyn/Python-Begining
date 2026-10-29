from collections import defaultdict, Counter

salaries = {"Huseyn": 2600,
            "Vali": 2000,
            "Farid": 2500}

# 1. Adding / changing: update()
# if the key doesn't exist, the update method creates the key-value pair.
# if the key exists, the update method updates its value
salaries.update({"Huseyn": 2500})
salaries.update({"Ali": 500})

# 2. setdefault()
# setdefault(): if the key exists, it returns the value.
# if the key doesn't exist, it creates the key-value pair and returns the value
# if only the key is given and it doesn't exist, the key is added with the value None
print(salaries.setdefault("Mirali"))
print(salaries.setdefault("Hasan", 600))
print(salaries)

# 3. setdefault() in practice: grouping
workers = [("Sales", "Əli"), ("Sales", "Vüsal"), ("Accountant", "Leyla")]

sections = {}
for section, name in workers:
    sections.setdefault(section, []).append(name)

print(sections)

# easier version:
sections = defaultdict(list)
for section, name in workers:
    sections[section].append(name)

print(dict(sections))

# for section, name in workers:
#     if section not in sections:
#         sections[section] = []
#     sections[section].append(ad)

# 4. Removing: pop() and popitem()
salaries.pop("Huseyn")
salaries.popitem()
print(salaries)

# 5. Viewing: keys(), values(), items()
keys = salaries.keys()
print(keys)
for key in keys:
    print(key, end=" ")
print()
print("=====")

values = salaries.values()
for value in salaries.values():
    print(value, end=" ")
print()
print("=====")

print(salaries.items())
for key, value in salaries.items():
    print(f"{key}: {value}")

# 6. Merging two dictionaries
stok = {"Apple": 100, "Pineapple": 80}
stok2 = {"Melon": 200, "Watermelon": 300}
# combined_stock = stok | stok2
# print(combined_stock)
stok.update(stok2)
print(stok)

print(Counter("Huseynov Huseyn"))
