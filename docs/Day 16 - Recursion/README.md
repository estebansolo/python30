# Day 16 - Recursion

Recursive functions are created when a function calls itself, this process will repeat indefinitely if we don't stop it in some condition, and only when it concludes, it will return a value to the place where it started its process.

We can turn any loop into a recursion.

```python
total = 0
for num in range(6):
    total += num

print(f"The sum of the numbers from 1 to 5 is equals to {total}")

# Output
# The sum of the numbers from 1 to 5 is equals to 15
```

We can convert this loop to a recursive function in the following way:

```python
def recursive_function(num):
    if num == 1:
        return num
    return num + recursive_function(num - 1)

times = 5
total = recursive_function(times)

print(f"The sum of the numbers from 1 to {times} is equals to {total}")

# Output
# The sum of the numbers from 1 to 5 is equals to 15
```

the above function is a basic example of what we can do, it starts by receiving the number 5 as an argument.

The first condition is used to end the recursion once the value of the argument is 1 and it will go in a chain by returning the total and adding it to the previous number. In other words:

```python
# First execution
>>> total = recursive_function(5)
>>> return 5 + recursive_function(4)
    # Second execution
    >>> return 4 + recursive_function(3)
        # Third execution
        >>> return 3 + recursive_function(2)
            # Fourth execution
            >>> return 2 + recursive_function(1)
                # Fifth execution
                >>> return 1
            >>> return 2 + 1 # 1 of the fifth execution
        >>> return 3 + 3 # 3 of the fourth execution
    >>> return 4 + 6 # 6 of the third execution
>>> return 5 + 10 # 10 of the second execution

# The sum of the numbers from 1 to 5 is equals to 15
```

When we call the function for the first time, a value is passed to it and it calls itself but passing a lower value and so on until the end (when the value is 1 and therefore it stops making more calls). At that point they start to return. The returned values are added to the original parameter in each one of the iterations until arriving at the beginning of everything in which the first call returns the final value.

[Go to the Challenge](https://github.com/estebansolo/Python30/blob/master/docs/Day%2016%20-%20Recursion/exercise.py)
