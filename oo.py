"""Discussion Questions

1. What are the three main design advantages that object orientation
   can provide? Explain each concept.

Abstraction - hiding away details that aren't significant for the use of something
Encapsulation - keeping relevant details together
Polymorphism - being able to use different parts of classes; creating a modular design; 
using parts interchangeably


2. What is a class?

    A class is a smarter dictionary.  It defines a set of behaviors (methods)
    or attributes for each instance that inherits from it.

3. What is a method?

A function defined within a class.


4. What is an instance in object orientation?

An instance is one example of a class.  While a class defines a set of behaviors, 
each instance inherits these behaviors from the class but can overrule/overwrite them.


5. How is a class attribute different than an instance attribute?
   Give an example of when you might use each.

   Every class attribute is passed on to its instances.  The instances can 
   overwrite the class attributes or include their own attributes which the class
   doesn't have. Instances inherit attributes from classes but classes don't inherit
   attributes from instances.


"""


"""2. Road Class"""


class Road(object):

    def __init__(self, num_lanes, speed_limit):
        """Initializes the road object"""
        self.num_lanes = 2
        self.speed_limit = 25

road_1 = Road(2,25)
road_1.num_lanes = 4
road_1.speed_limit = 60

road_2 = Road(2, 25)




"""3. Update Password"""


class User:
    """A user object."""

    def __init__(self, username, password):
        """Create a user with the given username and password."""

        self.username = username
        self.password = password

    def update_password(self, old_password, new_password):
        
        if self.password == old_password:
            self.password = new_password


"""4. Build a Library"""

class Book(object):
    """A Book object."""

    def __init__(self, title, author):
        """Create a book with the given title and author."""

        self.title = title
        self.author = author

class Library(object):

    def __init__(self):
        self.books = []

    def create_and_update_books(self, title, author):
        
        book = Book(title, author)
        self.books.append([book.title, book.author])

    def find_books_by_author(self, author):

        books_by_author = []
        for book in self.books:
            if book[1] == author:
                books_by_author.append(book)
        
        return books_by_author

"""5. Rectangle"""


class Rectangle:
    """A rectangle."""

    def __init__(self, length, width):
        """Create a rectangle with the given length and width."""

        self.length = float(length)
        self.width = float(width)

    def calculate_area(self):
        """Return the area of the rectangle."""

        return self.length * self.width

class Square(Rectangle):
    """A square."""

    def __init__(self, length):
        super().__init__(length, length)

        self.length = self.width = float(length)   
             
    def calculate_area(self):
        """Complete error hecking before returning area of the square."""

        if self.length == self.width:
            return super().calculate_area()  

        else:
            print("Invalid Square")