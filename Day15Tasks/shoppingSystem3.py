"""3. Shopping Cart System
Scenario: A user adds items to a shopping cart.
Task:
● Store items in a list
● Convert to set to remove duplicates
● Use loop + condition to calculate total cost
● Handle invalid input using try-except"""
try:
    lst=[]
    for i in range(3):
        product,quantity,cost=input(),int(input()),int(input())
        lst.append((product,quantity,cost))
    lst_to_set=set(lst)
    tot_cost=0
    for i in lst_to_set:
        print(f"{i[0]}: {i[2]*i[1]}")
        tot_cost+=i[2]*i[1]
    print(tot_cost)
except ValueError:
    print("Please! check entered input")
