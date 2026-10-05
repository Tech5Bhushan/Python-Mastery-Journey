# Q14. Write a Python program to compute the amount of debt in n months. Each month, the loan adds
# 5% interest to the $100,000 debt and rounds to the nearest 1,000 above

import math

n = int(input("Enter number of months: "))

debt = 100000

for i in range(n):
    debt = debt * 1.05
    debt = math.ceil(debt / 1000) * 1000

print("Debt after", n, "months:", int(debt))


# How math.ceil() works
# math.ceil(110250 / 1000) gives math.ceil(110.25) = 111 Then 111 * 1000 = 111000