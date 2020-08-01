"""
Create a recursive function which calculates the
factorial of a given number

Factorial: factorial(5) => 1*2*3*4*5 => 120

3 => 6
5 => 120
7 => 5040
10 => 3628800
"""

def factorial(number):
    if number == 1:
        return number
    
    return number * factorial(number - 1)

print(factorial(10))

"""
Let's simulate the operation of the operator module (%).

4 % 2 => 0
59 % 6 => 5
"""

def module(number, subtract):
    if number < subtract:
        return number
    
    return module(number - subtract, subtract)
    
print(module(59, 6))
print(59 % 6)