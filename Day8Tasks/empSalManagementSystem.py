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
dict={"Ramesh":25000,"Sita":30000,"Arun":28000}
with open("employees.txt",'w') as file:
    for i,j in dict.items():
        data=file.write(f"{i} {j}\n")
with open("employees.txt",'r') as file:
    data=file.read()
    print(data)
print("Employee details are:")
with open("employees.txt",'r') as file:
    #data=file.read()
    data1=file.readlines()
    word={}
    for i in data1:
        a,b=i.split()
        word[a]=int(b)
    print(word)
    highest_sal=max(word.values())
    k=[k for k in word.keys() if word[k]==highest_sal]
    print(f"highest salary employee: {k}")
with open("employees.txt",'a') as file: 
    data=file.write("Yamini 23000")
print("Updated Employee.txt file")
with open("employees.txt",'r') as file: 
    data=file.read()
    print(data)