# Q59. Write a Python program to find the biggest even number between two numbers inclusive.

num1 = int(input("Enter the number1: "))
num2 = int(input("Enter the number2: "))

big = None

for i in range(num1,num2+1):
    if i % 2 == 0:
        if big is None or i > big:
            big = i

if big is not None:
    print("The biggest even number is:",big)
else:
    print("There are no even numbers")