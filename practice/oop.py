# class bike(): #class
#     name="H2R"
#     brand="Kawasaki"
#     engine="1000cc"
#     type="Sports"
    
    # def info(self):#methods
    #     print(f"The name of this bike is {self.name} which is {self.engine} engine by {self.brand}. It is a {self.type} bike.")
#is a reference to the current instance of the class, and is used to access variables that belongs to the class.
# a=bike()#object
# b=bike()
# c=bike()

# a.name="S1000RR"#creating objects
# a.engine="1098CC"
# a.brand="BMW"
# a.type="Sports"

# b.name="GS1260"
# b.engine="1260cc"
# b.brand="BMW"
# b.type="Touring"

# c.name="Dominar"
# c.engine="400cc"
# c.brand="Bajaj"
# c.type="Sports Tourer"


# b.info()

# class bike():
#     def __init__(self,n,e,b,t):
#         print("first Initial")
#         self.name=n
#         self.engine=e
#         self.brand=b
#         self.type=t
    
#     def info(self):#methods
#         print(f"The name of this bike is {self.name} which is {self.engine} engine by {self.brand}. It is a {self.type} bike.")

# a= bike("Dominar","373","Bajaj","Sports tourer")
# a.info()

# def add(a,b):
#     print("a","b")

# print(add(4,5))

class employee():
    def setInfo(self,name,id):
        self.name=name
        self.id=id
    
    def getInfo(self):
        print(f"Name: {self.name}, ID: {self.id}")

class staff(employee):
    def setInfo(self, name, id,time):
        self.name=name
        self.id=id
        self.time=time
        
    def worktime(self):
        n=int(self.time)
        if n > 7:
            remaining_hr=16-n
            print(f"You have {remaining_hr} hours left to work!")
        else:
            print("You are late!")
        
    
# E1 = employee()
# E2 = employee()
S1= staff()
S2 = staff()

# E1.setInfo("Nirnaya",10)
# E2.setInfo("Hari",11)
# E1.getInfo()


S1.setInfo(input("Enter the Staff Name: "),input("Enter Their id:"),input("Enter the entry time in hours:"))
S1.getInfo()
S1.worktime()