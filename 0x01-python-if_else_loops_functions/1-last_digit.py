#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    last_number = (-1 * number) % 10
    last_number *= -1
elif number >= 0:
    last_number = number % 10

message = f"Last digit of {number} is {last_number}"

if last_number == 0:
    print(f"{message} and is 0")
elif last_number < 5:
    print(f"{message} and is less than 6 and not 0")
elif last_number > 5:
    print(f"{message} and is greater than 5")
