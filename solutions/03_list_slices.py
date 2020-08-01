"""
You can use the range function to easily create a list with
100 numbers, use list slices to take only those numbers that
are multiples of 3.
"""

numbers = list(range(1, 101))
print(numbers[2::3])

"""
From the list
['H', 'e', 'l', 'l', 'o', ' ', 'W', 'o', 'r', 'l', 'd']

Generate the following
['o', 'l', 'l']
"""

hello = ['H', 'e', 'l', 'l', 'o', ' ', 'W', 'o', 'r', 'l', 'd']
print(hello[4:1:-1])

"""
Remember it doesn't only work with lists, write your name and
put it in reverse
"""

name = "Esteban Solorzano"
print(name[::-1])