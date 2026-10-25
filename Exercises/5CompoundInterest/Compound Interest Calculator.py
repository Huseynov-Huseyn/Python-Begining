principalAmount = 0
rate = 0
repeat = 0
years = 0

while principalAmount <= 0:
    principalAmount = float(input("Please enter your amount of money: "))
    if principalAmount <= 0:
        print("Principal cannot be less than or equal to zero!")
while rate <= 0 or rate >= 1:
    rate = float(input("Please enter your rate with decimal between 0 and 1: "))
    if rate <= 0 or rate >= 1:
        print("Interest rate cannot be less than or equal to zero.Also cannot be more than or equal to 1")
while repeat <= 0:
    repeat = int(input("How many times interest per year: "))
    if repeat <= 0:
        print("Repeat cannot be less than or equal to zero!")
while years <= 0:
    years = int(input("How many years did this process go: "))
    if years <= 0:
        print("Years cannot be less than or equal to zero!")

totalAmount = principalAmount * (1 + (rate / repeat)) ** (repeat * years)
print(f"Your final total amount is: {totalAmount:.2f}$")
