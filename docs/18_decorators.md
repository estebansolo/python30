# Day 18 - Decorators

In Python, ***decorators*** are very useful and powerful once we understand how they work and how we can create them.

Following the good practices of Python, we can use the decorators to have a cleaner and easier to understand code, without having to duplicate the code in different parts to express the same thing.

## What are decorators?

The most common definition is the following:

> Decorators are functions that take another function and extends the behavior of the latter function without explicitly modifying it.

Decorators are **high order functions**, they allow us to add functionality to an existing code without affecting its behavior, each decorator must be preceded by a `@`.

```python
def decorator(fun, arg_a, arg_b):
    total = fun(arg_a, arg_b)
    print(f"The result of {arg_a} and {arg_b} is {total}")

def add(num_a, num_b):
    return num_a + num_b

decorator(add, 6, 2)

# Output:
# The result of 6 and 2 is 8
```

In this example, the "decorator" takes the function and the arguments as parameters and performs a new operation, different from that of the main function.

This same process as a decorator would be:

```python
def decorator(fun):
    def wrapper(arg_a, arg_b):
        total = fun(arg_a, arg_b)
        print(f"The result of {arg_a} and {arg_b} is {total}")
    
    return wrapper

@decorator
def add(num_a, num_b):
    return num_a + num_b

add(6, 2)

# Output
# The result of 6 and 2 is 8
```

## Types of decorators

- [Functions with arguments](#functions-with-arguments).
- [Decorators with arguments](#decorators-with-arguments).

### Functions with arguments

The structure of decorators is made by nesting functions and returning each one of them depending on the values we receive (function/arguments). When a function to be decorated receives arguments, the decorator changes and a new function is nested which receives the arguments that the main function receives.

In order to make this clear, let's look at the following example:

```python
def operation(function):
    print("Function as an argument")
    def wrapper(*args, **kwargs):
        print("All function parameters as arguments (positiona & named)")
        return function(*args, **kwargs)
    
    return wrapper

@operation
def add(num_a, num_b):
    print("Decorated function")
    return num_a + num_b

print(add(2, 4))

# Output
# Function as an argument
# All function parameters as arguments (positiona & named)
# Decorated function
# 6
```

The decorator keeps returning a function, in this case the wrapper function that is in charge of receiving as parameters each one of the arguments that were given to the `add` function and internally the execution of the main function is done.

### Decorators with arguments

Decorators can also receive arguments to define their behavior, as mentioned above, nested functions must be created for each behavior, in this case as they are decorators' arguments, they go at the beginning of the decorator's definition.

```python
def operation(print_result=False):
    def _operation(function):
        # Create wrapper to use arguments

    return _operation

@operation(True)
def add(num_a, num_b):
    pass
```

The way we assign a decorator to a function changes, and we can send arguments to our needs, in the previous case a variable to indicate whether or not we want to print the result before returning to the place where the function was called.

- Decorators can also be created using **classes**.
- You can use multiple Decorators in the same function.

In python it is very important to know about decorators, the majority of libraries use them and as you saw before `@classmethod` and `@staticmethod` are decorators that python provides us to change the behavior of the methods of their classes.

[Go to the Challenge](https://github.com/estebansolo/Python30/blob/master/exercises/18_decorators.py)

[Go to the Solution](https://github.com/estebansolo/Python30/blob/master/solutions/18_decorators.py)