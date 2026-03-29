"""1. Write a Python program using the random module to generate 10 random integers
between 1 and 100 and store them in a list. Print the list."""
import random
count=0
l=[]
while count<=10:
    l.append(random.randint(1,100))
print(l)
"""2. Write a program that uses random.choice() to randomly select a student from a
list and display:
"The selected student for presentation is: <name>"."""
"""3. Write a Python program using the math module to calculate and display the square
root, floor value, and ceiling value of a number entered by the user."""
"""4. Write a Python program that generates 20 random numbers between 1 and 200 using
the random module and store them in a list.
Then using the math module, compute and display:
● Maximum value
● Minimum value
● Square root of the maximum number
● Logarithm of the minimum number"""
"""5. Create a Number Guessing Game where:
● The program generates a random number between 1 and 50 using random.
● The user has 5 attempts to guess the number."""