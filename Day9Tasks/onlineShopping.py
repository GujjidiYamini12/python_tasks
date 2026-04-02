"""9. Online Shopping System (Multilevel Inheritance)
An e-commerce company organizes products using multiple levels. Create classes
Product → ElectronicProduct → MobilePhone using multilevel inheritance and
display product details."""
class Product:
    def display(self,name):
        self.name=name
        print(self.name)
class ElectronicProduct(Product):
    def display(self,name):
        self.name=name
        print(self.name)
class MobilePhone(ElectronicProduct):
    def display(self,name):
        self.name=name
        print(self.name)
p=Product()
p.display("Milk")
e=ElectronicProduct()
e.display("Radio")
m=MobilePhone()
m.display("Oppo F21")