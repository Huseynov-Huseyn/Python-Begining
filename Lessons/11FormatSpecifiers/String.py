number1 = 12.99
number2 = 16.99
number3 = 213.99
print(f"Number 1 is: {number1:.2f}$")
print(f"Number 2 is: {number2:.2f}$")
print(f"Number 3 is: {number3:.2f}$")

print("===========================")
print(f"Number 1 is: {number1:10}$")
print(f"Number 2 is: {number2:10}$")
print(f"Number 3 is: {number3:10}$")

print("===========================")
print(f"Number 1 is: {number1:010}$")
print(f"Number 2 is: {number2:010}$")
print(f"Number 3 is: {number3:010}$")

print("===========================")
print(f"Number 1 is: {number1:<10}$")
print(f"Number 2 is: {number2:>10}$")
# Centralize ^
print(f"Number 3 is: {number3:^10}$")

print("===========================")
number4 = -10.99
number5 = 10.99
print(f"Number 4 is:{number4:+}$")
print(f"Number 5 is:{number5:+}$")
print(f"Number 5 is:{number5: }$")

print("===========================")
number6 = 100000000000
print(f"Number 6 is:{number6:+,.2f}")
