"""
Create a list of words and with it, create a new dictionary
in which the key is the word and the value is the same word
reversed.
"""

words = ["This", "is", "a", "dict", "comprehension"]
new_dict = {word: word[::-1] for word in words}
print(new_dict)

"""
Let's try this one again:

Using the range function, create a sequence of numbers
from 1 to 100, and using the comprehension to return only
those that are multiplies of 2.
"""

numbers = range(1, 101)
multiples = [number for number in numbers if number % 2 == 0]
print(multiples)

"""
[[1, 2, 3, 4], [5, 6, 7, 8]]

Use the list above and create nested comprehensions so that
the final value is a new list like the following

[[2, 4, 6, 8], [10, 12, 14, 16]] The number multiplied by 2
"""

numbers = [[1, 2, 3, 4], [5, 6, 7, 8]]
totals = [[number * 2 for number in number_list] for number_list in numbers]
print(totals)
