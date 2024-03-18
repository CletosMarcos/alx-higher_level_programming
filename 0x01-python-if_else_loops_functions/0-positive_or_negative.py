#!/usr/bin/python3
import random
number = random.randint(-10, 10)
pos_neg = ""

if (number > 0):
    pos_neg = "is positive"
elif (number == 0):
    pos_neg = "is zero"
else:
    pos_neg = "is negative"

print(f"{number} {pos_neg}")
