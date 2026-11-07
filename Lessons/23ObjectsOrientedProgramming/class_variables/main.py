from Student import Student

student1 = Student("Huseyn", 21)
student2 = Student("Farid", 21)
student1.describe()
print(student1.class_year)
print(Student.class_year)
print(Student.num_of_students)
print(f"My graduating class of {Student.class_year} has {Student.num_of_students} students")
