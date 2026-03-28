'''1. Write a Python program to print a string entered by the user.'''
str1=input()
print("string entered by user: ",str1)
'''2. Write a program to find the length of a string.'''
l=len(str1)
print("length of str: ",l)
'''3. Write a program to convert a string to uppercase and lowercase.'''
print("uppercase: ",str1.upper())
print(str1)
print("lowercase: ",str1.lower())
'''4. Write a program to concatenate two strings.'''
print("Concatenate two strings: ",str1+"Gujjidi")
'''5. Write a program to check whether a substring exists in a string.'''
substr=input("enter substr here: ")
print("{substr} is exists in {str}: ".format(substr=substr,str=str1),substr.upper() in str1.upper())
'''6. Write a program to count the number of vowels in a string.'''
vow=['a','e','i','o','u']
count=0
for i in vow:
    if i in str1:
        count+=1
print("no.of vowels in string: ",count)
'''7. Write a program to reverse a string.'''
rev_str=str1[::-1]
print("reverse string method 1: ",rev_str)
rev_str=''
for i in str1:
    rev_str=i+rev_str
print("reverse string method 2: ",rev_str)
'''8. Write a program to check whether a string is a palindrome.'''

print('True palindrome') if str1.lower()==rev_str.lower() else print('False palindrome')
'''9. Write a program to count the frequency of each character in a string.'''
for i in str1:
    print("{i} count in {str1}: ".format(i=i,str1=str1),str1.count(i))
'''10. Write a program to remove duplicate characters from a string.'''
str1=input("enter string: ")
remDupStr=""
for i in str1:
    if i not in remDupStr:
        remDupStr+=i
print(remDupStr)