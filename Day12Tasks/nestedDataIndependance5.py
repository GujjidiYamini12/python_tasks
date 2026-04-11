"""5. Nested Data Independence (Deep Copy)
A school stores classroom data:
classes = [["Math", [30, 35]], ["Science", [25, 28]]]
Scenario:
● Create a deep copy of this structure.
● Modify student count in original.
Task:
● Prove that copied data remains unchanged.
● Explain why deep copy is required here.
"""
import copy
classes=[]
for i in range(2):
    a=input()
    b,c=int(input()),int(input())
    classes.append([a, [b, c]])
marks=copy.deepcopy(classes)
marks1=copy.copy(classes)
print(f"before changes: {classes}\nbefore changes(dp): {marks}\nbefore changes(sc): {marks1}")
classes[0][1][1]=50
classes[0][0]="Social"
print(f"after changes: {classes}\nafter changes(dp): {marks}\nafter changes(sc): {marks1}")
"""deepcopy is independent. So, changes made to original list doesn't affect deepcopy list. 
To independent completely"""