# Day 03 - List Slices

Before explaining how list slices work we must emphasize a couple of things.

1. Lists or arrays in other programming languages always start at index 0, i.e. if we have a list [a, b, c] the equivalent indexes are [0, 1, 2].
2. To move forward a little faster in this challenge you should know that the same rules apply as when working with the function range.

```
my_list[start:stop:step]
```

- `start`: (required) The initial value in the slice
- `stop`: (required) End of the slice, without including its value.
- `step`: (optional) The size of steps in the sequence the default value is 1

As we can see it is very similar to the function range, however there are some differences that we will detail below.

- Although I indicate that **start** and **stop** are required we can omit them and they will be taken from the index that begins and the index that ends, however we can define only one (either one), but this will be explained better with some examples.
- It cannot take negative values since as it works on the indexes of a list, these are only positive integers (0...). Stop can take negative values... ?

## Examples

```python
my_list = ["H", "E", "L", "L", "O"]
print(my_list[:])
```

If you haven't tried, what do you think is the output?

Going back to what I said before "start and stop are required", actually they are not, but as we are talking about slices, taking a part of the list, we must define the colon (:), this way we indicate that we are going to take from the first index (since before the colon no value was defined) to the last index (since no value was defined after the colon), this way we are generating a new list with this range that would be exactly the same.

Now how about we try to generate a list from the second index onwards? We don't need to define where it ends but where it begins

```python
my_list = ["H", "E", "L", "L", "O"]
print(my_list[2:])
```

Let's remember what the indices would be like

```
["H", "E", "L", "L", "O"]
[ 0 ,  1 ,  2 ,  3 ,  4 ]
```

As we are generating a slice from position 2 onwards we will get a list like the following

```python
["L", "L", "O"]
```

Now what we need is to obtain a similar list but up to the second last index, How do we do it? the initial index cannot contain negative indexes but the index where it ends does, indicating how many indexes it will exclude from the end.

So...

```python
my_list = ["H", "E", "L", "L", "O"]
print(my_list[:-1])
```

It will take from the beginning to the second last element in the list

```python
["H", "E", "L", "L"]
```

## Step

The step works in the same way as in the function range, its default value is 1 up but we can modify it if we want to go faster or in reverse

How do we create a new list but increase it from 2 items?

```python
my_list = ["H", "E", "L", "L", "O"]
print(my_list[::2])

# Output:
# ['H', 'L', 'O']
```

**Remember that if we want to take from the beginning to the end of the list we don't need to define any value but it must be blank**

And What if we want the same thing but in reverse?

```python
my_list = ["H", "E", "L", "L", "O"]
print(my_list[::-1])

# Output:
# ['O', 'L', 'L', 'E', 'H']
```

You can practice defining different values, combining them, changing the length of the list and its order.

Do you like it? Why don't you try:

```python
hello = "Hello World"
print(hello[::-1])
```

**You can use this slices not only with lists**

[Go to the Challenge](exercise.py)