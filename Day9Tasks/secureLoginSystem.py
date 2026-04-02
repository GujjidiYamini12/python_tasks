"""13. Secure Login System (Decorators)
A web application wants to ensure that users are authenticated before accessing
sensitive functions. Create a decorator that checks whether the user is logged in before
allowing access to a function.
"""
user_login=False
def decorator(func):
    #user_login=True
    def wrapper():
        if user_login:
            func()
        else:
            print("User access denied")
    return wrapper
@decorator
def app():
    print("I'm web application")
app()