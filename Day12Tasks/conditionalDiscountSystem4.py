"""4. Conditional Discount System (List Comprehension)
A shop has prices:
prices = [100, 200, 300, 400]
Scenario:
● Apply a 10% discount only if price > 200.
Task:
● Use list comprehension with condition to create updated price list.
"""
prices=[]
for i in range(4):
    a = int(input())
    prices.append(a)
upd_pr_lst=[i+i*0.1 for i in prices if i>200]
print(f"prices: {prices}\nupd prices: {upd_pr_lst}")