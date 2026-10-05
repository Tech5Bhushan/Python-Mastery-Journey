# Q5. Write a Python program to sum three given integers. However, if two values are equal, the sum will
# be zero.

a=int(input("Enter the 1st number: "))
b=int(input("Enter the 2nd number: "))
c=int(input("Enter the 3rd number: "))

if a==b or b==c or a==c:
    print("The sum is: 0")
else:
    print("The actual sum is: ",a+b+c)


# More Pythonic Version

a=int(input("Enter the 1st number: "))
b=int(input("Enter the 2nd number: "))
c=int(input("Enter the 3rd number: "))

print(0 if a==b or b==c or a==c else a+b+c)