# Q52. Write a Python program that takes three integers and checks whether the sum of the last digit of
# the first number and the last digit of the second number equals the last digit of the third number.

a = input("Enter the 1st number: ")
b = input("Enter the 2nd number: ")
c = input("Enter the 3rd number: ")

if (int(a[-1]) + int(b[-1])) % 10 == int(c[-1]):
    print("The sum of the last digit of the first number and the last digit of the second number equals the last digit of the third number")
else:
    print("NOT EQUAL")


# Alternate solution :


a = int(input("Enter the 1st number: "))
b = int(input("Enter the 2nd number: "))
c = int(input("Enter the 3rd number: "))

if ((a % 10) + (b % 10)) % 10 == (c % 10):
    print("Equal")
else:
    print("Not Equal")