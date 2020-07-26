# Day 15 - Else

As you can see from ***Error Handling***, we can use the 'else' clause not only with conditionals, in this case we'll see that we can use this clause with other statements.

## For/Else

Before we explain how we can include the else, we'll create a loop like the one below:

```python
numbers = range(10, 21)
for number in numbers:
    print(number)

# The previous loop will print the numbers from 10 to 20.
```

If you are familiar with loops, you will know that the **break** sentence will interrupt the execution and continue outside of it.

```python
numbers = range(10, 21)
for number in numbers:
    if number == 17:
        break
    print(number)

# The previous loop will print the numbers from 10 to 16, when the
# number 17 continues, the conditional will validate it and the loop
# will be interrupted, so the execution will continue.
```

However, there are cases when we are going through some kind of data we will realize that the loop ended without finding a **break**, in these cases is when we can make use of the `else` clause.

```python
numbers = range(10, 21)
for number in numbers:
    if number == 60:
        break
else:
    print("Number 60 was not found")

# The else clause is executed when a loop is not interrupted,
# and will only execute the block of code when the loop is over.
```

## While/Else

The while statement also allows the use of the `else` clause, and like the for loop it will only be executed if no break is found in the while block.

```python
while conditional:
    # Do some stuff with possibilities of break
else:
    # Do some stuff if no break executed
```

[Go to the Challenge](https://github.com/estebansolo/Python30/blob/master/exercises/15_else.py)
[Go to the Solution](https://github.com/estebansolo/Python30/blob/master/solutions/15_else.py)