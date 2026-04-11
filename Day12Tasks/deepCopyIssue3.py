"""3. Employee Data Copy Issue (Shallow vs Deep Copy)
A company stores employee data:
employees = [[101, "A"], [102, "B"], [103, "C"]]
Scenario:
● Create a shallow copy of the list.
● Modify one nested list (e.g., change "A" to "Z").
● Observe changes in both lists.
Task:
● Explain why the change reflects in both.
● Fix it using deep copy.
"""
import copy
employees=[]
for i in range(3):
    a, b = int(input()), input()
    employees.append([a, b])
manager=copy.copy(employees)
print(f"before changes: {employees}\nbefore changes: {manager}")
manager[0][1]="Z"
print(f"after changes: {employees}\nafter changes: {manager}")

