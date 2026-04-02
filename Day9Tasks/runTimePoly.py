"""11. Payment System (Runtime Polymorphism)
An online store supports multiple payment methods: CreditCard, UPI, and
NetBanking. Create a base class Payment with a method process_payment() and
override it in each payment type.
"""
class Payment:
    def process_payment(self):
        print("Processing payment")
class CreditCard(Payment):
    def process_payment(self):
        print("Processing credit card payment")
class UPI(Payment):
    def process_payment(self):
        print("Processing UPI payment")
class NetBanking(Payment):
    def process_payment(self):
        print("Processing net banking payment.")
cc=CreditCard()
cc.process_payment()
upi=UPI()
upi.process_payment()
nb=NetBanking()
nb.process_payment()