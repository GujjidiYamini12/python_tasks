"""1. Write a Python program using the random module to generate 10 random integers
between 1 and 100 and store them in a list. Print the list."""
import random
from math import *
count=0
num=[]
while count<10:
    num.append(random.randint(1,100))
    count+=1
print(num)
"""2. Write a program that uses random.choice() to randomly select a student from a
list and display:
"The selected student for presentation is: <name>"."""
l=["Yamini","Naveen","Laxmi","Narayana"]
print(f"The selected student for presentation is: <{random.choice(l)}>")
"""3. Write a Python program using the math module to calculate and display the square
root, floor value, and ceiling value of a number entered by the user."""
n=input("enter float: ")
a=input("enter integer: ")
print(f"square root: {sqrt(int(a))}, floor value: {floor(float(n))}, ceiling value: {ceil(float(n))}")
"""4. Write a Python program that generates 20 random numbers between 1 and 200 using
the random module and store them in a list.
Then using the math module, compute and display:
● Maximum value
● Minimum value
● Square root of the maximum number
● Logarithm of the minimum number"""
l=[random.randint(1,200) for i in range(20)]
print(f"maximum: {max(l)}\nminimum: {min(l)}\nSquare root: {sqrt(max(l))}\nLogarithm: {log(min(l))}")
"""5. Create a Number Guessing Game where:
● The program generates a random number between 1 and 50 using random.
● The user has 5 attempts to guess the number."""
print(f"NUMBER GUESS GAME")
num=random.randint(1,50)
for i in range(5):
    if int(input())==num:
        print("Correct")
        break
    elif i<4:
        print("Retry")
    else:
        print("Failed")