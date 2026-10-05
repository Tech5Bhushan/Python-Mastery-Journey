# Q1. Write a Python program to test whether a number is within 100 of 1000 or 2000.

num = int(input("Enter the number: "))

if abs(1000-num) <= 100 or abs(2000-num) <= 200:
    print(True)
else:
    print(False)

# The abs() function in Python is a built-in tool that returns the absolute value of a number.
# It strips away any negative sign, providing the non-negative magnitude or the number's total distance from zero on a number line.
