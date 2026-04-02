"""4. Bank Account System (Class, Object, Constructor)
A bank wants to manage customer accounts. Create a BankAccount class with a
constructor to initialize account number and balance. Implement methods to deposit,
withdraw, and display balance"""
class BankAccount:
    def __init__(self,accNum,bal):
        self.accNum=accNum
        self.bal=bal
    def deposit(self,depAcc):
        self.depAcc=depAcc
        self.bal+=self.depAcc
    def withdraw(self,withdrawAcc):
        self.withdrawAcc=withdrawAcc
        self.bal-=self.withdrawAcc
    def display(self):
        print(self.bal)
b=BankAccount(1234,10000)
print("Balance: ",end="")
b.display()
b.deposit(1000)
print("Balance After Deposit: ",end="")
b.display()
b.withdraw(500)
print("Balance After Withdraw: ",end="")
b.display()