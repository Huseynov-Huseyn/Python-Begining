name = input("Please enter your name: ")
while name == "":
    print("You didn't enter your name!")
    name = input("Please enter your name: ")
print(f"Hello {name}!")

age = int(input("Please enter your age: "))
while age <= 0:
    print("Enter a valid age!")
    age = int(input("Please enter your age: "))
print(f"Alright {name}, you are {age} years old.")

food = input("Enter a food you like (q to quit): ")
while not food == "q":
    print(f"You like {food}")
    food = input("Enter another food you like (q to quit): ")
print(f"Good bye {name}!")
