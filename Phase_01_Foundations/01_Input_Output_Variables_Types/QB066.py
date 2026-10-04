# Q66. Write a Python program to print the following numbers up to 2 decimal places


# Correct Solution 1: Using format()

num = float(input("Enter the number: "))

print(format(num,".2f"))

#Correct Solution 2: Using f-strings (Recommended)

num1 = float(input("Enter the number: "))

print(f"{num1:.2f}")

# Correct Solution 3: Using % Formatting

num2 = float(input("Enter a number: "))

print("%.2f" % num1)

# .2 → show 2 digits after the decimal point
# f → floating-point format

