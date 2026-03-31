"""4. Prime Number
Question:
Write a program to check whether a number is Prime.
Definition:
A Prime number is a number that has only two factors: 1 and itself.
Example:
Number = 7
Output:
Factors = 1, 7
7 is a Prime number"""
def prime(num):
    count=0
    for i in range(2,num):
        if num%i==0:
            count+=1
    if count>1:
        print(" not prime")
    else: 
        print("prime")
prime(int(input("enter integer:")))