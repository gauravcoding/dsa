class car:
    def __init__(self,model,type,year):
        self.model=model
        self.type=type
        self.year=year
    def display_info(self):
        print(f"Car model is {self.model} their type is {self.type} and manufacturer year is {self.year}")
c1=car("BMW","Petrol",2002)
c2=car("Mercedes","diesel",2005)
c1.display_info()
c2.display_info()

class Animal:
    def __init__(self,speak):
        self.speak=speak
class Dog(Animal):
    def sounds(self):
        print(f"Dog oftenly speaks {self.speak}")
D1=Dog("woof")
D1.sounds()


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
print(r1.area())
print(c1.area())

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
c1.display_info()
c2.display_info()

class Animal:
    def __init__(self,speak):
        self.speak=speak
class Dog(Animal):
    def sounds(self):
        print(f"Dog oftenly speaks {self.speak}")
D1=Dog("woof")




# inherit
class Employe:
    def __init__(self,id,name):
        self.id=id
        self.name=name
class NewEmploye(Employe):
    def __str__(self):
        return f"Employee ID: {self.id}, Name: {self.name}"


emp1=NewEmploye(10,"Gaurav")
print(emp1)

# encapsulation
class BankAccount:
    def __init__(self,account,balance=0):
        self.account=account
        self.balance=balance
    def deposit(self,amount):
        self.balance+=amount

    def withdraw(self,amount):
        if amount<self.balance:
            self.balance-=amount
        else:
            print("Insufficient Balance in your account")
    def info(self):
        return self.balance
account=BankAccount(1111313)
account.deposit(3000)
print(account.info())
account.withdraw(4000)





class str_list_method:
    print("We are now try to solve programs using CLASS")
    def upper(self,str):
        self.str=str
        return str.upper()
    def common_number(self,list1,list2):
        intersection_list=[]
        self.list1=list1
        self.list2=list2
        for ele in list1:
            for item in list2:
                if ele==item:
                    intersection_list.append(item)

                else:
                    intersection_list
        return intersection_list
    def dict_to_list(self,list1,list2):
        self.list1 = list1
        self.list2 = list2
        return dict(zip(list1,list2))

method=str_list_method()
print(method.upper("gaurav"))
print(method.common_number([1,2,3,4,5],[3,4,5,6,7]))
print(method.dict_to_list([1,2,3,4],[5,6,7]))

class animal:
    def __init__(self, legs):
        self.legs = legs
class StreetAnimal(animal):
    def __init__(self, name, legs, sound):
        super().__init__(legs)
        self.sound = sound
        self.name = name

    def info_about(self):
        print(f"{self.name} has {self.legs} legs and makes a {self.sound} sound")

dog = StreetAnimal("Dog", 4, "Bark")
dog.info_about()

from math import *
class Area:
    def __init__(self, radius):
        self.radius = radius

class Circle(Area):
    def __init__(self, radius):
        super().__init__(radius)
    def calculate_area(self):
        print(f"Area of the shape is {pi*self.radius**2}")
fourSide=Circle(10)
fourSide.calculate_area()