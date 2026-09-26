# Q10. Write a Python program to sum two given integers. However, if the sum is between 15 and 20 it
# will return 20.

num1 = int(input("Enter the 1st number: "))
num2 = int(input("Enter the 2nd number: "))

addition = num1 + num2

if 15 < addition < 20:
    print("20")
else:
    print("The entered number is either less than 15 or more than 20")

#Alternate solution

def sum_or_20(a,b):
    total = a+b
    return 20 if 15 < total < 20 else total

print(sum_or_20(8,9))