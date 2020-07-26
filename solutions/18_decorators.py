"""
Create a decorator that works as a cache for the different
calls we make to a function, you can test with the function
fibonacci.
"""

from timeit import timeit

def memo(fn):
    cache = {}
    def wrapper(*args):
        if args not in cache:
            cache[args] = fn(*args)
        
        return cache[args]
        
    return wrapper

@memo
def fibonacci(num):
    if num in [0, 1]:
        return num
    
    return fibonacci(num - 1) + fibonacci(num - 2)

print(timeit("fibonacci(35)", setup="from __main__ import fibonacci", number=1))

"""
Create a decorator logger which prints out what you are calling
and what you get as a result of the function.
"""

def logger(fn):
    def wrapper(*args, **kwargs):
        print(f"Calling '{fn.__name__}' function".center(50, "="))
        if args:
            print("Positional Arguments:", args)
            
        if kwargs:
            print("Keyword Arguments:", kwargs)
            
        response = fn(*args, **kwargs)
        
        print(f"Response: {response}")
        
        return response
        
    return wrapper

@logger
def add(num_a, num_b):
    return num_a + num_b

@logger
def multiply(num_a, num_b):
    return num_a * num_b


add(4, 7)
multiply(8, num_b=3)