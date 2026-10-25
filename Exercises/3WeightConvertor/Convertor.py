weight = float(input("Please enter your weight : "))
unit = input("Kilograms or Pounds? (K or L) : ")
if unit == "K":
    weight = round(weight * 2.205, 3)
    unit = "Lbs."
    print(f"You are {weight} {unit}")
elif unit == "L":
    weight = round(weight / 2.205, 3)
    unit = "Kgs."
    print(f"You are {weight} {unit}")
else:
    print(f"{unit} was not valid")
