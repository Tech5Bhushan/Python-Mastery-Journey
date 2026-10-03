# Q49. Write a Python program to test whether a given number is symmetrical or not. A number is
# symmetrical when it is equal to its reverse. A number is symmetrical when it is equal of its reverse.

num = input("Enter the number: ")

if num == num[::-1]:
    print("The number is SYMMETRICAL")
else:
    print("The number is NOT SYMMETRICAL")

# Alternate Solution - without slicing

num1 = input("Enter the number: ")

reverse = ""

for digit in num1:
    reverse = digit + reverse
    print(reverse)
if num1 == reverse:
    print("The number is SYMMETRICAL")
else:
    print("The number is NOT Symmetrical")

