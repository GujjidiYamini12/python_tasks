"""3. Employee Salary System (Simple Inheritance)
A company has two types of employees: Employee and Manager. Create a base class
Employee containing name and salary. Create a derived class Manager that inherits
from Employee and displays the employee details."""
class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def show(self):
        print(f"Employee name: {self.name}\nEmployee Salary: {self.salary}")
class Manager(Employee):
    def display(self):
        print(f"Manager name: {self.name}\nManager Salary: {self.salary}\n")
m=Manager('Rahul',10000)
m.display()
m.show()