# Q44. Write a Python program which solve the equation ax+by=c dx+ey=f Print the values of x, y where
# a, b, c, d, e and f are given.


# Solution using Cramer’s Rule :

a = float(input("Enter number a: "))
b = float(input("Enter number b: "))
c = float(input("Enter number c: "))
d = float(input("Enter number d: "))
e = float(input("Enter number e: "))
f = float(input("Enter number f: "))

determinant = (a * e) - (b * d)

if determinant == 0:
    print("The equations do not have a unique solution.")
else:
    x = (c * e) - (b * f) / determinant
    y = (a * f) - (c * d) / determinant

    print("x = ",x)
    print("y = ",y)