'''1. Create a list of 5 numbers and print all elements.'''
lst=[1,2,3,4,5]
print(lst)
'''2. Write a program to find the length of a list.'''
l=len(lst)
print(l)
'''3. Write a program to add an element to a list using append().'''
lst.append(6)
print(lst)
'''4. Write a program to access the third element in a list.'''
print("third element: ",lst[2])
'''5. Write a program to find the largest and smallest element in a list.'''
print("largest element: ",max(lst),"\t","smallest element: ",min(lst))
'''6. Write a program to reverse a list.'''
lst.reverse()
print("reverse list: ",lst)
lst.reverse()
'''7. Write a program to remove duplicate elements from a list.'''
lst.append(6)
print("before removing duplicates",lst)
for i in lst:
    if lst.count(i)>1 :
        lst.remove(i)
    else:
        continue
print("after removing duplicates",lst)
'''8. Write a program to find the second largest number in a list.'''
max_ele=max(lst)
print("first maximum element in list: ",max_ele)
lst.remove(max_ele)
secMaxElement=max(lst)
print("second max element: ",secMaxElement)
