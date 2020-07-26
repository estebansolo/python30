# Day 11 - Classmethod and Staticmethod

We have not yet started to create our decorators but this time we will try to use two that comes with python, these are `staticmethod` and `classmethod`

In order to explain how to make use of a decorator right now, we must put it over the definition of the method/function with the prefix `@`.

The methods of a class are a kind of function which is defined in a class and can be of three types:

- [Instance Methods](#Instance%20Methods)
- [Class Methods](#Classmethod)
- [Static Methods](#Staticmethod)

## Instance Methods

Instance methods are the ones we usually create when working with classes, these methods must have an argument that is always the first one and as a convention, it is called **self**, these methods are part of the instance that we create.

```python
class MyClass:
    def instance_method(self):
        print("Instance Method Called")

instance = MyClass()
instance.instance_method()

# Output:
# Instance Method Called
```

We define a method called `instance_method` which as we indicated must have `self` as the first parameter which refers to the instance created and we can use it to read or create attributes or use other methods in this instance of the class.

## Classmethod

In order to define a class method, we must use the `classmethod` decorator. When working with instance methods, the method must have an argument which is self, which refers to the instance created, in this case, we will not define `self` because we cannot use anything related to the instance, however, we must use an argument which by convention is `cls`.

```python
class MyClass:
    attribute = "hello, world"
    
    @classmethod
    def class_method(cls):
        """ Class Method """
        print(cls.attribute)

MyClass.class_method()

# Output:
# hello, world
```

**cls** refers to the class itself and the attributes defined in it.

## Staticmethod

The static methods are defined the same as the class methods but this time the decorator `staticmethod` is used. Unlike the other methods, these do not receive any mandatory argument (besides that our logic requires).

So these methods can not access attributes or other methods of the class or instance.

```python
class MyClass:
    def __init__(self):
        self.static_method(50)

    @staticmethod
    def static_method(number):
        print("Static Method Called")
        print(number * number)

MyClass.static_method(30)

# Output: 
# Static Method Called
# 900

instance = MyClass()

# Output: 
# Static Method Called
# 2500
```

Static methods can be called from both instance and class.

## What's it for?

We may never have used them, but we probably needed them.

The static methods are useful to separate the logic that doesn't have to make use of the instance or the class, and it' s also good practice to separate this kind of logic.

Let's see an example using both decorators

```python
class FileManager:
    def __init__(self, json_content):
        self.content = json_content
        print(json_content)
    
    @classmethod
    def from_csv(cls, filename):
        file_content = cls.read_csv_content(filename)
        return cls(file_content)
    
    @staticmethod
    def read_csv_content(filename):
        # Read file
        # Convert to json
        return content

instance_from_json = FileManager(json_content)
instance_from_csv = FileManager.from_csv("path/to/the/file")
```

Static method we use them for features that do not require the instance or the class, the class method allows us to create a new instance of a different format than the one the class receives when it is instantiated which is json.

[Go to the Challenge](https://github.com/estebansolo/Python30/blob/master/exercises/11_classmethod_static_method.py)
[Go to the Solution](https://github.com/estebansolo/Python30/blob/master/solutions/11_classmethod_static_method.py)