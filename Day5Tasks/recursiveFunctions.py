'''1. Write a recursive function to calculate the factorial of a number.'''
def fact(n):
    if n==0 or n==1:
        return 1
    return n*fact(n-1)
print(fact(5))
'''2. Write a recursive function to find the nth Fibonacci number.'''
def fac(n):
    if n==2:
        return 3
    return n+fac(n-1)
print(fac(5))
'''3. Write a recursive function to calculate the sum of digits of a number.
Example: Input = 123 → Output = 6'''
def sum1(str1):
    sum=0
    for i in str1:
        sum+=int(i)
    return sum
print(sum("123"))
'''4. Write a recursive function to reverse a string.'''
def reverseString(str1):
    if len(str1)==1:
        return 