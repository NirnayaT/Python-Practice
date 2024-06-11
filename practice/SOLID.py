'''
                SOLID
---------------------------------------
S- SINGLE RESPONSIBILITY PRINCIPLE (SRP)
O- OPEN / CLOSE PRINCIPLE (OCP)
L- LISKOV SUBSTITUTION PRINCIPLE (LSP)
I- INTERFACE SEGREGATE PRINCIPLE(ISP)
D- DEPENDENCY INVERSION PRINCIPLE(DIP)
---------------------------------------

-->Introduced by Robert C. Martin (Computer Scientist) a.k.a Uncle Bob
-->SOLID acronym introduced by Micheal Feathers.
-->Set of rules and best practices to follow while
    designing class structures.
    
WHY SOLID?
"
    To create understandable, readable, and testable code
    that many developers can collaboratively work on.
"

SRP:
    A class should one and only one reson to change.
    
    Only one responsibility.
    
    If a class takes care of more than one task then
    we should seperate those task into seperate class.
    
OCP:
    Introduced by Betrand Meyer in 1988.
    
    Software entities (classes, functions, modules, etc)
    should be open for extension, but closed for modification.
    
    Making a class into abstract base class (ABC) and using 
    abstract method on the method is a way to implement OCP 
    because it forces child class to make its own method.
    
LSP:
    Introduced by Barbara Liskov at an OOPSLA conference in 1987.
    
    Subtypes must be substainable for their base types.
    
    The method should be implemented for sub types in such a way 
    that it dosen't affects the behaviour of the program for that
    we can use SRP.
    
ISP:
    Uncle Bob introduced ISP.
    
    Clients should not be forced to depend updon methods that they 
    do not use. Interface belongs to client, not to hierarchies.
    
    So, the best method is to use SRP and OCP principle in ISP.
    
DIP:
    Introduced by Uncle Bob.
    
    Abstraction shouldn't depend upon details rather details should
    depend upon abstraction.
    
    Suppose, there are two class and methods in it, method in first class 
    is to display data and set data in second class. Here, the second class
    shouldn't make a concrete database. Clients should be able to make changes
    in the data into different database and here it shows that abstraction depends 
    on details where details should. Hence, DIP principle should be implemented.
'''

#Example for SRP
class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email
    
    def get_username(self):
        return self.username
    
    def get_email(self):
        return self.email

# In this example, the User class has a single responsibility: managing user data.

#Example for OCP
from abc import ABC,abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius * self.radius

# New shapes can be added by creating new classes without modifying existing ones.

#Example for LSP
class Bird:
    def fly(self):
        pass

class Sparrow(Bird):
    def fly(self):
        print("Sparrow is flying")

class Ostrich(Bird):
    def fly(self):
        raise NotImplementedError("Ostrich cannot fly")

# Both Sparrow and Ostrich are subclasses of Bird and can be used interchangeably where Bird is expected.

#So instead we can,
class canfly:
    def fly(self):
        pass
class bird:
    def wings(self):
        pass
class sparrow(bird,canfly):
    def fly(self):
        pass
class ostrich(bird):
    pass
#Although, both sparrow and ostrich are birds, only sparrow can fly.

#Example for ISP

class UsernameProvider:
    def get_username(self):
        pass

class EmailProvider:
    def get_email(self):
        pass

class UserWithUsernameAndEmail(UsernameProvider,EmailProvider):
    def __init__(self, username,email):
        self.username = username
        self.email = email
    
    def get_username(self):
        return self.username
    def get_email(self):
        return self.email
    
class UserwithEmail(EmailProvider):
    def __init__(self, email):
        self.email = email
    
    def get_email(self):
        return self.email

user = UserWithUsernameAndEmail("Nirnaya","hahaha@123.com")
print("Username:", user.get_username())  # Output: Username: Nirnaya
print("Email:", user.get_email())  #  Output: hahaha@123.com

#Suppose we have a class that needs only the get_username() method and not the get_email() method. We can create a separate interface for this purpose.

#Example for DIP

class FrontEnd:
    def __init__(self, back_end):
        self.back_end = back_end

    def display_data(self):
        data = self.back_end.get_data_from_database()
        print("Display data:", data)

class BackEnd:
    def get_data_from_database(self):
        return "Data from the database"
    
'''
In this example, the FrontEnd class depends on the BackEnd class and 
its concrete implementation. You can say that both classes are tightly 
coupled. This coupling can lead to scalability issues. For example, say 
that your app is growing fast, and you want the app to be able to read 
data from a REST API. How would you do that?

-We can't. So instead we can.
'''
from abc import ABC, abstractmethod

class FrontEnd:
    def __init__(self, data_source):
        self.data_source = data_source

    def display_data(self):
        data = self.data_source.get_data()
        print("Display data:", data)

class DataSource(ABC):
    @abstractmethod
    def get_data(self):
        pass

class Database(DataSource):
    def get_data(self):
        return "Data from the database"

class API(DataSource):
    def get_data(self):
        return "Data from the API"