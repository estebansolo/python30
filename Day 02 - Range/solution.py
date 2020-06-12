"""
Generate a sequence using the function range that
returns the following.

[-100, -90, -80, -70, -60, -50, -40, -30, -20, -10, 0,
10, 20, 30, 40, 50, 60, 70, 80, 90]
"""

print(list(range(-100, 100, 10)))

"""
Generate the previous sequence but in this case in
the opposite way.
"""

print(list(range(90, -110, -10)))

"""
This challenge can be a bit difficult, try to create a
function that returns a sequence of decimal numbers between
2 numbers, incremental only.

Here's a hint, use the while statement
"""

def floating_range(start, stop, step):
    numbers = []
    last_number = start

    while last_number < stop:
        numbers.append(last_number)
        last_number += step
        last_number = round(last_number, 2)

    return numbers


print(floating_range(0.5, 2.5, 0.5))
print(floating_range(0.5, 2.5, 0.2))

# Floating Point Arithmetic: Issues and Limitations
# https://docs.python.org/3/tutorial/floatingpoint.html