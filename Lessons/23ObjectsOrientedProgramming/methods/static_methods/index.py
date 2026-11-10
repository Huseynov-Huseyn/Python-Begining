from Employee import Employee

if Employee.is_valid_position("Manager"):
    employee1 = Employee("Huseyn", "Manager")
else:
    print("Position is not valid")

print(Employee.is_valid_position("Manager"))
print(Employee.is_valid_position("Engineer"))
