class Person:
    def __init__(self):
        self.name = ""
        self.age = 0

    def read_person_info(self):
        self.name = input("Enter name: ")
        self.age = int(input("Enter age: "))

    def print_person_info(self):
        print("Name:", self.name)
        print("Age:", self.age)


class Student(Person):
    def __init__(self):
        super().__init__()
        self.roll_number = 0
        self.grade = ""

    def read_student_info(self):
        super().read_person_info()
        self.roll_number = int(input("Enter roll number: "))
        self.grade = input("Enter grade: ")

    def print_student_info(self):
        super().print_person_info()
        print("Roll Number:", self.roll_number)
        print("Grade:", self.grade)


# Example usage:
student1 = Student()
print("\nEnter student information:")
student1.read_student_info()
print("\nStudent information:")
student1.print_student_info()
