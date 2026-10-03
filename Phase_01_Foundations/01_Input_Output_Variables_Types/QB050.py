# Q50. Write a Python program to count the number of equal numbers from three given integers.

a = input("Enter the 1st number: ")
b = input("Enter the 2nd number: ")
c = input("Enter the 3rd number: ")

if a == b == c:
    print("The count of equal number is:",3)
elif a ==b or b==c or a==c:
    print("The count of equal number is:",2)
else:
    print("The count of equal number is:",0)


# Shorter Solution:

a, b, c = map(int, input("Enter three integers: ").split())

if a == b == c:
    print("The count of equal number is:",3)
elif a == b or b == c or a == c:
    print("The count of equal number is:",2)
else:
    print("The count of equal number is:",0)