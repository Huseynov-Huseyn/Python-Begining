import random

# print(help(random))
# number = random.randint(1, 10)
low = 5
high = 20
number = random.randint(low, high)
# create an integer between 0 and 1
# random=random.random()
print(number)

options = ("rock", "paper", "scissors")
option = random.choice(options)
print(option)

cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
random.shuffle(cards)
print(cards)

# Reproducibility / Determinism
# with seed method, same value with random
# In this class specified as a Number 42 and always get the same result
# random.seed(42)

# Creating sub list of main list with quantity (no repetition)
data = [10, 20, 30, 40, 50, 60]
subset = random.sample(data, 3)
print(subset)

# randomization of weights
animals = ("Cat", "Dog", "Bird")
weight = (0.7, 0.2, 0.1)
print(random.choices(animals, weights=weight, k=5))

# random float between a and b
print(random.uniform(20, 30))

mu = 100
sigma = 50
# Gauss Function
print(random.gauss(mu, sigma))
