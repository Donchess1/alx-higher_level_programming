#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
a = abs(number) % 10
if number < 0:
    a = -a
print(f"Last digit of {number} is {a} and is ", end ="")
if a > 5:
    print("greater than 5")
elif a == 0:
    print("0")
else:
    print("less than 6 and not 0")
