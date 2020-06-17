# Day 09 - Enumerate

Enumerate is a built-in Python function to which we can provide an iterator and return each of its elements in a tuple with a counter.

```python
enumerate(sequence, start=0)
```

The default start value is 0 since, as in other programming languages, the indexes start at 0.

```python
languages = ["Go", "Python", "Java"]
print(list(enumerate(languages)))

# Output:
# [(0, 'Go'), (1, 'Python'), (2, 'Java')]
```

The enumerate function returns an iterator, to be able to visualize it we must parse it or iterate it.

```python
languages = ["Go", "Python", "Java"]
for counter, element in enumerate(languages):
    print(counter, element)

# Output:
# 0 Go
# 1 Python
# 2 Java
```

The optional start argument can be manipulated with the argument called **start**.

```python
languages = ["Go", "Python", "Java"]
for counter, element in enumerate(languages):
    print(counter, element)

# Output:
# 1 Go
# 2 Python
# 3 Java
```

[Go to the Challenge](exercise.py)