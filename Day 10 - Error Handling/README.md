# Day 10 - Error Handling

Python provides us with a very useful structure that allows us to handle the errors that can be caused in our projects.

`try/except` allows us to capture errors and manipulate them without stopping the workflow.

The `try` block contains the code that could cause an error and we''re going to capture it in except.

```python
try:
  int("Hello")
except:
  print("An exception occurred")
```

The code above is intended to capture any error generated within the try structure, this one is because we can't cast as a number the string "Hello".

## Catching specific exceptions

Although in the previous code we were able to capture the error, it is not a good practice to do so since we have no knowledge of what is wrong.

If our code generates any exceptions of which we are not aware, it could affect us instead of helping us. Python is included with some [excepciones](https://docs.python.org/3/library/exceptions.html#bltin-exceptions), however each library we use can have its own exceptions as well as we can create them ourselves.

```python
int("Hello")

# Output:
# Traceback (most recent call last):
# File "<stdin>", line 1, in <module>
# ValueError: invalid literal for int() with base 10: 'Hello'
```

If we run only the casting we'll see the error that python generates, specifically **ValueError**, this will be the error that we'll capture.

```python
try:
  int("Hello")
except ValueError as err:
  print("An exception occurred:", err)

# Output: An exception occurred: invalid literal for int() with base 10: 'Hello'
```

## Multiple Exceptions

We could capture more than one exception to perform different actions, we can leave them separately to manipulate them separately or in the same exception for the same process.

```python
try:
  int("Hello")
except (ValueError, TypeError) as err:
  # Actions to take if the code generates ValueError or TypeError
  pass
except ZeroDivisionError:
  # ZeroDivisionError captures another action
```

## Raising Exceptions

These errors that occur in our code were executed at some point, so we can do it ourselves using the `raise` keyword.

```python
try:
  number = "Hello"
  if not number.isnumeric():
    raise ValueError(f"{number} is not numeric")
except ValueError as err:
  print(err)

# Output:
# Hello is not numeric
```

## Else

Usually when we hear about the `else` clause we relate it to conditionals, however in python we can use it for different structures, one of them is the **try/except**.

The `else` clause allows us to execute the code if no exception has been generated.

```python
try:
  number = int("12")
except ValueError as err:
  print(err)
else:
  print("No exceptions occurred")
  print("Number:", number)

# Output:
# No exceptions occurred
# Number: 12
```

## Finally

Another clause we can use with try/except is `finally`, it allows us to execute a block of code whether or not an exception is generated. **It will be executed at the end of the process** and after the else clause in case we have one.

```python
try:
  number = int("Hello")
except ValueError as err:
  print(err)
else:
  print("No exceptions occurred")
finally:
  print("This text will be printed whether or not an exception is generated")

# Output:
# invalid literal for int() with base 10: 'Hello'
# This text will be printed whether or not an exception is generated
```

[Go to the Challenge](exercise.py)