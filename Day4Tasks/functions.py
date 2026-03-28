'''11. Write a program using a user-defined function to add two numbers.'''
def add1(a,b):
    return a+b
print(add1(int(input("enter a: ")),int(input("enter b: "))))
'''12. Write a program to create a function that prints a greeting message.'''
def greet():
    print("Hello everyone")
greet()
'''13. Write a function to find the square of a number.'''
def numSqrt(num):
    return num**2 #find power, multiply is optimatic
num=int(input("enter number: "))
print(numSqrt(num))
'''14. Write a program using the built-in function len() to find the length of a list.'''
def lenOfList(*lst):
    return len(lst)
print(lenOfList(1,2,4,3,5,6.7)) #create list with user input() once we have to write input()
'''15. Write a function to check whether a number is even or odd.'''
def evenOrOdd(number):
    print("even") if num%2==0 else print("odd")
evenOrOdd(num)
'''16. Write a function that returns the factorial of a number.'''
def fac(number):
    if number==0 or number==1:
        return 1
    return number*fac(number-1)
print(fac(5))
    
'''17. Write a program using the built-in max() function to find the largest number in a list.'''
lst=[1,2,3,5,5,6,7,8]
print("largest number: ",max(lst))
'''18. Write a function to find the sum of elements in a list using a user-defined function.'''
def sumOfNum(lst):
    sum=0
    for i in lst:
        sum+=i
    return sum
print(sumOfNum([1,2,3,4,5]))
'''19. Write a function that takes a string as input and returns the number of vowels.'''
def noOfVowels(str1):
    vowLst=['a','e','i','o','u']
    countOfVowels=0
    for i in vowLst:
        if i in str1:
            countOfVowels+=str1.count(i)
    return countOfVowels
str1=input("string: ")
print("no of vowels: ",noOfVowels(str1))
'''20. Write a Python program with a function that returns the largest of three numbers.'''
def largest(a,b,c):
    return a if ((a>b) and (a>c)) else (b if ((b>a) and (b>c)) else c)
print(largest(1,2,3))