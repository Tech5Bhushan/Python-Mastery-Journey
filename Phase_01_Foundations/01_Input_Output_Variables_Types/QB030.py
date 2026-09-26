# Q30. Write a Python program to check whether multiple variables have the same value.

a = 5
b = 5
c = 5

if a == b == c:
    print("ALL VARIABLES HAVE THE SAME VALUE")
else:
    print("Variables contain different values")

# FOR MULTIPLE VARIABLES (MORE THAN 3)
#Using set

a = 10
b = 7
c = 8
d = 10

if len({a,b,c,d}) == 1:
    print("ALL VARIABLES HAVE THE SAME VALUE")
else:
    print("Variables contain different values")

# Explanation:

# A set stores only unique values.
#
# Example:
# a = b = c = d = 10
#
# print({a, b, c, d})
# Output:
# {10}
# Since there is only one unique value:
# len({a, b, c, d}) == 1
# returns:
# True