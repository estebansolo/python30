# Day 1 - *args and **kwargs

When we define functions, we can make use of two kinds of arguments, ***positional arguments*** and ***named arguments or keyword arguments***.

Keyword arguments are normally used to declare arguments with a default value, which are then used in case we don't pass it in when we make the call.

## Arguments
```python
def multiply(a, b):
    print(a * b)

multiply(5, 4)

# Output: 20
```

## Keyword Arguments

```python
def keyword_multiply(a=2, b=9):
    print(a * b)

keyword_multiply()
keyword_multiply(5, 4)
keyword_multiply(b=4, a=4)
keyword_multiply(b=2)

# Output: 18
# Output: 20
# Output: 16
# Output: 4
```

Before explaining what are the `*args and **kwargs` we must emphasize that these variable names are only a **convention** and we can change their names when we need to, the important thing in this case are the * (asterisks)

## Use of *args

We use *args for positional arguments, i.e. those that do not have a default value in the definition of the function

```python
def fun(a, b, c):
    print(a, b, c)

fun(1, 2, 3)
```

```python
def fun(*args):
    print(args)

fun(1, 2, 3)

# Output: (1, 2, 3)
```

When we use *args we are treating all positional arguments as a **tuple**.

## Use of **kwargs

On the other hand we use the **kwargs for those arguments that have a default value in the definition of the function.

```python
def fun(a=0, b=0, c=0):
    print(a, b, c)

fun(a=1, b=2, c=3)
```

```python
def fun(**kwargs):
    print(kwargs)

fun(a=1, b=2, c=3)

# Output: {"a": 1,"b": 2,"c": 3}
```

When we use double asterisk (**) we are treating all keyword arguments as a **dict**.

This functionality allows us to pass an indefinite list of arguments, either positional or named, and treat them as 1 or 2 variables in the function, this is because just as we can combine both types of arguments when defining a function, we can make use of both variables in the same function.

**Note** that when working with both types of arguments, we must first define the positional arguments and then those that are named.

```python
def fun(*args, **kwargs):
    print(args)
    print(kwargs)

fun(1, 2, a=3, b=6)

# Output:
# (1, 2)
# {"a": 3, "b": 6}
```

## Use of *args and **kwargs when calling a function

In the same way that we can pass multiple arguments and receive them in a single variable, we can make use of the asterisks (*) to do the process in the opposite way, in other words, we have a variable (tuple, list) with `n` values and pass it to a function with multiple arguments.

```python
def func(a, b, c):
    print(f"a = {a}")
    print(f"b = {b}")
    print(f"c = {c}")
```

### Using a single asterisk

```python
numbers = [5, 4, 2]
func(*numbers)

# Output:
# a = 5
# b = 4
# c = 2
```

### Using double asterisk

```python
numbers = {"c": 4, "a": 6, "b": 9}
func(**numbers)

# Output:
# a = 6
# b = 9
# c = 4
```

In this case we could use the double asterisk although the function has no arguments with default values, since positional arguments can be treated in both ways.

## Python Example

If we see the Python documentation, the [print](https://docs.python.org/3/library/functions.html#print) function makes use of *args, in its case and as I indicated at the beginning, it is not necessary that it is called this way.

`print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)`

We can print multiple values by passing them to the function each separated by a comma or even using the *args

```python
print("Hello", "World")

values = ["Hello", "World"]
print(*values)

# Output:
# Hello World
# Hello World
```

[Go to the Challenge](exercise.py)