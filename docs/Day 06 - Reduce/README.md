# Day 06 - Reduce

This is the last higher order function we'll see and like the previous ones it gets one function and one sequence.

## Differences from the others:

- The function takes two elements of the sequence at once.
- It doesn't return a list, it returns a single value.
- Must be imported.

## How does it work?

Suppose we have the following list

```python
[2, 6, 9, 1]
```

The function **reduces** takes 2 values and performs an action, the result of this continues as the first parameter in the next execution and the same action is performed.

For this case we will add the values:

```python
from functools import reduce

def add(num_a, num_b):
    return num_a + num_b

numbers = [5, 9, 4, 1]
print(reduce(add, numbers))

# Output:
# 19
```

## Steps

First of all

- `num_a`: 5
- `num_b`: 9
- returned value: 14

Then

- `num_a`: 14 (previous returned)
- `num_b`: 4 (next in sequence)
- returned value: 18

Finally

- `num_a`: 18
- `num_b`: 1
- Final returned value: 19

It is not the best way to do it however to perform a new test. Let's join the following list and return a string.

```python
from functools import reduce

def join_string(word_a, word_b):
    string = f"{word_a} {word_b}"
    return string

words = ["My", "name", "is", "Esteban"]
print(reduce(join_string, words))

# Output:
# My name is Esteban
```

[Go to the Challenge](https://github.com/estebansolo/Python30/blob/master/docs/Day%2006%20-%20Reduce/exercise.py)