# Q68. Write a Python program to print the following positive and negative numbers with no decimal
# places.

# Solution (Using f-string)
num = float(input("Enter the number: "))
print(f"{num:.0f}")

# Alternative Using format()

num1 = float(input("Enter the number: "))
print(format(num,".0f"))


# Alternative Using %

num2 = float(input("Enter the number: "))
print("%.0f" % num)

# means:
#
# f → floating-point format
# .0 → display 0 digits after the decimal point