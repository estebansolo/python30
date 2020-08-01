# Day 08 - Comprehensions

The Python Comprehensions allow us in a clear and simple way, create sequences from other sequences, these work in a similar way to the **filter** and **map** functions.

Types of compressions:

- list comprehensions
- dictionary comprehensions
- set comprehensions

## List Comprehensions

We can create lists in a clear way, the list comprehension structure is:

```python
new_list = [output for i in sequence if condition]
```

Almost all the comprehensions work in a similar way depending on the type of structure we need to obtain.

- `new_list`: The variable which will contain the list.
- `output`: The output of every element in the list.
- `i`: Value in the sequence.
- `condition`: (optional) Comprehensions can have conditions to decide which value it will keep.

### Common Example

```python
totals = []
for number in range(1, 6):
    totals.append(number * 2)

print(totals)
```

We can perform this same action with the **map** function as we saw before, however this time we will use comprehension:

```python
totals = [number * 2 for number in range(1, 6)]
print(totals)

# Output:
# [2, 4, 6, 8, 10]
```

It works exactly the same, now how about filtering out just odd numbers?

Remember that we can add a conditional, if it is satisfied, the value will be kept in the new sequence

```python
totals = [number * 2 for number in range(1, 6) if number % 2 != 0]
print(totals)

# Output:
# [2, 6, 10] -> 1, 3, 5 (odd numbers)
```
## Dict Comprehensions

They work in a similar way, we just have to take into account, the type of braces that are used and the format of the dictionaries `key: value`

```python
new_dict = {output_key: output_value for i in sequence if condition}
```

We will use a list of numbers and create a dictionary in which its key will be the real number and its value will be the number multiplied by itself.

```python
new_dict = {}
numbers = [5, 8, 2, 6, 3]
for number in numbers:
    new_dict[number] = number * number

print(new_dict)

# Output:
# {5: 25, 8: 64, 2: 4, 6: 36, 3: 9}
```

#### Comprehension

```python
numbers = [5, 8, 2, 6, 3]
new_dict = {number: number * number for number in numbers}
print(new_dict)

# Output:
# {5: 25, 8: 64, 2: 4, 6: 36, 3: 9}
```

In this example we can also use conditionals, the same way we can work with other types of data such as sets or generators.

[Go to the Challenge](https://github.com/estebansolo/Python30/blob/master/exercises/08_comprehensions.py)

[Go to the Solution](https://github.com/estebansolo/Python30/blob/master/solutions/08_comprehensions.py)