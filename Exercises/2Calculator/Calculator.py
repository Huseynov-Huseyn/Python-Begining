operator = input("Select the operation (+ - / *): ")
num1 = float(input("Please enter your first number: "))
num2 = float(input("Please enter your second number: "))

if operator == "+":
    result = round(num1 + num2, 3)
    print(result)
elif operator == "-":
    result = round(num1 - num2, 3)
    print(result)
elif operator == "/":
    result = round(num1 / num2, 3)
    print(result)
elif operator == "*":
    result = round(num1 * num2, 3)
    print(result)
else:
    print("Wrong operator input")
