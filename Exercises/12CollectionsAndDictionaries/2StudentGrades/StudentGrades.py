# ===================== LEVEL: EASY =====================
# TASK 2: Student Grades (dictionary)
#
# What to do:
#   1. Create a dictionary: {"Ali": 85, "Leyla": 92, "Orxan": 70}
#   2. Print Leyla's grade (use the key).
#   3. Add a new student "Aysel" with grade 88.
#   4. Change Orxan's grade to 75.
#   5. Delete "Ali" from the dictionary.
#   6. Loop through the dictionary and print every student like this:
#         Leyla: 92
#
# Bonus: Use .get("Nigar", "Not found") to look for a student that does not exist.
#
# Concepts: dict, add/update/delete, for loop with .items(), .get()

# Write your code below:

grades = {"Ali": 85, "Leyla": 92, "Orxan": 70}
print(grades.get("Leyla"))
# grades.update({"Aysel": 88})
grades["Aysel"] = 88
# grades.update({"Orxan": 75})
grades["Orxan"] = 75
grades.pop("Ali")
for key, value in grades.items():
    print(f"{key}: {value}")

print(grades.get("Nigar", "Not found"))
