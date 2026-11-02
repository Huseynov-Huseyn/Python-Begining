# Iterables = an object/collection that can return its elements one at a time
# allowing it to be iterated over in a loop

for character in "ML":
    print(character)

# TypeError
# for character in 5

# after using too much next(it). loop end and make StopIteration error
numbers = ["10", "20", "30"]
it = iter(numbers)
print(next(it))
print(next(it))

# for loop work principle:
it = iter(numbers)
while True:
    try:
        x = next(it)
    except StopIteration:
        break
    print(x)

it = iter([1, 2, 3])
print(list(it))
print(list(it))

# epoch loop
# data[start:end]
data = list(range(10))
batch_size = 4
for start in range(0, len(data), batch_size):
    print(data[start:start + batch_size])

# enumerate
batches = list(range(10))
for step, batch in enumerate(batches):
    if step % 100 == 0:
        print(f"step {step}: loss = ...")

# zip
features = [[1, 2], [3, 4], [5, 6]]
labels = [0, 1, 0]
print(list(zip(features, labels)))
# [([1, 2], 0), ([3, 4], 1), ([5, 6], 0)]
