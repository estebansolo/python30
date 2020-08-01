"""
Use try/except to catch an error, you can try to validate
what happens when we do

my_list = ["a", "b", "c"]
print(my_list[10])
"""

try:
    my_list = ["a", "b", "c"]
    print(my_list[10])
except IndexError as err:
    print(err)

"""
Cause an exception to be raised using the raise keyword and
print a message after you have finished catching the error
at finally.
"""

try:
    raise ZeroDivisionError
except ZeroDivisionError:
    print("Error Zero Division")
finally:
    print("Finally")

"""
Use input function to request information to the user and in
the try/except structure catches multiple errors that can be
generated
"""

try:
    divisor = int(input("Divisor: "))
    calculate = 5 / divisor
except (ValueError, ZeroDivisionError) as err:
    print("Error:", err)