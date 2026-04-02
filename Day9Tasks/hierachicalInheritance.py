"""10. University Staff Management (Hierarchical Inheritance)
A university has different staff types such as Professor, LabAssistant, and
Administrator. All inherit from a base class Staff. Implement hierarchical inheritance
to manage and display their information.
"""
class Staff:
    def display(self,name,sal,id):
        self.name=name
        self.sal=sal
        self.id=id
        print(f"name: {self.name}\nsal: {self.sal}\nid: {self.id}")
class Professor(Staff):
    def display(self,name,sal,id):
        self.name=name
        self.sal=sal
        self.id=id
        print(f"name: {self.name}\nsal: {self.sal}\nid: {self.id}")

class LabAssistant(Staff):
    def display(self,name,sal,id):
        self.name=name
        self.sal=sal
        self.id=id
        print(f"name: {self.name}\nsal: {self.sal}\nid: {self.id}")
class Administrator(Staff):
    def display(self,name,sal,id):
        self.name=name
        self.sal=sal
        self.id=id
        print(f"name: {self.name}\nsal: {self.sal}\nid: {self.id}")

p=Professor()
p.display("Rahul",10000,1)
l=LabAssistant()
l.display("Yamini",1000,2)
a=Administrator()
a.display("Yamini",1000,3)