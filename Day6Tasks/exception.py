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
subject=('maths','sci','soc')
student=set()
dic={}
def addStudent():
    try:
        name=input("enter student name: ")
        subject=(int(input("enter maths marks: ")),
        int(input("enter sci marks: ")),
        int(input("enter soc marks: ")))
        dic[name]=list(subject)
    except ValueError:
        print("Invalid input! Please enter numeric marks.")
    except TypeError:
        print("Marks data type error.")
    

def displayStudent():
    print(dic)

def totMarks(list,index=0):
    if len(list)<=index:
        return 0
    return list[index]+totMarks(list,index+1)
def calAvg():
    try:
        name=input("enter student name to calculate average: ")
        if name in dic.keys():
            tot=totMarks(dic[name])
            avgMarks=tot/len(subject)
            print("Total Marks: ",tot)
            print("Average Marks: ",avgMarks)
        else:
            raise NameError
    except NameError:
        print("Student name not found.")
    except ZeroDivisionError:
        print("Cannot divide by zero.")

while True:
    print("1. Add Student\n2. Display Students\n3. Calculate Average\n4. Exit")
    num=int(input("Enter choice: "))
    if num==1:
        addStudent()
    elif num==2:
        displayStudent()
    elif num==3:
        calAvg()
    elif num==4:
        break
    else:
        print("Invalid choice")
