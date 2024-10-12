def repeat(num_times):
    def decorator_repeat(func):
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                func(*args, **kwargs)
        return wrapper
    return decorator_repeat

@repeat(num_times=3)
def greet(name):
    print(f"Hello, {name}!")

# Calling the decorated function
greet("Alice")



class Value:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def info(self):
        return f" His name is {self.name} and Age is {self.age}"
    @classmethod
    def employe(cls,name,age):
        return cls(name,age)
e1=Value.employe("gaurav",21)
print(e1.info())