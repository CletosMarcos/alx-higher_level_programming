#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
sentnc = ""

if (number < 0):
    ld = (number * -1) % 10
else:
    ld = number % 10

if (ld > 5):
    sentnc = "and is greater than 5"
elif (ld == 0):
    sentnc = "and is 0"
else:
    sentnc = "and is less than 6 and not 0"

print(f"Last digit of {number} is {ld} {sentnc}")
