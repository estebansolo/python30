# Day 17 - Memoization

Memoization is a caching technique which stores the result of complex operations to be used in case the same call is made again.

In this way we can optimize not only the execution time but also the use of memory of our logic based on previous processes.

```python
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)
```

This function is a bit complex depending on the number we send to calculate the fibonacci, to see how long the execution could take we will use **timeit**.

```python
from timeit import timeit

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

timeit("fibonacci(35)", setup="from __main__ import fibonacci", number=1)

# Output
# 3.4363581580000755
```

This process was performed once and took about 4 seconds, if you can see it is a recursive function which is called itself several times per execution and sometimes performs the same operation for the same arguments.

This process can be optimized because we will always get the same result if we pass the same argument, in other words, it is a pure function.

```python
from timeit import timeit

history = {}

def fibonacci(n):
    if n in history:
        return history[n]
    if n == 0:
        return 0
    elif n == 1:
        return 1
    fibonacci_result = fibonacci(n - 1) + fibonacci(n - 2)
    history[n] = fibonacci_result
    return fibonacci_result

timeit("fibonacci(35)", setup="from __main__ import fibonacci", number=1)

# Output
# 0.0001454799985367572
```

The execution time and resources are quite low thanks to a history, as you can see, when we know the fibonacci of a number `x` this is stored and before calculating it the only thing we have to do is check if we have calculated it before so we don't have to do it again.

[Go to the Challenge](exercise.py)
