"""15. Infinite Even Number Generator (Generators)
Create a generator function that continuously generates even numbers starting from 2. 
The program should print the first N even numbers using this generator.
"""
def even_num(n):
    for i in range(2,n+1):
        if i%2==0:
            yield i
n=int(input("enter n: "))
for i in even_num(n):
    print(i)