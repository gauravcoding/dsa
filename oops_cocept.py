class car:
    def __init__(self,model,type,year):
        self.model=model
        self.type=type
        self.year=year
    def display_info(self):
        print(f"Car model is {self.model} their type is {self.type} and manufacturer year is {self.year}")
c1=car("BMW","Petrol",2002)
c2=car("Mercedes","diesel",2005)
# c1.display_info()
# c2.display_info()

class Animal:
    def __init__(self,speak):
        self.speak=speak
class Dog(Animal):
    def sounds(self):
        print(f"Dog oftenly speaks {self.speak}")
D1=Dog("woof")
# D1.sounds()


import math
class shape:
    def __init__(self):
        pass
class rectangle(shape):
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def area(self):
        return self.length*self.width
class circle(shape):
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return 3.14*self.radius**2
r1=rectangle(10,12)
c1=circle(11)
# print(r1.area())
# print(c1.area())

class vehicle:
    def start(self):
        print("Started")
class bike(vehicle):
    def start(self):
        print(self)
        print("Bike started")
bike1=bike()
class car:
    def __init__(self,model,type,year):
        self.model=model
        self.type=type
        self.year=year
    def display_info(self):
        print(f"Car model is {self.model} their type is {self.type} and manufacturer year is {self.year}")
c1=car("BMW","Petrol",2002)
c2=car("Mercedes","diesel",2005)
# c1.display_info()
# c2.display_info()

class Animal:
    def __init__(self,speak):
        self.speak=speak
class Dog(Animal):
    def sounds(self):
        print(f"Dog oftenly speaks {self.speak}")
D1=Dog("woof")
