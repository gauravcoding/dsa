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

print(ForVote(17))  # Call the decorated function
