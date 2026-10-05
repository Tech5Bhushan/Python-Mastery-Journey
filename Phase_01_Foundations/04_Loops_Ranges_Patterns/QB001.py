# Q1. Write a Python program to generate a number in a specified range except some specific numbers.
# Generate a number in a specified range (1, 10) except [2, 9, 10]
# 7
# Generate a number in a specified range (-5, 5) except [-5,0,4,3,2]
# -4

# Solution
#
# The idea is:
#
# Generate numbers within the given range.
# Exclude the specified numbers.
# Pick a valid number from the remaining numbers.

import random

lst = [2, 9, 10]
e_lst = []
for i in range(1,11):
    if i not in lst:
        e_lst.append(i)
print(random.choice(e_lst))
