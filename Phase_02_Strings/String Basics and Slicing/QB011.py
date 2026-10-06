# Q11. Write a Python program that returns a string that is n (non-negative integer) copies of a given
# string.

name = "Bhushan"

n = int(input("Enter number of copies: "))

if n >= 0:
    print(name * n)
else:
    print("Please enter a non-negative integer.")

