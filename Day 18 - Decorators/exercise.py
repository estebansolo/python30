"""
Create a decorator that works as a cache for the different
calls we make to a function, you can test with the function
fibonacci.
"""

from timeit import timeit

def fibonacci(num):
    if num in [0, 1]:
        return num
    
    return fibonacci(num - 1) + fibonacci(num - 2)

print(timeit("fibonacci(35)", setup="from __main__ import fibonacci", number=1))

"""
Create a decorator logger which prints out what you are calling
and what you get as a result of the function.
"""