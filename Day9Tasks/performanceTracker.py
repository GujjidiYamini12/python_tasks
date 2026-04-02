"""14. Performance Tracker (Decorators)
A software team wants to track how long functions take to execute. Create a decorator
that measures and prints the execution time of a function.
"""
import time
def track(func):
    def wrapper():
        start=time.time()
        func()
        end=time.time()
        print("Execution time: ",end-start)
    return wrapper
@track
def func():
    for i in range(100000):
        pass
func()
