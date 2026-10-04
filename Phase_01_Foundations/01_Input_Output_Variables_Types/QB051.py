# Q51. Write a Python program to check whether a given number is odd or even. A number is called
# Oddish if the sum of all of its digits is odd, and a number is called Evenish if the sum of all of its digits
# is even.

num = input("Enter the Number: ")
total = 0
for digit in num:
    total = total + int(digit)

if total % 2 == 0:
    print("A number is Evenish")
else:
    print("A number is Oddish")

# More Pythonic Version

num1 = input("Enter the number: ")

total1 = sum(int(digit) for digit in num1)

if total1 % 2 == 0:
    print("A number is Evenish")
else:
    print("A number is Oddish")


# One-Liner Version

num2 = input("Enter the number: ")

print("Evenish" if sum(int(d) for d in num2) % 2 == 0 else "Oddish")