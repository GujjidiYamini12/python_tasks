'''1. Create a dictionary with 3 student names and their marks.'''
dict1={"s1":90,"s2":50,"s3":60}
print(dict1)
'''2. Write a program to print all keys of a dictionary.'''
print("keys: ",dict1.keys())
'''3. Write a program to print all values of a dictionary.'''
print("values: ",dict1.values())
'''4. Write a program to access the value of a specific key.'''
print("value of specific key: ",dict1["s1"])
'''5. Write a program to add a new key-value pair to a dictionary.'''
print("before dict: ",dict1)
dict1["s4"]=70
print("after new ele added: ",dict1)
'''6. Write a program to update the value of an existing key.'''
print("before dict: ",dict1)
dict1["s2"]=55
print("after dict: ",dict1)
'''7. Write a program to check whether a key exists in a dictionary.'''
print("key exists: ","s5" in dict1.keys())
print("key exists: ","s2" in dict1.keys())
'''8. Write a program to find the student with the highest marks from a dictionary.'''
print("maximum marks: ",max(dict1.values()))