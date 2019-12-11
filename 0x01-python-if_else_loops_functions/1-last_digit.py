#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
intro = "Last digit of "
if number < 0:
    digit = number % -10
else:
    digit = number % 10
if digit > 5:
    print("{}{} is {} and is greater than 5".format(intro, number, digit))
elif digit == 0:
    print("{}{} is {} and is 0".format(intro, number, digit))
elif digit < 6:
    print("{}{} is {} and is less than 6 and not 0".format(intro, number, digit))
