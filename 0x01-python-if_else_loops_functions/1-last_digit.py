#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    last_number = (-1 * number) % 10
else:
    last_number = number % 10

if last_number < 5:
    print(f"Last digit of {number:d} is {last_number} and is less than 6 and not 0")
elif last_number > 5:
    print(f"Last digit of {number:d} is {last_number} and is greater than 5")
else:
    print(f"Last digit of {number:d} is {last_number} and is 0")
