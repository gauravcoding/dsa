def age_checker(func):
    def wrapper(age, **kwargs):
        if age >= 18:
            print("You're an adult now!")
            return func(age, **kwargs)
        else:
            print("You're not adult")
            return None
        # Return the result of the original function
    return wrapper  # Ensure the wrapper is returned from the decorator

@age_checker
def ForVote(age):
    return "You can vote"

print(ForVote(18))  # Call the decorated function


class Parent:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello {self.name} from Parent")


class Child(Parent):
    def __init__(self, name):
        super().__init__(name)

    def greet(self):
        print(f"Hello {self.name} from Child")


obj = Child("Gaurav")

obj.greet()
obj.greet()


class person:
    name="Gaurav singh"
    occ="Python developer"
    def __init__(self,name,occ):
        self.name=name
        self.occ=occ
    def info(self):
        print(f"{self.name} is a {self.occ} ")
a=person("Gaurav","Software developer")
a.info()
b=person("Akriti","HR")
b.info()






def half_upper(str):
    length=len(str)//2
    return str[:length+1].upper() + str[length+1:]
print(half_upper("geeksforgeeks"))



def num_char(str):
    numberAvl=False
    charAvl=False
    for item in str:
        if item.isalpha():
            charAvl=True
        if item.isdigit():
            numberAvl=True
    return charAvl and numberAvl
print(num_char("thishasboth29"))
print(num_char("geeksforgeeks"))