# 81. Write a Python program to calculate the average of the numbers a through b (b not included) rounded to the nearest integer, in binary (or -1 if there are no such numbers).
# Input:
# 4 , 7
# Output:
# 0b101
# Input:
# 11 , 19
# Output:
# 0b1110

# Question explanation :

# For the numbers from a to b-1, we need to:
#
# Find the average.
# Round it to the nearest integer.
# Convert the result to binary.
# If there are no numbers in the range (a >= b), return -1.

a = int(input("Enter the number: "))
b = int(input("Enter the number: "))

if a >=b:
    print(-1)
else:
    avg = round(sum(range(a,b))/len(range(a,b)))
    print(bin(avg))

# Beginner-Friendly Version

a = int(input("Enter a: "))
b = int(input("Enter b: "))

if a >= b:
    print(-1)
else:
    total = 0
    count = 0

    for i in range(a, b):
        total += i
        count += 1

    average = round(total / count)

    print(bin(average))