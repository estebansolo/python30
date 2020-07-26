"""
Again use the range function to generate a sequence of
numbers from 1 to 20, use the map function to return
whether the number is even or not.
"""

def is_even(number):
    return (number % 2 == 0)

print(list(map(is_even, range(1, 21))))

"""
Create two lists A and B of numbers, which must be given
to the function, the final result will be a new list which
will contain the sum of the values in A and B

A = [1, 5, 6]
B = [3, 5, 9]

C = [4, 10, 15]
"""

a = [1, 5, 6]
b = [3, 5, 9]

def add(num_a, num_b):
    return num_a + num_b

print(list(map(add, a, b)))

"""
Create a list of lists, these with multiple numbers to
be averaged

[
    [1, 2, 3],
    [9, 6, 1]
]
"""

list_of_lists = [
    [1, 2, 3],
    [9, 6, 1],
    [7, 9, 10]
]

def average(numbers):
    total = sum(numbers)
    return round(total / len(numbers), 2)

print(list(map(average, list_of_lists)))