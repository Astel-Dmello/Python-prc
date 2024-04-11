class Employee:
    def __init__(self, name, department, salary):
        self.name = name
        self.department = department
        self.salary = salary

    def read_employee_info(self):
        self.name = input("Enter employee name: ")
        self.department = input("Enter department: ")
        self.salary = float(input("Enter salary: "))

    def print_employee_info(self):
        print("Employee Name:", self.name)
        print("Department:", self.department)
        print("Salary:", self.salary)

# Example usage:
emp1 = Employee("John Doe", "IT", 50000)
emp1.print_employee_info()

print("\nEnter employee information:")
emp2 = Employee("", "", 0)
emp2.read_employee_info()
emp2.print_employee_info()

