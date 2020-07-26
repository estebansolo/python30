# Day 02 - Range

**Range** is a built-in funtion that generates a sequence of numbers from the given values.

The syntax is as follows:

```python
range([start,] stop [, step])
```

As you can see, the function receives up to 3 parameters, however only one is required

- `start`: (Optional) The initial value in the sequence, by default is 0
- `stop`: (required) End of the sequence, without including its value.
- `step`: (optional) The size of steps in the sequence the default value is 1

## Let's Try

We'll print out what the function **range** returns if we pass it number 5. Remember that it has a parameter that is required (stop).

So, In this case the sequence will start at 0 and end at 5 (not including it).

`start` and `step` will take their default values.

```python
print(range(5))
```

We'll see that when printing it returns something similar to **range(0, 5)**, but what we want is to see the complete sequence, so to see the values that compose it, for this we must cast this range as a list

```python
sequence = list(range(5))
print(sequence)
```

The output is now more understandable

```
[0, 1, 2, 3, 4]
```

### Two parameters

When we call **range** passing two arguments, with the first value we define where the sequence starts and with the second one where it ends.

**Remember that the value where it ends is not included in the sequence**

```python
print(list(range(2, 9)))

# Output:
# [2, 3, 4, 5, 6, 7, 8]
```

### Three parameters

When we use the function with all its arguments, we will define where it starts, where it ends and how many steps the sequence will be.

```python
print(list(range(-5, 5, 2)))

# Output:
# [-5, -3, -1, 1, 3]
```

We can see that the sequence starts at -5 and ends at 5, but why doesn't he print the 4?

This is due to the steps we are indicating, which are 2, this way it will omit 1 value before returning the next

```
# Include [-5, -3, -1, 1, 3]
# Exclude [-4, -2, 0, 2, 4]
```

## Notes

- All values must be integers
- Values can be positive or negative

**Try this**

```
print(list(5, -5, -1))
```

## How can I use float numbers with range?

The answer, You can't... if you need to create a sequence of numbers with floating values, you could take a look to [numpy.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html)

[Go to the Challenge](https://github.com/estebansolo/Python30/blob/master/exercises/02_range.py)
[Go to the Solution](https://github.com/estebansolo/Python30/blob/master/solutions/02_range.py)