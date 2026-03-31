""". Palindrome Number
Question:
Write a program to check whether a number is a Palindrome.
Definition:
A number is a Palindrome if it reads the same forward and backward.
Example:
Number = 121
Reverse = 121
Output:
121 is a Palindrome number
"""
def pal(num):
    rev=num[::-1]
    if num==rev:
        print("palindrome")
    else:
        print("not palindrome")
pal("121")