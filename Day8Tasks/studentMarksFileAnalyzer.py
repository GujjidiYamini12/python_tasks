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
dict={"Rahul":80,"Anita":90,"Ravi":75}
with open("marks.txt",'w') as file:
    for i,j in dict.items():
        data=file.write(f"{i} {j}\n")
count=0
tot=0
avg=0
with open("marks.txt",'r') as file:
    data=file.read()
    print(data)
    word=data.split()
    print("All student records:")
    for i in word:
        if i.isdigit():
            tot+=int(i)
            count+=1
        else:
            print(i)
    avg=tot/count
    print("Average of marks: ",avg)
    
