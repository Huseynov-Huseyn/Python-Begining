from Book import Book

b1 = Book("Brave New World", "Aldous Huxley", 243)
b2 = Book("Brave New World", "Aldous Huxley", 243)
b3 = Book("Harry Potter 1", "J.K.Rowling", 232)

print(b1)
print(b1 < b3)
print(b1 > b3)
print(b1 + b2)
print("Potter" in b1)
print("Potter" in b3)
print(b3["title"])
# repr using for developer information
print(repr(b2))
# str using for user information
print(str(b2))
