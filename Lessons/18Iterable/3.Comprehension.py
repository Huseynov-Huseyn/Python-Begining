# Comprehension
numbers = list(range(15))
print([x ** 2 for x in numbers if x % 3 == 0])

new_number = []
for x in numbers:
    if x % 3 == 0:
        new_number.append(x ** 2)
print(new_number)

words = ["ai", "data", "ml", "data"]
length = [len(w) for w in words]
unique = {w for w in words}
w_len = {w: len(w) for w in words}

data = list(range(15))
# If at end= drop element or keep it
positives = [x for x in data if x > 0]
# if at begin keep every element, but change the value
relu = [x if x > 0 else 0 for x in data]

matrix = [[1, 2], [3, 4], [5, 6]]
flat = [x for row in matrix for x in row]

transposed = [[row[i] for row in matrix] for i in range(2)]

ages = [18, 21, 40, 60]
lo, hi = min(ages), max(ages)
normalized = [(a - lo) / (hi - lo) for a in ages]
print(normalized)
