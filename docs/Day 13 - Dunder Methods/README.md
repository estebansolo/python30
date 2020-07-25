# Day 13 - Dunder Methods

"Everything in Python is an object." You've probably heard this before, that's because it is, every data type we use is an object that has been enriched to increase its performance.

Dunder methods, or magic methods, are methods that we can define in our classes to give them more functionality than they have. These methods allow us to simulate the behavior of different data types from those we can find in the language.

The name dunder methods come from double underscores as a prefix and suffix of the method, e.g. `__init__`.

```python
class User:
    def __init__(self, name):
        self.__name = name
    
new_user = User("Christopher")
print(new_user)

# Output:
# <__main__.User object at 0x7fafdc06cdd0>
```

I have created a basic User class which receives the name at the time of instantiation when printing this instance, we can see the address in memory although now it is not something we need to know, how about improving this?

## Object Representation

**__repr__** is a method that allows us to define what information is going to represent our class, in this case, to see clear information of the created instance.

```python
class User:
    def __init__(self, name):
        self.__name = name
    
    def __repr__(self):
        return f"Class User: {self.__name}"

new_user = User("Christopher")
print(new_user)

# Output:
# Class User: Christopher
```

## Count

You have probably already used the `len()` function more than once, but did you know that we can also implement it on our objects?

```python
class User:
    def __init__(self, name):
        self.__name = name
    
    def __repr__(self):
        return f"Class User: {self.__name}"
    
    def __len__(self):
        return len(self.__name)

new_user = User("Christopher")
print(new_user)
print(len(new_user))

# Output:
# Class User: Christopher
# 11
```

The `len()` function allows us to know the number of characters in a string, however, we can use the magic method __len__ to know from our object the number of characters that our User represents.

## More

There are quite a few methods that we can probably use more than we need, but we can practice with each one of them and enrich our code like never before. [Dunder Methods](https://docs.python.org/3/reference/datamodel.html)

[Go to the Challenge](https://github.com/estebansolo/Python30/blob/master/docs/Day%2013%20-%20Dunder%20Methods/exercise.py)