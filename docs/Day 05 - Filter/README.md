# Day 05 - Filter

Another higher order function is **filter**, the function filter allows as its name indicates to filter a sequence and return only the values that fulfill a condition.

Like the Map function, it receives 2 arguments which are

- A function
- A sequence that is going to be filtered

## How does it work?

Each of the elements in the sequence will be delivered to the function, if the function returns **True** the value that is delivered will be kept, otherwise it will be discarded

```python
def keep_hello(element):
    return element == "hello"

strings = ["don't", "say", "hello"]
print(list(filter(keep_hello, strings)))
```

Each of the strings will be validated in the **keep_hello** function, in this case if the string is equal to **hello**, the value will be kept. The final list will be:

```
["hello"]
```

In the following example we will see how to validate which users are of legal age, remember that if they are not, we will discard them and keep only those who fulfill the condition.

```python
users = [
    {
        "name": "Esteban",
        "age": 26
    },
    {
        "name": "Jose",
        "age": 15
    },
    {
        "name": "Jaime",
        "age": 18
    }
]

def validate_age(user):
    return user["age"] >= 18

print(list(filter(validate_age, users)))

# Output:
# [
#   {'name': 'Esteban', 'age': 26},
#   {'name': 'Jaime', 'age': 18}
# ]
```

[Go to the Challenge](https://github.com/estebansolo/Python30/blob/master/docs/Day%2005%20-%20Filter/exercise.py)