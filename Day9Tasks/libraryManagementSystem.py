"""16. Library Management System (Constructor & Inheritance)
A library stores information about books and digital books. Create a base class Book
with a constructor to initialize book details. Create a derived class EBook that adds file
size information."""
class Book:
    def __init__(self,name,rating):
        self.name=name
        self.rating=rating
    def display(self):
        print(f"{self.name} rating {self.rating} ")
class EBook(Book):
    def __init__(self,name,rating,size):
        self.name=name
        self.rating=rating
        self.size=size
    def display(self):
        print(f"{self.name} rating {self.rating} with size {self.size}")
e=EBook("RDPD",4,200)
e.display()