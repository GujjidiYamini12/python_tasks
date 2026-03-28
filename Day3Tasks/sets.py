'''1. Create a set of numbers and print it.'''
set1={1,2,3,4,5,6,6}
print(set1)
'''2. Write a program to add an element to a set.'''
set1.add(7)
print("after adding ele: ",set1)
'''3. Write a program to remove an element from a set.'''
#set1.pop(2)
print(set1,set1.pop(),set1)
print(set1,set1.remove(3),set1)
print(set1,set1.clear(),set1)
'''4. Write a program to check if an element exists in a set.'''
print(1 in set1)
'''5. Write a program to find the union of two sets.'''
set1={1,2,3,4,5}
set2={2,3,4,5,6,7}
print("union: " ,set1.union(set2))
'''6. Write a program to find the intersection of two sets.'''
print("intersection: ",set1.intersection(set2))
'''7. Write a program to find the difference between two sets.'''
print("difference: ",set1.difference(set2))
'''8. Write a program to remove duplicate values from a list using a set.'''
lst=[1,2,3,4,5,6,3,4,2,1]
set1=set(lst)
print("removing duplicates: ",set1)