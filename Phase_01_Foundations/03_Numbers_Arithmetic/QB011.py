# Q11. Write a Python program to calculate sum of digits of a number.

num = input("Enter the number: ")
total = 0
for digit in num:
    total += int(digit)

print("sum of digits of a number: ", total )


# Alternate Method

num = input("Enter the number: ")
print(sum(int(digit) for digit in num))

# Small Improvement
#
# If negative numbers might be entered:

num = input("Enter the number: ").strip('-')
total = 0

for digit in num:
    total += int(digit)

print("sum of digits of a number:", total)