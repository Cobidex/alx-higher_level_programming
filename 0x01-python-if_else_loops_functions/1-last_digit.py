#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    remain = int(number % -10)
else:
    remain = int(number % 10)
if remain > 5:
    print(f"Last digit of {number} is {remain} and is greater than 5")
elif remain == 0:
    print(f"Last digit of {number} is {remain} and is 0")
elif (remain < 6) and (not 0):
    print(f"Last digit of {number} is {remain} and is less than 6 and not 0")
