# Q.20. Write a Python program to filter for numbers in a given list whose sum of digits is > 0,
# where the first digit can be negative.
# Input:
# [11, -6, -103, -200]
# Output:
# [11, -103]
# Input:
# [1, 7, -4, 4, -9, 2]
# Output:
# [1, 7, 4, 2]
# Input:
# [10, -11, -71, -13, 14, -32]
# Output:
# [10, -13, 14]


# Beginner-friendly solution

lst = [11, -6, -103, -200]

result = []

for num in lst:

    total = 0
    s = str(num)

    if s[0] == '-':
        total = total - int(s[1])

        for i in range(2, len(s)):
            total = total + int(s[i])

    else:
        for digit in s:
            total = total + int(digit)

    if total > 0:
        result.append(num)

print(result)

# Using enumerate()

lst = [11, -6, -103, -200]

result = []

for num in lst:
    digits = str(num)

    total = 0

    for i, digit in enumerate(digits):
        if digit == '-':
            continue

        if i == 1 and digits[0] == '-':
            total -= int(digit)
        else:
            total += int(digit)

    if total > 0:
        result.append(num)

print(result)

#More Compact Solution

def digit_sum(n):
    s = str(n)

    if n < 0:
        return -int(s[1]) + sum(int(d) for d in s[2:])
    else:
        return sum(int(d) for d in s)

lst = [11, -6, -103, -200]

result = [num for num in lst if digit_sum(num) > 0]

print(result)
