# Day 20 - Context Managers

When working with any type of resources in any programming language, we must release them once we no longer use them, this must be done because leaving resources open and not making use of them can slow down the system or even cause it to fail.

Context managers are a Python feature that allows us to manage these resources in a simple way leaving aside the need to always assign and release resources manually.

Let's suppose that we need to make some operation with the handling of plain files, so we must open a file, read its content and close it once we are done with it:

```python
file = open('path/to/the/file')
content = file.read()
file.close()
```

As you can see when using this resource we must release it, for this case it is simply to close the file. However this process of opening and closing files is not the best and for some reason we could forget to add it.

When we use a context manager, we use the keyword `with`, the previous example would look like this:

```python
with open('path/to/the/file') as file:
    content = file.read()
```

It starts by opening a file for processing, reads its contents and just before leaving this block, closes it.

## Implementation

- [Context Managers with classes](#context-managers-with-classes)
- [Context Managers with functions](#context-managers-with-functions)

### Context Managers with classes

In order to create context managers using classes, we will be using the [Dunder Methods](../Day%2013%20-%20Dunder%20Methods), to be more precise the `__enter__` and `__exit__`.

```python
class ContextManager:
    def __init__(self):
        pass

    def __enter__(self):
        pass

    def __exit__(self, type, value, traceback):
        pass
```

- `__init__`: Creates the object.
- `__enter__`: Return the resource we are going to use.
- `__exit__`: It releases the resources when we finish using the context manager instance.

This last one, as you could see, receives three arguments that in case an exception occurs, it will pass the **type**, **value** and **traceback** of the exception so we can decide how to proceed at the moment of releasing the resource.

```python
class OpenFile:
    def __init__(self, filename):
        self.file = open(filename)
    
    def __enter__(self):
        return self.file

    def __exit__(self, type, value, traceback):
        self.file.close()
```

In this way we can try to simulate the behaviour when opening files, once we have defined our methods, we can make use of the `with` keyword.

```python
with OpenFile("path/to/the/file") as file:
    content = file.read()
```

### Context Managers with functions

We can also implement our context manager using functions, however to create them we must make use of [Decorators](../Day%2018%20-%20Decorators/) and [Generators](../Day%2019%20-%20Generators/).

```python
from contextlib import contextmanager

@contextmanager
def open_file(filename):
    file = open(filename)

    try:
        yield file
    except:
        # Exceptions that may occur  
    finally:
        file.close()
```

We use the decorator `@contextmanager` and the keyword `yield` to convert a simple function into a context manager, and in the same way here we can capture the exceptions that occur and manage them according to our needs.

The use of this context manager is the same as the one we did with classes, the only thing that would change is the name of the class/function we are using.

[Go to the Challenge](exercise.py)