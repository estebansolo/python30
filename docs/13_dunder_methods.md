# Day 13 - Dunder Methods

"Everything in Python is an object." You've probably heard this before, that's because it is, every data type we use is an object that has been enriched to increase its performance.

Dunder methods, or magic methods, are methods we can define in our classes to give them more functionality than they have. These methods allow us to simulate the behavior of different data types from those we can find in the language.

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

I've created a basic class `User` which receives the name at the moment of its instantiation. When printing this instance, we can see the address in memory although now this is not what we need, how about improving this?

## Object Representation

`__repr__` is a method that allows us to define what information is going to represent our class, in this case, to see clear information of the created instance.

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

You have probably used the `len()` function more than once, but did you know we can also implement this in our objects?

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

The `len()` function allows us to know the number of characters in a string, however, we can use the magic method `__len__` to know from our object the number of characters that our `User` represents.

## More

There are quite a few methods that we probably won't need, however, we can practice with each of them to enrich our code like never before. [Dunder Methods](https://docs.python.org/3/reference/datamodel.html)

[Go to the Challenge](https://github.com/estebansolo/Python30/blob/master/exercises/13_dunder_methods.py)

[Go to the Solution](https://github.com/estebansolo/Python30/blob/master/solutions/13_dunder_methods.py)