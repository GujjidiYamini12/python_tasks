"""5. Perfect Number
Question:
Write a program to check whether a number is a Perfect number.
Definition:
A Perfect number is a number whose sum of proper divisors equals the number.
Example:
Number = 6
Divisors: 1, 2, 3
Sum = 1 + 2 + 3 = 6
Output:
6 is a Perfect number"""
def perfectNum(num):
    sum=0
    for i in range(1,num):
        if num%i==0:
            sum+=i
    if sum==num:
        print("perfect number")
    else:
        print("not perfect number")
perfectNum(int(input("enter integer:")))