"""17. Employee Bonus Calculator (Decorators & OOP)
A company wants to apply a bonus calculation automatically before displaying the
salary. Create an Employee class and use a decorator that modifies the salary by
adding a bonus before displaying it."""
def addBonus(func):
    def wrapper(self):
        bonus=float(input("enter float bonus:"))
        tsal=self.sal+bonus*self.sal
        print("After bonus added: ",tsal)
    return wrapper
class Employee:
    def __init__(self,sal):
        self.sal=sal
    @addBonus
    def salary(self):
        print("Only sal: ",self.sal)
e=Employee(10000)
e.salary()