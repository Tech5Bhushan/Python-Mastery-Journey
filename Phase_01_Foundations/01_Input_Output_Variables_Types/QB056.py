# Q56. Write a Python program to compute the product of the odd digits in a given number, or 0 if there
# aren't any.

num = input("Enter the number: ")

mul = 1
odd_found = False

for digit in num:
    if int(digit) % 2 != 0:
        mul *= int(digit)
        odd_found = True
if odd_found:
    print("The multiplication of odd digits is:", mul)
else:
    print("0")