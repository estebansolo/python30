# Day 19 - Generators

Before explaining what they are and how we can create our own generators, let's understand what iterators are.

An iterator is an object that allows to go through one by one the elements in a data structure, the iterators have a `next()` function which when called, returns the next element in the sequence, when there are no more elements, it throws an exception (StopIteration) which generates that the iteration stops.

Generators are basically iterators, the difference is that their elements are not stored in memory so we can only iterate over them once. The generators can be created using functions, however these functions do not use the keyword `return`, instead we use the keyword `yield`.

```python
def generator():
    counter = 0
    while counter < 10:
        yield counter
        counter += 1

my_gen = generator()

print(next(my_gen))
print(next(my_gen))
print(next(my_gen))
print(next(my_gen))

# Output
# 0
# 1
# 2
# 3
```

Initially we have a function which has a loop, however as you can see it has the keyword `yield`, which allows in each iteration to deliver a value and wait at that point until it is called again.

In other words, we have a counter with a value of 0 at the beginning, when we request an element from the iterator with the `next` function, the generator will reach the **yield** and deliver a value, it will increase the variable by one and return to the position of the **yield** waiting for the next call.

> Once the function yields, the function is paused and the control is transferred to the caller.

Finally, when the iterator ends, in this case when the counter reaches 10, an exception will be launched which will indicate that the iteration is over.

```python
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
```

We can use `for` loops to iterate over each of its elements, this will print each of the elements and once it is done, instead of launching the exception, it will finish the iteration:

```python
for num in generator():
    print(num)
```

## send

The generators have a `send()` method which allows us to send values to the generators to the point where they are waiting to continue, this in turn returns the next element of the iteration:

```python
def generator():
    counter = 0
    while counter < 10:
        new_value = yield counter
        if new_value:
            counter = new_value
        else:
            counter += 1

my_gen = generator()

print(next(my_gen))
print(my_gen.send(7))
print(next(my_gen))
print(next(my_gen))

# Output
# 0
# 7
# 8
# 9
```

In this case we must validate whether or not we have received a value, since in each iteration he receives a null value or `None`.

## throw

Also they have a `throw` method which is useful when we need to pass an exception to the generator, we must take into account that the generator will not stop if we can correctly validate it, and like the method [send](#send), it will return the next value in iteration.

```python
def generator():
    counter = 0
    while counter < 10:
        try:
            yield counter
        except ValueError:
            print("Raised Exception")
            counter += 2
        else:
            counter += 1

my_gen = generator()

print(next(my_gen))
print(my_gen.throw(ValueError))
print(next(my_gen))

# Output
# 0
# Raised Exception
# 2
# 3
```

Generators allow us as their name suggests to **generate** data at runtime, that's why they are very useful when we work with a larger volume of data.

[Go to the Challenge](https://github.com/estebansolo/Python30/blob/master/exercises/19_generators.py)

[Go to the Solution](https://github.com/estebansolo/Python30/blob/master/solutions/19_generators.py)