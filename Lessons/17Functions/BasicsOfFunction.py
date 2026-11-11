# function is a block of reusable code.
# def functionName(parameter1, parameter2):
# return statement used to end a function and send a result back to the caller
# parameters order: positional -> default -> *args -> **kwargs

def song(name, age):  # name, age = parameter
    print("============")
    print(f"Hello World! It's {name} and i am {age} years old.")
    print("============")
    print()


for i in range(3):
    song("Huseyn", 21)  # "Huseyn", 21 = argument


def add(number1, number2):
    return number1 + number2


print(add(5, 10))


def create_username(name, surname):
    name = name.capitalize()
    surname = surname.capitalize()
    return name + " " + surname


print(create_username("huseyn", "huseynov"))
