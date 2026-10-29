# ===================== LEVEL: EASY =====================
# TASK 3: Unique Numbers (set and tuple)
#
# What to do:
#   1. Given the list: numbers = [1, 2, 2, 3, 4, 4, 4, 5, 1]
#   2. Convert it to a set to remove duplicates and print the result.
#   3. Print how many unique numbers there are.
#   4. Convert the unique numbers to a sorted list and then to a tuple. Print it.
#   5. Try to change the first element of the tuple. What happens? Write the
#      answer as a comment (hint: tuples are immutable).
#
# Expected output (example):
#   {1, 2, 3, 4, 5}
#   Unique count: 5
#   (1, 2, 3, 4, 5)
#
# Concepts: set, tuple, sorted(), immutability

# Write your code below:
numbers = [1, 2, 2, 3, 4, 4, 4, 5, 1]
numbersSet = set(numbers)
print(numbersSet)
print(f"Unique count: {len(numbersSet)}")
sortedNumbers = sorted(list(numbersSet))
numbersTuple = tuple(sortedNumbers)
print(numbersTuple)

# numbersTuple[0] = 2
# TypeError
