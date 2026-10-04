# Q70. Write a Python program to display a number with a comma separator.


# Using f-string

num = int(input("Enter the number: "))
print(f"{num:,}")

# Alternative Using format()

num1 = int(input("Enter the number: "))
print(format(num1,","))


# Alternative for Float Numbers

num2 = 12345.54646
print(f"{num2:,.2f}")


# Explanation
# The format specifier: , adds commas as thousands separators.