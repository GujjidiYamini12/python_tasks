'''3. Type Casting
'''
'''1. Convert an integer to a float. '''
num=int(10)
float_num=float(num)
print(float_num)
'''2. Convert a float to an integer. '''
num=20.501
int_num=int(num)
print(int_num)
'''3. Convert a string `"123"` to an integer. '''
str='123'
print(int(str))
'''4. Convert an integer to a string and print it with text.''' 
a=10
#print(str(a))
'''5. Take a number as input and convert it to an integer. '''
num=input()
print(int(num))

'''6. Convert a float to a string and print it. '''
num_float=20.5
str=str(num_float)
print(str)
'''7. Add two numbers taken as strings by converting them to integers. '''
a=int(input())
b=int(input())
print(a+b)
'''8. Convert `"45.6"` to float. '''
print(float("45.6"))
'''9. Convert a number to string and concatenate it with another string. '''
a=int(2)
print("Hello"+str(a))
'''10. Write a program to display the type of converted variable.'''
a=input()
print(type(a))