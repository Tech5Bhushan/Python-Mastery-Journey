# Q27. Write a Python program that inputs a number and generates an error message if it is not a
# number.

try:
    num = int(input("Enter the number: "))
    print(num)
except ValueError:
    print("Invalid Number")