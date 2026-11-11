# membership operators = used to test whether a value is found in a sequence:1. in 2. not in
# return boolean

fruit = "Apple"
if "A" in fruit:
    print("A is in fruit")
else:
    print("A is not in fruit")

if "a" not in fruit:
    print("a is in fruit")
else:
    print("a is not in fruit")

grades = {"Huseyn": 100,
          "Ali": 40,
          "Musa": 70}
student = "Musa"
if student in grades:
    print(f"{student} grade is : {grades[student]}")
else:
    print(f"{student} was not found ")

email = "huseynhuseyn343@gmail.com"
if "@" in email and "." in email:
    print("Valid email")
