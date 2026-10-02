# Q36. Write a Python program to convert an integer to binary that keeps leading zeros.

# SOLUTION1 : USING format()

a = 7
binary = format(a,'08b')
print(binary)

# Explanation
# '08b' means:
# 0 → pad with zeros
# 8 → total width of 8 digits
# b → binary format
#
# So the binary representation of 7 (111) becomes 00000111.

# Solution 2: Using bin() and zfill()

b = 7
binary_1 = bin(b)[2:].zfill(8)
print(binary_1)

# Explanation
# bin(7) returns '0b111'
# [2:] removes the 0b prefix
# zfill(8) adds leading zeros until the length becomes 8


# Interview Note
# bin(n) → Binary with 0b prefix.
# format(n, '08b') → Binary with leading zeros.
# zfill() → Pads zeros on the left side of a string.
#
# Topic: Numbers and Arithmetic → Number Systems → Binary Conversion → String Formatting