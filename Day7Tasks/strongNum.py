""". Strong Number
Question:
Write a program to check whether a given number is a Strong number.
Definition:
A Strong number is a number whose sum of factorial of digits is equal to the number itself.
Example:
Number = 145
Calculation:
1! + 4! + 5!
= 1 + 24 + 120
= 145
Output:
145 is a Strong number"""
def fact(num):
    if num==0 or num==1:
        return 1
    else:
        return num*fact(num-1)
    
def strongNum(num):
    l=list(num)
    sum=0
    for i in l:
        i=int(i)
        sum+=fact(i)
    print(sum)
    if int(num)==sum:
        return "Strong Number"
    else:
        return "Not a Strong number"
print(strongNum(input("enter number:")))