'''#16.
def add(a, b, c):
    return a + b + c
 
values = [1, 2, 3]
print(add(values))'''
 

'''#17.
 
def square(nums):
    result = []
    for n in nums:
        result.append(n*n)
 
square([1,2,3,4])
print(result)'''
 

#18.
x = [1, 2, 3]
 
print(id(x))
 
x += [4]
 
print(id(x))