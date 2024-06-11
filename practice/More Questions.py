# The principles of Object Oriented Programming(OOP). Relevant example to each other.

'''
    In Object Oriented Programming(OOP), there are four main principles: 
    1. Abstraction
    2. Encapsulation
    3. Inheritance 
    4. Polymorphism
    
    1. Abstraction: 
        -Abstraction is the process for hiding unecessary details and only displaying essential details.
       It is used in python by importing ABC, abstractclass from abc (ABC: Abstract Back Class). By passing ABC 
       in the Class and using @abstractmethod we can initiate abstraction.
       
       So basically, Abstraction is used in Inheritance, while the base class is using abstract method to a method,
       then the child class may required to fulfill the condition to create the same method for itself to inherit from 
       parents class.
       
       For Example:
         Bank Class App
'''

#Abstraction
from abc import ABC, abstractmethod #importing Abstract Base Class

class Bankapp(ABC):#creating a class
    def database(self):
        print("connected to the database.")
    
    @abstractmethod#abstractmethod decorator. 
    #Classes derived from this class cannot then be instantiated unless all 
    #abstract methods have been overridden.
    def security(self):
        pass
class Mobileapp(Bankapp):#inheritating Bankapp class
    def mobilelogin(self):
        print("Logged in to Mobile App.")
    
    def security(self):#overriding abstract method
        print("This is secure.")
        
mob = Mobileapp()#creating an object for the mobile app class
mob.security()#calling method from child class


'''
    2. Encapsulation:
       -Encapsulation is the process of adding a layer to the details capsulating the details
       for security. In Python, Encapsulation is achieved by using access modifiers, controlling the 
       visibility of class attributes and methods.
       
       So there are three types of access Modifiers: public, private and protected.
       
       1. Public Members:
        -In public members, class attributes and methods are accessible both inside and
        outside the class. They are declared without any prefix or a underscore prefix.
        
        Example:
'''

class Bankapp:
    #public modifiers
    def __init__(self,username,password):
        self.username=username
        self.password=password

obj=Bankapp("Ram","123")
print(obj.username)#output = Ram
print(obj.password)#output = 123

'''
    2. Protected Members:
        -In protected members, class attributes and method are
        just accessible within the class or it's child class. They are declared
        with a _ prefix.
        
        Example:
'''

class Bankapp:
    def __init__(self,username,password):
        #protected modifiers
        self._username=username
        self._password=password
    
obj1= Bankapp("Ram","123")
# print(obj1.username)#shows error

'''
    3. Private Members:
        -In private members, they are just accessible within the class. They are declared
        with a __ prefix.
        
        Example:
'''

class Bankapp:
    def __init__(self,username: str ,password: str):
        #protected modifiers
        self.__username=username
        self.__password=password
    
obj2= Bankapp("Ram","123")
# print(obj2.username)#shows attribute error

'''
    Sometimes the private modifiers can be accessed outside the
    class causing some negative impacts. In that situation, we can
    user getters and setters for more security while accessing the 
    variables or methods, we can set criteria using getters and setters.
    
    
    3. Inheritance:
      -Inheritance allows us to define a class that inherits all the 
      methods and properties from another class.
      
      So, Parent Class is the class being inherited from.
      and Child class is the class being inherited to.
      
      For Example:
'''
#Single Inheritance
class Bankapp():#creating a Base class
    def database(self):
        print("connected to the database.")
        
    def security(self):
        print("This is secure.")
class Mobileapp(Bankapp):#inheritating and creating derived class
    def mobilelogin(self):
        print("Logged in to Mobile App.")
        
mob = Mobileapp()#creating an object for base class
mob.security()#we can use methods from parent class after inheritating.

'''
    So, basically, There are five types of inheritance:
    1. Single Inheritance
    2. Multiple Inheritance
    3. Multilevel Inheritance
    4. Hybrid Inheritance
    5. Hierarchical Inheritance
    
    1. Single Inheritance
      -It is a type of inheritance where the child class 
       inherits methods and attributes from one parent class.
       
    Example:
    Is above
      
    2. Multiple Inheritance:
        -It is a type of inheritance where the child class 
        inherits from multiple parent class.
        
    Example:
    
'''
#Multiple Inheritance
class Bankapp():#Base class
    def database(self):
        print("connected to the database.")
        
    def security(self):
        print("This is secure.")
