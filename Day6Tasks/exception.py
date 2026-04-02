"""Q1: Develop a Python program to manage student marks for three subjects. Store the subject
names in a tuple, maintain unique student names in a set, and store each student’s marks
in a list inside a dictionary where the key is the student name. Create user-defined
functions to add a student with marks, display all student records, and calculate the average
marks of a student. Implement a recursive function to calculate the total marks from the list of
marks. The program should interact with the user through a simple menu. Also include
exception handling to handle ValueError (non-numeric marks input), ZeroDivisionError
(average calculation issues), TypeError (incorrect data type in marks), and NameError (when a
student name entered does not exist in the dictionary).
Example Output:
1. Add Student
2. Display Students
3. Calculate Average
4. Exit
Enter choice: 1
Enter student name: Rahul
Enter marks for Math: 80
Enter marks for Science: 85
Enter marks for English: 90
1. Add Student
2. Display Students
3. Calculate Average
4. Exit
Enter choice: 2
Rahul : [80, 85, 90]
1. Add Student
2. Display Students
3. Calculate Average
4. Exit
Enter choice: 3
Enter student name to calculate average: Rahul
Total Marks: 255
Average Marks: 85.0
1. Add Student
2. Display Students
3. Calculate Average
4. Exit
Enter choice: 4
Example of Exception Handling Output
ValueError
Enter marks for Math: abc
Invalid input! Please enter numeric marks.
NameError
Enter student name to calculate average: Ramesh
Student name not found.
ZeroDivisionError
Cannot divide by zero.
TypeError
Marks data type errors"""
dit=[]
def addStudent(name,marks):
    dit={name:marks}
    print(dit) #displaying student
    avgMarks=sum(marks)/3
    return avgMarks
def totMarks(name, marks):
    if len(marks)==0:
        return 0
    return marks[0]+totMarks(marks[1:])        
name=input("enter student name: ")
mathsMarks,sciMarks,engMarks=int(input("enter maths marks: ")),int(input("enter sci marks: ")),int(input("enter eng marks: "))
marks=[mathsMarks,sciMarks,engMarks]
subject=('maths','sci','eng')
print("Total Marks: ",totMarks(name,marks))
print("Average Marks: ",addStudent(name,marks))
