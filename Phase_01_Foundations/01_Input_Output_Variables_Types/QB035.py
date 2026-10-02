# Q35. Write a Python program to convert true to 1 and false to 0.

print(int(True))
print(int(False))

# Explanation
# In Python, True and False are boolean values.
# Internally:
# True = 1
# False = 0
# The int() function converts a boolean value to its integer equivalent.
#
#
# Although bool is a separate data type, it is a subclass of int, which is why:
#
# print(True + True)
# print(False + True)
# Output will be
# 2
# 1