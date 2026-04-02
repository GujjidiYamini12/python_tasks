"""1. Student Information System (Class & Object)
A school wants a program to store student details. Create a Student class with
attributes such as name, roll number, and marks. Create objects for at least three
students and display their details."""
class Student:
    def __init__(self,name,rollNumber,marks):
        self.name=name
        self.rollNumber=rollNumber
        self.marks=marks
    
    def display(self):
        print("Student name: ",self.name)
        print("Student Roll Number: ",self.rollNumber)
        print("Student marks: ",self.marks,end="\n\n")
s1=Student("Yamini",1,100)
s2=Student("Deepika",2,90)
s3=Student("Upasana",3,95)
s4=Student("Muskhan",4,80)
s1.display()
s2.display()
s3.display()
s4.display()