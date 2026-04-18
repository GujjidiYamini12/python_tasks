"""1. Student Score Processor
Scenario:
A teacher stores student names and marks in a list of tuples.
Task:
● Convert data into a dictionary
● Use a loop + condition to find students scoring above 50
● Use math module to calculate average
● Store results in a text file
"""
import math
#stores student names and marks in a list of tuples
lst=[("Ravi",55),("Sree",50),("Yamini",100),("Naveen",90),("Deepika",45)]
#lst=[('Yamini', 90), ('Shashi', 100)]
"""for i in range(2):
    name, marks=input(),int(input())
    lst.append((name, marks))"""
#print(lst)
#Convert data into a dictionary
dit={}
names=[]
marks=[]
for j in lst:
    names.append(j[0])
    marks.append(j[1])
print(dit)
#print(f"{names}\n{marks}")
#Convert data into a dictionary
dit["name"]=names
dit["marks"]=marks
print(dit)
#Use a loop + condition to find students scoring above 50
fil_arr=[]
for i in dit["marks"]:
    if i>50:
        fil_arr.append(i)
print(fil_arr)
#Use math module to calculate average
avg=math.fsum(fil_arr)/len(fil_arr)
print(avg)
with open("text.txt",'a') as file:
    for i in dit.keys():
        file.write(f"{dit[i]}: {dit.get(i)}")
    file.write(f"Average marks of students: {avg}")