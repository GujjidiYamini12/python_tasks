"""1. Student List Backup (Shallow Copy)
A teacher has a list of student marks:
marks = [50, 60, 70, 80]
Scenario:
She creates a backup using assignment:
backup = marks
Task:
● Modify the first element in marks.
● Observe the change in backup.
● Explain why both lists are affected.
"""
marks=[]
for i in range(4):
    marks.append(int(input()))
backup=marks
print(f"before changes: {marks}\nbefore changes: {backup}")
marks[0]=40
print(f"after changes: {marks}\nafter changes: {backup}")

"""marks, backup lists are referring to same memory address. 
So any changes made to mark will affects backup too. 
And it is called shallow copy"""
backup[3]=100
print(f"after changes: {marks}\nafter changes: {backup}")