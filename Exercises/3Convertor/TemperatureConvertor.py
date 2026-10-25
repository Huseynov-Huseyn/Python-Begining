unit = input("Celsius or Fahrenheit? (C or F): ")
temp = float(input("Please enter temperature: "))
if unit == "C":
    temp = round((temp * 1.8) + 32, 1)
    unit = "Fahrenheit."
    print(f"Temperature is {temp} {unit}")
elif unit == "F":
    temp = round((temp - 32) / 1.8, 1)
    unit = "Celsius."
    print(f"Temperature is {temp} {unit}")
else:
    print(f"{unit} is an invalid unit of measurement!")
