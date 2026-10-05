# Q16. Write a Python program to compute the digit distance between two integers. The digit distance
# between two numbers is the absolute value of the difference of those numbers. For example, the
# distance between 3 and -3 on the number line given by the 3 - (-3) = 3 + 3 = 6 units Digit distance of
# 123 and 256 is Since 1 - 2 + 2 - 5 + 3 - 6 = 1 + 3 + 3 = 7

num1 = input("Enter the 1st Number: ")
num2 = input("Enter the 2nd Number: ")

total = 0

for i in range(len(num1)):
    total += abs(int(num1[i]) - int(num2[i]))

print("Digit Distance:", total)


# Better Version Using zip()

num1 = input("Enter the 1st Number: ")
num2 = input("Enter the 2nd Number: ")

total = 0

for d1, d2 in zip(num1, num2):
    total += abs(int(d1) - int(d2))

print("Digit Distance:", total)