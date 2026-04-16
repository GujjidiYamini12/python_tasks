"""5. Employee Management System (OOP + File + Dict)
Scenario:
Manage employee data.
Task:
● Create a class Employee
● Store employees in a dictionary
● Save data to a file
● Use exception handling for invalid salary input
● Use loop to display all employees"""
class Employee:
    def __init__(self,id,name,salary):
        self.id=id
        self.name=name
        self.salary=salary
    def display(self):
        return f"{self.name} : {self.salary}"
emp={}
for i in range(3):
    id=int(input())
    name=input()
    try: 
        sal=int(input())
    except ValueError:
        print("Invalid input")
    e=Employee(id,name,sal)
    emp[id]=e
with open("emp.txt","w") as file:
    for i in emp.values():
        file.write(i.display()+"\n")
for i in emp.values():
    print(i.display())