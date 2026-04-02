""". Shape Area Calculator (Polymorphism)
A graphics application needs to calculate the area of different shapes. Create classes
Circle, Rectangle, and Triangle, each having an area() method. Demonstrate
polymorphism by calling the same method for different objects.
"""
from math import pi
class Circle:
    def area(self,radius):
        self.radius=radius
        area=pi*self.radius**2
        print(f"Area of circle: {area}")
class Rectangle:
    def area(self,length,width):
        self.length=length
        self.width=width
        area=self.length*self.width
        print(f"Area of Rectangle: {area}")
class Triangle:
    def area(self,height,width):
        self.height=height
        self.width=width
        area=0.5*self.height*self.width
        print(f"Area of Triangle: {area}")
c=Circle()
c.area(5)
r=Rectangle()
r.area(5,7)
t=Triangle()
t.area(5,9)