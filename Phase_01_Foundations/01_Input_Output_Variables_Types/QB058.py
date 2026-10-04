# Q58. Write a Python program to find an integer exponent x such that a^x = n.

# Solution Using a Loop

a = int(input("Enter the value: "))
n = int(input("Enter the value: "))
x = 0
while a**x != n:
    x = x + 1

print("The value of x is",x)