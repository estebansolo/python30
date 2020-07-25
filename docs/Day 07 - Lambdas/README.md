# Day 07 - Lambdas

Lambda functions are also known as anonymous functions, they can, like a normal function, take different arguments but lambdas are one line functions.

```python
lambda arguments: expresion
```

## Example

```python
multiply = lambda a, b: a * b
print(multiply(5, 2))

# Output:
# 10
```

## Why use Lambda functions?

We can create functions that perform a simple action using **lambda functions**, so that we can make our code more compact and simple.

Let's try using the lambda functions with one of the previous examples.

### Filter example

```python
def multiple(number):
    return number % 2 == 0

numbers = range(1, 101)
print(list(filter(multiple, numbers)))
```

### Using lambda function

```python
numbers = range(1, 101)
print(list(filter(lambda number: number % 2 == 0, numbers)))
```

[Go to the Challenge](https://github.com/estebansolo/Python30/blob/master/docs/Day%2007%20-%20Lambdas/exercise.py)