class Mobileapp():#Base Class
    def mobilelogin(self):
        print("Logged in to Mobile App.")
    
class Menu(Bankapp,Mobileapp):#derived class
    def menuoption(self):
        print("Menu Option Appears.")
    
mob = Menu()#creating an object for derived class
mob.security()#output from base class: This is secure.
mob.mobilelogin()#output from base class: Logged in to Mobile App.
mob.menuoption()#out from the derived class: Menu Option appears.

'''
    3. Multilevel Inheritance:
        -It is a type of inheritance where derived class inherits from 
        another derived class.
        
    Example:
    
''' 
#MultiLevel Inheritance
class Bankapp():#Base class
    def database(self):
        print("connected to the database.")
        
    def security(self):
        print("This is secure.")
class Mobileapp(Bankapp):#Intermediate Class
    def mobilelogin(self):
        print("Logged in to Mobile App.")
    
class Menu(Mobileapp):#derived class
    def menuoption(self):
        print("Menu Option Appears.")
    
mob = Menu()#creating an object for derived class
mob.security()#output from base class: This is secure.
mob.mobilelogin()#output from Intermediate class: Logged in to Mobile App.
mob.menuoption()#out from the derived class: Menu Option appears.

'''
    4.Hybrid Inheritance:
        -It is a type of inheritance that consists multiple types
        of inheritance.
        
    Example:
    
'''
#Hybrid Inheritance
class Bankapp:#Base class
    def database(self):
        print("connected to the database.")
        
    def security(self):
        print("This is secure.")
class Mobileapp(Bankapp):#derived class
    def mobilelogin(self):
        print("Logged in to Mobile App.")
    
class Webapp(Bankapp):#dervied class
    def weblogin():
        print("Logged in to Web App.")
    
class Menu(Mobileapp,Webapp,Bankapp):#derived class
    def menuoption(self):
        print("Menu Option Appears.")

obj=Menu()
obj.database()
obj.security()
obj.mobilelogin()
'''
    5. Heirarchical Inheritance
        -It is a type of inheritance where multiple derived class are 
        created from one Base class.
        
        Example:
        
'''
#Heirarchical Inheritance
class Bankapp:#Base class
    def database(self):
        print("connected to the database.")
        
    def security(self):
        print("This is secure.")
class Mobileapp(Bankapp):#derived class
    def mobilelogin(self):
        print("Logged in to Mobile App.")
    
class Webapp(Bankapp):#derived class
    def weblogin():
        print("Logged in to Web App.")
    
class Menu(Mobileapp):#derived class
    def menuoption(self):
        print("Menu Option Appears.")

obj=Menu()
obj.database()
obj.security()
obj.mobilelogin()
'''
    4. Polymorphism:
    - Polymorphism means having many forms. So, basically in python, polymorphism is 
    implemented by three method:
        1. Method Overriding
        2. Method Overloading
        3. Operator Overloading
        
        1. Method Overriding :
         - It is the proccess for child class to override the existing
         method of parent class.
         
         For Example:
         
'''
class Bankapp():#creating a Base class
    def database(self):
        print("connected to the database.")
        
    def security(self):
        print("This is secure.")
class Mobileapp(Bankapp):#inheritating and creating derived class
    def mobilelogin(self):
        print("Logged in to Mobile App.")
    
    def database(self):#Method Overriding
        print("connected to mobileapp database.")
        
mob = Mobileapp()#creating an object for base class
mob.database()#we can use methods from parent class after inheritating.

'''
        2. Method Overloading:
        - Method overloading is the process where 
        method executes according to the input given.
        But, unfortunately in python, this feature is not 
        given. But, we can use it in a smart way using
        if-else condition.
        
        Example:
        
'''
class Bankapp:
        
    def user(self, name, pin=0):
        if pin == 0:
            print("Create a new pin")
        else:
            print(f"Welcome {name}! Logged in Sucessfully!")      

obj1 = Bankapp()
obj1.user('Nirnaya')#output: Create a new pin
obj1.user('Nirnaya',123)#output: Welcome Nirnaya! Logged in Sucessfully! 

'''
        3. Operator Overloading:
        - So, basically the process is same as method overloading but here 
        operator works according to the user input.
        
        For example: If we use '+' operator and the two input is str then it concatenates, if int 
        performs an addition, if list it merges both list and likewise.
        
'''