'''6. String Formatting'''
'''1. Print a name and age using string formatting. '''
print("Hi, this is {name} age is {age} old".format(name='Yamini',age=24))
'''2. Format a string using `format()` method. '''
print("Hi, this is {name} age is {age} old".format(name='Yamini',age=24))
'''3. Use **f-strings** to print a sentence with variables. '''
name='Yamini'
age=24
print(f"Hi, this is {name} age is {age} old")
'''4. Display a floating number with 2 decimal places. '''
num=float(input("enter floating number: "))
formatted="{:.2f}".format(num)
print(f"floating number with 2 decimal points: {format}")
'''5. Print a formatted price value. '''
print("{price}".format(price=100))
'''6. Create a sentence using two variables with formatting. '''
print("I'm printing sentence using {num} variables with formatting {string}".format(num=3,string="Yamini is a name"))
'''7. Format a number with commas (100000 → 100,000). 
number=input()

print("{number} with comma is {num1}".format(number,num1))'''
'''8. Display a percentage using string formatting. '''
print("percentage : {per}".format(per=100))
'''9. Align text using formatting. '''

'''10. Print a table row using formatted strings.'''