"""5. Vehicle Management System (Inheritance)
A transport company manages different vehicles. Create a base class Vehicle with
attributes like brand and speed. Create derived classes Car and Bike that inherit from
Vehicle and display their details."""
class Vehicle:
    def __init__(self,brand,speed):
        self.brand=brand
        self.speed=speed
    def display(self):
        print(f"Vehicle brand: {self.brand}\nVehicle speed: {self.speed}")

class Car(Vehicle):
    def display(self):
        print(f"Car brand: {self.brand}\nCar speed: {self.speed}")
class Bike(Vehicle):
    def display(self):
        print(f"Bike brand: {self.brand}\nBike speed: {self.speed}")

c=Car("Audi",160)
b=Bike("Royal and field",100)
v=Vehicle("IDK",50)
c.display()
b.display()
v.display()