# Day 07 - Lambdas

Lambda functions are also known as anonymous functions, they can, as a normal function, take different arguments and return a single value, but lambdas are one-line functions.

The syntax is as follows:

```python
lambda arguments: expresion
```

## Example

```python
def normal_multiply(num_a, num_b):
    return num_a * num_b

lambda_multiply = lambda num_a, num_b: num_a * num_b

print(normal_multiply(5, 2))
print(lambda_multiply(5, 2))

# Output:
# 10
# 10
```

As you can see both `normal_multiply` and `lambda_multiply` functions, another difference you can notice is that **lambda** functions return a value without explicitly using the `return` keyword.

## Why use Lambda functions?

We can create functions that perform a simple actions or operations using **lambda functions**, so that we can make our code more compact and simple.

Let's try using the lambda functions with one of the previous examples.

### Filter example

```python
def multiple(number):
    return number % 2 == 0

numbers = range(1, 101)
filter_numbers = filter(multiple, numbers)
print(list(filter_numbers))
```

#### Using lambda function

```python
numbers = range(1, 101)
filter_numbers = filter(lambda number: number % 2 == 0, numbers)
print(list(filter_numbers))
```

When you understand the syntax of these functions, you will see that they are really easy to use and can be very useful.

[Go to the Challenge](https://github.com/estebansolo/Python30/blob/master/exercises/07_lambdas.py)

[Go to the Solution](https://github.com/estebansolo/Python30/blob/master/solutions/07_lambdas.py)