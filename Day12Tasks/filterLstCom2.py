"""2. Even Number Filter (List Comprehension)
A system stores numbers:
nums = [1, 2, 3, 4, 5, 6]
Task:
● Use list comprehension to create a new list containing only even numbers"""
num=[]
for i in range(6):
    num.append(int(input()))
new_lst=[i for i in num if i%2==0]
print(new_lst)