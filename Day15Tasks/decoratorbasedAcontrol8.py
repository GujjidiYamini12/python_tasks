"""8. Decorator-based Access Control
Scenario:
Restrict access to certain functions.
Task:
● Create a decorator to check user role
● Use condition inside decorator
● Apply decorator to multiple functions
● Store roles in a dictionary
"""
dic={
    "Yamini":"developer",
    "Subbu":"Police"
}
def access_control(role):
    def decorator(func):
        def wrapper(name):
            if dic.get(name)==role:
                print("Accessed")
                return func(name)
            else:
                print("Denied")
        return wrapper
    return decorator
@access_control("developer")
def developer(name):
    print(f"{name} is a developer")
@access_control("Police")
def Police(name):
    print(f"{name} is a police")
@access_control("Hacker")
def Hacker(name):
    print(f"{name} is a Hacker")
developer("Yamini")
Police("Subbu")
Hacker("Naveen")
Hacker("Name")