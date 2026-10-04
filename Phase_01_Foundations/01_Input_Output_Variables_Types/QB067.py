# Q67. Write a Python program to print the following numbers up to 2 decimal places with a sign.

# Solution (Using f-string)

num = float(input("Enter the number: "))
print(f"{num:+.2f}")

# Alternative Solution Using %

num1 = float(input("Enter the number: "))
print("%+.2f" %num1)


# + → always display the sign
# .2 → show 2 digits after the decimal point
# f → floating-point format