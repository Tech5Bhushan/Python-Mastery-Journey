# Q2. Write a Python program to sum the first n positive integers.

n = int(input("Enter the number: "))
if n > 0:
    total = 0
    for num in range(1,n+1):
        total = total + num

    print(total)
else:
    print("Please, Enter the Positive Number.")


# Pythonic Version

n = int(input("Enter the number: "))

if n > 0:
    print(sum(range(1,n+1)))
else:
    print("Please, Enter the Positive Number.")


# Mathematical Formula Version (Best for Interviews)

# The sum of the first n positive integers is:
#
# (n(n+1))/2

n = int(input("Enter the number: "))

if n > 0:
    print(n * (n + 1) // 2)
else:
    print("Please enter a positive number.")

# Remember 0 is NOT a Positive Integer