# Day 12 - Property

In object-oriented programming, the getter and setter methods help us access private attributes of a class, allowing the code to be well encapsulated and to avoid accessing them directly.

Although in Python we can't define methods or attributes as private, we can use a convention that indicates to other developers the level of accessibility of these.

- Protected: For protected attributes or methods, we must set an underscore before the definition. e.g. `self._name = "My name"`
- Private: Private attributes or methods have 2 underscores. e.g. `def __private_method(self):`

## Getter / Setter

```python
class User:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name
    
    def set_name(self, name):
        self.__name = name

user = User("Esteban", 26)
print(f"Name: {user.get_name()}")

user.set_name("Cristian")
print(f"Name: {user.get_name()}")

# Output:
# Name: Esteban
# Name: Cristian
```

The traditional way or as it is usually done in other programming languages is using normal methods.

This preamble is intended to give you an understanding of each of these levels and to help you understand how **Property** can help you create getters and setters in a Pythonic way.

## Property

`Property` is a built-in decorator that allows us to define the getter and setter.

Let's see with the same code as above how to use the property decorator.

```python
class User:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
    
    @property
    def name(self):
        print("Getter called")
        return self.__name
    
    @name.setter
    def name(self, name):
        print("Setter called")
        self.__name = name

user = User("Esteban", 26)
print(f"Name: {user.name}")
user.name = "Cristian"
print(f"Name: {user.name}")

# Output:
# Getter called
# Name: Esteban
# Setter called
# Getter called
# Name: Cristian
```

As you can see, the property decorator did not change much in the way we do the getter/setter however this allows it to be more intuitive and easy to read each of its attributes, also like the methods defined above, allow us to control how we access the attributes of the class.

The property decorator is defined in a method that will return the value of the attribute, to define the setter we must use the property created, `@<property>.setter`.

We don't have to define each of these methods for each property, as we only do this for those we're going to access, or they can be read-only attributes so we'll only need the getters.

Remember that we can implement these methods as we need them so that we won't affect the implementation of the code.

```python
class User:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
    
    @property
    def age(self):
        return self.__age
    
    @age.setter
    def age(self, age):
        if not isinstance(age, int) or age < 0:
            raise ValueError("Invalid age")
    
        self.__age = age

user = User("Esteban", 26)
user.age = "26"

# Output:
# Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
#  File "<stdin>", line 13, in age
# ValueError: Invalid age
```

[Go to the Challenge](https://github.com/estebansolo/Python30/blob/master/docs/Day%2012%20-%20Property/exercise.py)