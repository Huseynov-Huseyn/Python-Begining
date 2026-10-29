# ===================== LEVEL: MEDIUM =====================
# TASK 4: Word Counter (dictionary as a counter)
#
# What to do:
#   1. Ask the user to enter a sentence (input).
#   2. Convert it to the lowercase and split it into words (.split()).
#   3. Count how many times each word appears using a dictionary
#      (do NOT use collections.Counter, do it manually).
#   4. Print every word and its count.
#   5. Print the most frequent word.
#
# Example:
#   Input:  "the cat and the dog and the bird"
#   Output:
#       the: 3
#       cat: 1
#       and: 2
#       dog: 1
#       bird: 1
#   Most frequent word: the (3 times)
#
# Concepts: dict, .get(word, 0) + 1, for loop, max() with key=

# Write your code below:

sentence = input("Please enter a sentence: ").lower()
words = sentence.split()
wordsCount = dict()
for word in words:
    wordsCount[word] = wordsCount.get(word, 0) + 1

for key, value in wordsCount.items():
    print(f"{key}: {value}")

frequentWord = max(wordsCount, key=wordsCount.get)
print(f"Most frequent word: {frequentWord} ({wordsCount.get(frequentWord)} times)")
