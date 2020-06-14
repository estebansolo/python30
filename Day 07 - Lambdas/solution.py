"""
Try using lasmbda functions with the challenges of
map, filter and reduce.
"""

"""
Map
"""

numbers = range(1, 21)
print(list(map(lambda number: number % 2 == 0, numbers)))

a = [1, 5, 6]
b = [3, 5, 9]
print(list(map(lambda num_a, num_b: num_a + num_b, a, b)))

list_of_lists = [
    [1, 2, 3],
    [9, 6, 1],
    [7, 9, 10]
]
print(list(map(lambda numbers: round(sum(numbers) / len(numbers), 2), list_of_lists)))

"""
Filter
"""

numbers = range(1, 101)
print(list(filter(lambda number: number % 2 == 0, numbers)))


users = [
    {"name": "Esteban", "age": 26},
    {"name": "Jose", "age": 15},
    {"name": "Jaime", "age": 18}
]

print(list(filter(lambda user: user["age"] < 18, users)))


numbers = range(-10, 10)
print(list(filter(lambda number: number % 3 == 0 and number < 0, numbers)))

"""
Reduce
"""

from functools import reduce

numbers = [5, 9, 7, 84, 15, 36, 2]
print(reduce(lambda number_a, number_b: number_a * number_b, numbers))


words = ["Hello", "World", "In", "Python"]
print(reduce(lambda word_a, word_b: (len(word_a) if isinstance(word_a, str) else word_a) + len(word_b), words))


numbers = [5, 9, 18, 3, 2]
print(reduce(lambda num_a, num_b: num_a if num_a > num_b else num_b, numbers))