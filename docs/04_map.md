# Day 04 - Map

Python comes with some higher order functions which can be very useful when working in a functional way.

In this first case we'll look at the **Map function**. The map function receives 2 arguments in the following order:

- A function
- At least a sequence (list, tuple, iterator, etc)

## How does it work?

Each of the elements of the sequence will be delivered to the function, this process is done 1 to 1 and what it will do depends on what we define in the function.

At the end we will obtain an iterator which will contain each of the results of the calls to the function.

```python
def multiply(element):
    return element * 2

numbers = [2, 4, 6, 8]
print(map(multiply, numbers))
```

In this example each number in the list will be given to the function and this number will be multiplied by 2, we return its result which at the end we will have a similar iterator as follows

```
<map object at 0x7f98f2b52150>
```

How can we see all the results?

Just like when we work with range to be able to see the numbers, we have to cast the result as a list.

```python
def multiply(element):
    return element * 2

numbers = [2, 4, 6, 8]
print(list(map(multiply, numbers)))
```

We can see the same list of numbers but after we've gone through the function. We can do this same process for any sequence of dict, strings, floats, etc

```python
users = [
    {
        "name": "Esteban",
        "age": 26
    },
    {
        "name": "Jose",
        "age": 23
    },
    {
        "name": "Jaime",
        "age": 40
    }
]

def get_age(user):
    return user["age"]

print(list(map(get_age, users)))

# Output:
# [26, 23, 40]
```

## Multiple Sequences

We can make use of the function map by passing multiple sequences, each of the sequences will give a value to the function at the same time

```python
def user(name, age, country):
    return {
        "name": name,
        "age": age,
        "country": country
    }


names = ["Esteban", "Jose", "Jaime"]
ages = [26, 23, 40]
countries = ["Colombia", "España", "Argentina"]

print(list(map(user, names, ages, countries)))

# Output
# [
#   {'name': 'Esteban', 'age': 26, 'country': 'Colombia'},
#   {'name': 'Jose', 'age': 23, 'country': 'España'},
#   {'name': 'Jaime', 'age': 40, 'country': 'Argentina'}
# ]
```

The way the map function works depends on whether we need to perform the same action for each of the elements in a sequence

[Go to the Challenge](https://github.com/estebansolo/Python30/blob/master/exercises/04_map.py)
[Go to the Solution](https://github.com/estebansolo/Python30/blob/master/solutions/04_map.py)