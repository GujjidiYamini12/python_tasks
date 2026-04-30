'''1. Bitwise Operators'''
'''1. Write a Python program to perform bitwise AND (&) on two numbers entered by the
user.'''
a=int(input("enter a:"))
b=int(input("enter b:"))
print(a&b)
'''2. Write a program to perform bitwise OR (|) operation between two integers.'''
print(a|b)
'''3. Write a program to demonstrate the bitwise XOR (^) operator using two numbers.'''
print(a^b)
'''4. Write a program to perform left shift (<<) and right shift (>>) operations on a number.'''
print(a<<2)
print(a>>2)
'''5. Write a Python program that takes a number and prints its bitwise NOT (~) value.'''
print(~a)
'''2. Conditional Statements'''
'''1. Write a program to check whether a number is positive, negative, or zero.'''
if(a>0): 
    print("positive")
elif(a<0):
    print("negative")
else:
    print("zero")
'''2. Write a program to check if a person is eligible to vote (age ≥ 18).'''
age=int(input("enter age for vote: "))
print("eligible") if age>=18 else print("not eligible")
'''3. Write a program to find the largest of three numbers using if-elif-else.'''
a,b,c=9,7,10
print(a,"is greatest") if a>b and a>c else print(b,"is greatest") if b>a and b>c else print(c, "is greatest")
'''4. Write a program to check whether a number is even or odd.'''
print(a,"is even") if a%2==0 else print(a,"is odd")
'''5. Write a program to assign grades based on marks (for example: A, B, C, Fail).'''
mark=int(input("enter marks: "))
if mark>=90:
    print("A")
elif mark>=80:
    print("B")
elif mark>=70:
    print("C")
elif mark>=60:
    print("D")
elif mark>=50:
    print("E")
else:
    print("Fail")

'''3. Looping Statements'''
'''1. Write a Python program to print numbers from 1 to 10 using a for loop.'''
for i in range(1,11):
    print(i)
'''2. Write a program to print the multiplication table of a number using a loop.'''
num=int(input("enter number for multiplication table: "))
for i in range(1,11):
    print("{num} * {i} = {num}*{i}".format(num=num,i=i))
'''3. Write a program to find the sum of numbers from 1 to N using a loop.'''
n=int(input("number for sum:"))
sum=0
for i in range(1,n+1):
    sum+=i
print(sum)
'''4. Write a program to print all even numbers between 1 and 50.'''
for i in range(1,50):
    if i%2==0:
        print(i,end=" ")
'''5. Write a program to calculate the factorial of a number using a loop.'''
n=int(input("number for factorial:"))
fac=1
for i in range(0,n+1):
    if i==0 or i==1:
        fac=1
    fac*=i
print(fac)

'''4. Jumping Statements'''
'''1. Write a program using break to stop printing numbers when the number reaches 5.'''
i=1
while(i<10):
    if i==5:
        break
    print(i,end=" ")
    i+=1
    
'''2. Write a program using continue to skip printing the number 3 in a loop from 1 to 10.'''
i=1
while(i<=10):
    if i==3:
        continue
    print(i,end=" ")
    i+=1
    
'''3. Write a program that uses pass inside a loop.'''
while(i<=10):
    pass
print("passed")
'''4. Write a program that searches for a number in a list and breaks the loop when found.'''
num=int(input("number for search:"))
l=[2,3,5,8,1,7,9]
for i in l:
    if i==num:
        print("founded breaking now")
        break
'''5. Write a program that prints numbers from 1 to 10 but skips even numbers using
continue'''
i=1
while(i<=10):
    if i%2==0:
        continue
    print(i,end=" ")
    i+=1