# Q4. Write a Python program to compute the future value of a specified principal amount, rate of
# interest, and number of years.

# The formula for Future Value (Compound Interest) is:
# FV=P×(1+r)**t

# Where:
# P = Principal amount
# r = Annual interest rate (in decimal form)
# t = Number of years


principal = float(input("Ether the Principal amount: "))
rate = float(input("Enter the rate of interest: "))
years = int(input("Enter the number of years: "))

future_value = principal * (1+rate/100) ** years

print("Future Value: ", round(future_value,2))


# Using f-string

principal = float(input("Ether the Principal amount: "))
rate = float(input("Enter the rate of interest: "))
years = int(input("Enter the number of years: "))

fv = principal * (1 + rate / 100) ** years

print(f"Future Value is: {fv:.2f}")
