# Q23. Write a Python program to swap two variables.

a = 10
b = 20

a,b = b,a
print("a=",a,"b=",b)

# Solution 2: Using a Temporary Variable

a = 10
b = 20

temp = a
a = b
b = temp

print("a =", a)
print("b =", b)

# Solution 3: User Input

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

a, b = b, a

print("After swapping:")
print("a =", a)
print("b =", b)


# Q: Why is a, b = b, a preferred in Python?
#
# Because:
#
# No extra variable is required.
# Code is shorter and cleaner.
# It is the standard Pythonic approach.