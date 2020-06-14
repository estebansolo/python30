"""
Using the range function, create a sequence of numbers
from 1 to 100, and using the filter function return only
those that are multiplies of 2.
"""

def multiple(number):
    return number % 2 == 0

numbers = range(1, 101)
print(list(filter(multiple, numbers)))

"""
According to the example of older users, take the same
list of users or create your own and return those who
are underage.
"""

users = [
    {
        "name": "Esteban",
        "age": 26
    },
    {
        "name": "Jose",
        "age": 15
    },
    {
        "name": "Jaime",
        "age": 18
    }
]

def validate_age(user):
    return user["age"] < 18

print(list(filter(validate_age, users)))

"""
Create a new list of numbers in this case from -10 to
10 and return only those that are multiples of 3 and
negative.
"""

def negative_multiple(number):
    return number % 3 == 0 and number < 0

numbers = range(-10, 10)
print(list(filter(negative_multiple, numbers)))