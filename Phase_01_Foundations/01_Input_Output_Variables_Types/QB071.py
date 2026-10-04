# Q71. Write a Python program to format a number with a percentage

# Using f-string

num = float(input("Enter the number :"))
print(f"{num:.2%}")

#Alternative Using format()

num1 = float(input("Enter the number: "))
print(format(num1,".2%"))

# Explanation
# The format specifier:
# :.2%
# means:
# % → multiply by 100 and append %
# .2 → show 2 digits after the decimal point