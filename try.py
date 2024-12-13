
def cal(a, b):
    try:
        print(a / b)
    except ZeroDivisionError:
        print("Denominator can't be zero")
    except TypeError:
        print("Put a numeric value")
    except ValueError:
        print("Put an integer value")

print(cal(10, "a"))


def division(A):
    try:
        raise ZeroDivisionError()
        if  A/0:
            print("not divionable")
        else:
            print("can be divisionale")
    except (ZeroDivisionError, ValueError) as error:
        print(error)
        print("Invalid input")
division(5)


#typeError
def add(a,b):
    try:
        c=a+b
        print(c)
    except TypeError:
        print("you can't add int wth str")
print(add(1,10))