"""
Create a list of 5 names and use the enumerate function to
display them as follows:

1. Name One
2. Name Two
...
5. Name Five
"""

names = ["Juan", "Jose", "Daniela", "Mario", "Luis"]
for index, name in enumerate(names, 1):
    print(f"{index}. {name}")

"""
Use the enumerate function on a string (your name) and print
each character with its corresponding index
"""

for index, char in enumerate("Esteban"):
    print(index, char)