"""
Create a function that multiplies a sequence of
numbers.
"""

from functools import reduce

def multiply(number_a, number_b):
    return number_a * number_b

numbers = [5, 9, 7, 84, 15, 36, 2]
print(reduce(multiply, numbers))

"""
This challenge can be a bit complicated, however
remember to use conditionals to decide what action
to take. Create a function that takes a list of
strings and returns the sum of its characters.
"""

def count_chars(word_a, word_b):
    word_a = len(word_a) if isinstance(word_a, str) else word_a
    return word_a + len(word_b)

words = ["Hello", "World", "In", "Python"]
print(reduce(count_chars, words))

"""
Take a list of numbers and return the largest.
"""

def find_largest(num_a, num_b):
    largest = num_a
    if num_b > largest:
        largest = num_b

    return largest

numbers = [5, 9, 18, 3, 2]
print(reduce(find_largest, numbers))