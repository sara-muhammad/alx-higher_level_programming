#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
s = abs(number) % 10
if s > 5:
    print(f"last digit of {number} is {s} and is greater than 5")
elif s == 0:
    print(f"last digit of {number} is {s} and is 0")
elif s < 5 and s != 0:
    print(f"last digit of {number} is {s} and is less than 6 and not 0")
