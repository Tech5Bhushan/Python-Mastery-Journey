# Q69. Write a Python program to print the following integers with '*' to the right of the specified width.

# Solution Using f-string

num = int(input("Enter a number: "))
width = int(input("Enter the width: "))

print(f"{num:*<{width}}")


# Alternative Using format()

num = 123

print(format(num, "*<10"))

# means:
#
# * → fill character
#  → left align
# 10 → total width 10