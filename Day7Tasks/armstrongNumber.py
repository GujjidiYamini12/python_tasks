"""1. Armstrong Number
Question:
Write a program to check whether a given number is an Armstrong number or not.
Definition:
A number is called an Armstrong number if the sum of the cubes of its digits is equal to the
number itself.
Example:
Number = 153
Calculation:
1³ + 5³ + 3³
= 1 + 125 + 27
= 153
Output:
153 is an Armstrong numbe"""
def armStrong(num):
    l=list(num)
    sum=0
    for i in num:
        sum+=pow(int(i),3)
    return sum
input=input("enter number: ")
result=armStrong(input)
if int(input)==result:
    print("Armstrong Number")  
else:
    print("Not an Armstrong Number")