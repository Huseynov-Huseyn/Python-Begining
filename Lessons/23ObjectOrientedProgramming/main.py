from Car import Car

car1 = Car("Hundai", 2013, "Red", True)
car2 = Car("Mustang", 2023, "Blue", False)
print(car1.model)
print(car1.for_sale)
print(car2.model)
print(car2.for_sale)

car1.drive()
car2.stop()
car2.describe()
