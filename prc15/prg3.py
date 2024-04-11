class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print("Name:", self.name)
        print("Age:", self.age)


class Student:
    def __init__(self, roll_number, grade):
        self.roll_number = roll_number
        self.grade = grade

    def display_info(self):
        print("Roll Number:", self.roll_number)
        print("Grade:", self.grade)


class Resident(Person, Student):
    def __init__(self, name, age, roll_number, grade, address):
        Person.__init__(self, name, age)
        Student.__init__(self, roll_number, grade)
        self.address = address

    def display_info(self):
        print("Resident Information:")
        Person.display_info(self)
        Student.display_info(self)
        print("Address:", self.address)


# Example usage:
resident1 = Resident("John Doe", 25, 101, 'A', "123 Main Street")
resident1.display_info()
