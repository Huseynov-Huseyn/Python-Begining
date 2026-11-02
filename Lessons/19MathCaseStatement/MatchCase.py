# Math-case statement: an alternative to using many elif statements.
#                      Execute some code if a value matches a 'case'
#                      Benefits: cleaner and syntax is more readable.
# Syntax:
# match subject:
#     case pattern1:
#         # Code block if pattern1 matches
#     case pattern2:
#         # Code block if pattern2 matches
#     case _:
#         # Code block if no pattern matches
def check_number(number):
    match number:
        case 10:
            print("It's 10")
        case 20:
            print("It's 20")
        case _:
            print("It's neither 10 nor 20")


check_number(20)
check_number(15)
print("=========")


def check_character(character):
    match character:
        case "A":
            print("It's A")
        case "B":
            print("It's B")
        case _:
            print("It's neither A nor B")


check_character("A")
check_character("C")
print("=========")


def check_number2(number):
    match number:
        case 10 | 20 | 30:
            print(f"Matched {number}")
        case 40 | 50 | 60:
            print(f"Matched {number}")
        case _:
            print("No match found")


check_number2(20)
check_number2(60)
check_number2(80)
print("=========")


def num_check3(x):
    match x:
        case n if n > 0:
            print("Positive number")
        case n if n < 0:
            print("Negative number")
        case _:
            print("Zero")


num_check3(15)
num_check3(-8)
num_check3(0)
print("=========")


def process(data):
    match data:
        case [x, y]:
            print(f"Two elements: {x},{y}")
        case [x, y, z]:
            print(f"Three elements: {x},{y},{z}")
        case _:
            print("Unknown format")


process([10, 20])
process([10])
print("=========")


def personal_info(data):
    match data:
        case {"name": name, "age": age}:
            print(f"Name: {name}, Age: {age}")
        case {"name": name}:
            print(f"Name: {name}")
        case _:
            print("Unknown format")


personal_info({"name": "Emily", "age": 25})
personal_info({"name": "Harry"})
personal_info({"city": "New York"})
print("=========")
