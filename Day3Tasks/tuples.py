'''1. Create a tuple with 5 elements and print it.'''
tup=(1,2,3,4,5)
print(tup)
print(type(tup))
'''2. Write a program to find the length of a tuple.'''
l=len(tup)
print("length: ",l)
'''3. Write a program to access the second element in a tuple.'''
print("second element: ",tup[1])
'''4. Write a program to check whether an element exists in a tuple.'''
num=int(input("enter random ele: "))
print(num in tup)
'''5. Write a program to count how many times an element appears in a tuple.'''
tup=(1,2,2,3,3,3,4,4,4,4,5,5)
set1=set(tup)
for i in set1:
    print("count of {i}: ".format(i=i),tup.count(i))
'''6. Write a program to concatenate two tuples.'''
tup1=(1,2,3)
tup2=(4,5,6)
print("concatenate tuple: ",tup1+tup2)
'''7. Write a program to convert a tuple to a list and modify the element.'''
lst=list(tup)
print("{tup} tuple converted to list: {lst}".format(tup=tup,lst=lst))
'''8. Write a program to find the maximum and minimum values in a tuple.'''
print("maximum element: {max} and minimum element: {min}".format(max=max(tup1),min=min(tup1)))