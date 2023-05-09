#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
d = f"{abs(number) % 10 * (number / abs(number)):.0f}"

if d != 0:
    if d < 6:
        print(f"Last digit of {number} is {d} and is less than 6 and not 0")
    else:
        print(f"Last digit of {number} is {d} and is greater than 5")
else:
    print(f"Last digit of {number} is 0 and is 0")
