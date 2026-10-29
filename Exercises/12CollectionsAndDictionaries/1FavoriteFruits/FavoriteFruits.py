# ===================== LEVEL: EASY =====================
# TASK 1: Favorite Fruits (list)
#
# What to do:
#   1. Create a list with 5 fruits: "apple", "banana", "orange", "grape", "kiwi".
#   2. Print the first fruit and the last fruit (use indexing).
#   3. Add "mango" to the end of the list (append).
#   4. Remove "banana" from the list (remove).
#   5. Sort the list alphabetically and print it.
#   6. Print how many fruits are in the list (len).
#
# Expected output (example):
#   First: apple | Last: kiwi
#   ['apple', 'grape', 'kiwi', 'mango', 'orange']
#   Total fruits: 5
#
# Concepts: list, indexing, append, remove, sort, len

# Write your code below:

fruits = ["apple", "banana", "orange", "grape", "kiwi"]
print(f"First: {fruits[0]} | Last: {fruits[- 1]}")
fruits.append("mango")
fruits.remove("banana")
fruits.sort()
print(fruits)
print(f"Total fruits: {len(fruits)}")
