"""
Use for/else or while/else to validate all numbers in a
list and print out whether or not there is an even number.
"""

numbers = [41, 7, 9, 13]
for number in numbers:
    if number % 2 == 0:
        print(number, "is even")
        break
else:
    print("No even number in the list")

"""
Create a random number from 1 to 10 and by using a for/else
or while/else allow the user to enter their options, win if
the user guess it, lose after 3 attempts.
"""

import random

loop = 3
random_number = random.randint(1, 10)

while loop > 0:
    guess = int(input("Guess the number:"))
    if guess == random_number:
        print("You win")
        break
        
    loop -= 1
else:
    print("You lose, the number is", random_number)
