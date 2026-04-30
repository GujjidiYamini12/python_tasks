'''4. Operators'''
'''1. Write a program to add two numbers using arithmetic operators. '''
n1=int(input())
n2=int(input())
print(n1+n2)
'''2. Write a program to check if one number is greater than another. '''
if(n1>n2):
    print("n1 is greatest")
else:
    print("n2 is greatest")
'''3. Use modulus operator to check if a number is even or odd. '''
if(n1%2==0):
    print("It is an Even number")
else:
    print("It's an odd number")
'''4. Write a program using logical operators to check age eligibility for voting.''' 
age=int(input("enter age: "))
if(age>18 | age==18):
    print("eligibility")
else:
    print("not eligibility")
'''5. Demonstrate the use of assignment operators (`+=`, `-=`). '''
sum=10
sum+=20
print(sum)
sum=10
sum-=20
print(sum)
'''6. Write a program using comparison operators. '''
if((n1>n2 & n1==n2 )| (n1>=n2)):
    print("n1 is greatest")
elif(n1<n2 | n1!=n2):
    print("n2 is greatest")
'''7. Calculate the power of a number using `**`. '''
power=n1**2
print(power)
'''8. Use floor division operator to divide two numbers. '''
print(" floor division of n1 and n2: ",n1//n2)
'''9. Write a program that checks if two numbers are equal.''' 
if(n1==n2):
    print("n1 is equal to n2")
else:
    print("n1 is not equal to n2")
'''10. Combine arithmetic and comparison operators in one expression.'''
a=20
b=(10+5*3)>=a
print(b)