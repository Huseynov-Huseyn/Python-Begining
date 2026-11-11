# Class Methods = Allows operations related to the class itself
#                 Take (cls) as the first parameter, which represent the class itself
#
# Instance Method = Best for operations on Instance of the class (object)
# Static Method = Best for utility functions that do not need access to class data
# Class Method = Best for class-level data or require access to the class itself
class Student:
    count = 0
    total_gpa = 0

    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
        Student.count += 1
        Student.total_gpa += gpa

    def get_info(self):
        return f"{self.name} {self.gpa}"

    @classmethod
    def get_count(cls):
        return f"Total number of student: {cls.count}"

    @classmethod
    def get_average_gpa(cls):
        if cls.count == 0:
            return "Couldn't find the student"
        else:
            return f"Average gpa of class: {cls.total_gpa / cls.count:.2f}"
