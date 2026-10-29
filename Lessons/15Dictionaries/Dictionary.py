# Dictionary = a collection of {key:value} pairs
#              ordered and changeable. no duplicates
# searching by key is fast. key must be unique and hashable
# list, set and dict cannot be keys. a tuple containing a list also cannot be a key
# value can be anything

# 1. Creating a dictionary
salaries = {"Huseyn": 2600,
            "Vali": 2000,
            "Farid": 2500}

# print(dir(salaries))
# print(help(salaries))

# 2. Which types can be a key
# {"a": 1}             str key: OK
# {(1, 2): "empty"}    tuple key: OK
# {[1, 2]: "x"}        TypeError: unhashable type: 'list'   ← list CANNOT

# 3. Getting a value with get()
print(salaries.get("Huseyn"))
# print(salaries.get("Hesen"))
if salaries.get("Hesen"):
    print("This person exists")
else:
    print("This person doesn't exist")

# 4. Checking with "in" (checks keys by default)
stok = {"Apple": 100, "Pineapple": 80}
print("Apple" in stok)
print(100 in stok)
print(100 in stok.values())

# 5. Creating a dictionary from two lists with zip()
keys = ["USA", "Canada", "Turkiye"]
values = ["Washington DC", "Ottawa", "Ankara"]
d = dict(zip(keys, values))
print(d)