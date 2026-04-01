"""1. Student Attendance Record
A teacher wants to store student attendance in a file named attendance.txt. Write a
Python program that takes a student name as input and appends it to the file. Then
display the contents of the file."""
name=input("enter student name: ")
file=open("attendance.txt","a")
file.write(name)
file.close()
file=open("attendance.txt","r")
print(file.read())
file.close()

"""2. Notes Reader Program
A student stores daily notes in a file called notes.txt. Write a program that opens the
file, reads all the contents, and displays them on the screen.
"""
with open("notes.txt","r") as file:
    content=file.read()
print(content)


"""3. Grocery List Manager
A user wants to save grocery items in a file grocery.txt. Write a Python program that
takes multiple items from the user and writes them into the file, with each item on a
new line."""
items = input("Enter grocery items separated by commas: ").split(",")

# Write items to file
with open("grocery.txt", "w") as file:
    for i in items:
        file.write(i.strip()+"\n")

print("Grocery list saved successfully.")

"""4. Student Marks File Analyzer
A teacher stores student marks in a file marks.txt in the format:
Name Marks
Example:
Rahul 80
Anita 90
Ravi 75
Write a Python program to:
● Read the file
● Display all student records
● Calculate and display the average marks of the class

"""
total = 0
count = 0
with open("marks.txt", "r") as file:
    print("Student Records:")
    for line in file:
        name, marks = line.split()
        marks = int(marks)
        print(f"{name} - {marks}")
        total += marks
        count += 1
if count > 0:
    average = total / count
    print(f"\nAverage Marks: {average}")
else:
    print("No records found.")
"""5. Word Counter Program
A writer saves an article in a file called article.txt. Write a Python program that:
● Opens and reads the file
● Counts the number of words, lines, and characters in the file
● Displays the results."""
with open("article.txt", "r") as file:
    content = file.read()
words = len(content.split())
lines = content.count("\n") + 1
characters = len(content)
print("Word Count:", words)
print("Line Count:", lines)
print("Character Count:", characters)
"""6. Employee Salary Management System
A company stores employee data in a file employees.txt in the format:
EmployeeName Salary
Example:
Ramesh 25000
Sita 30000
Arun 28000
Write a Python program that:
● Reads employee data from the file
● Displays all employee details
● Finds the employee with the highest salary
● Appends a new employee record to the file"""
highest_salary = 0
highest_employee = ""
with open("employees.txt", "r") as file:
    print("Employee Details:")
    for line in file:
        name, salary = line.split()
        salary = int(salary)
        print(f"{name} - {salary}")
        if salary > highest_salary:
            highest_salary = salary
            highest_employee = name
print(f"\nHighest Salary: {highest_employee} - {highest_salary}")
new_name = input("Enter new employee name: ")
new_salary = input("Enter salary: ")
with open("employees.txt", "a") as file:
    file.write(f"{new_name} {new_salary}\n")
print("New employee added successfully.")