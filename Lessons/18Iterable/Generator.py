# Difference between return and yield
# return - creating all in one and return all in one
# yield - iteration.giving 1 and waiting. making pause
import sys


def normal_func():
    return [1, 2, 3]


def gen_func():
    yield 1
    yield 2
    yield 3


g = gen_func()
print(g)
print(next(g))
print(next(g))
print(next(g))


def countdown(n):
    while n > 0:
        yield n
        n -= 1


for x in countdown(3):
    print(x)

lst = [x for x in range(1_000_000)]  # list comprehension
gen = (x for x in range(1_000_000))  # generator expression
print(sys.getsizeof(lst))  # around 8 000 000 bite (~8 MB)
print(sys.getsizeof(gen))  # around 100-200 bite (not being dependent on element)

# Generator expression
total = sum(x ** 2 for x in range(1000000))
print(total)


# infinite generator
def infinite_ids():
    n = 0
    while True:
        yield n
        n += 1


ids = infinite_ids()
print(next(ids), next(ids), next(ids))  # 0 1 2


# pipeline = connecting generators like a chain
def read_lines(path):
    with open(path, encoding="utf-8") as f:
        for line in f:  # fayl özü də lazy iterable-dır
            yield line.strip()


def non_empty(lines):
    for line in lines:
        if line:
            yield line


def to_lower(lines):
    for line in lines:
        yield line.lower()


import random


def batch_generator(X, y, batch_size, shuffle=True):
    indices = list(range(len(X)))
    if shuffle:
        random.shuffle(indices)  # hər epoch-da sıra fərqli olsun
    for start in range(0, len(indices), batch_size):
        idx = indices[start:start + batch_size]
        yield [X[i] for i in idx], [y[i] for i in idx]


X = [[i, i * 2] for i in range(10)]
y = [i % 2 for i in range(10)]
for epoch in range(2):
    for xb, yb in batch_generator(X, y, batch_size=4):
        print(epoch, xb, yb)

g = (x for x in range(3))
print(list(g))
print(list(g))
