"""
Create a function that receives N numbers and returns
each of these multiplied by 2
"""

def multiply_by_two(*nums):
    totals = []
    for num in nums:
        totals.append(num * 2)

    return totals

numbers = multiply_by_two(5, 9, 6, 3, 8, 15, 8, 6, 23, 1)
print(numbers)

numbers = multiply_by_two(5, 85, 9)
print(numbers)

"""
Create a function that receives N arguments with your
personal information: name, age, phone, country, etc

Then print those values with their names
"""

def personal_information(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

personal_information(
    name="Esteban",
    lastname="Solorzano",
    age=26,
    country="Colombia"
)

"""
The Python print function receives positional arguments
and named arguments, the named arguments are used to alter
the way this print works:

sep = It indicates how all the values we pass will be separated
end = Indicates what you will put at the end of printing

Default Values:
sep = " "
end = "\n"
"""

config = {"sep": "**", "end": "\nThis is the end"}
values = ["Hello", "World", "This", "Is", "Esteban"]

print(*values, **config)