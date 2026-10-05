# Q12. Write a Python program to calculate the midpoints of a line

# Formula :
# To calculate the midpoint of a line joining two points (x1,y1)(x_1, y_1)(x1,y1) and (x2,y2)(x_2, y_2)(x2,y2), use:
# Midpoint=((X1+X2/2),((Y1+Y2)/2))

x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))

x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))

mid_x = (x1 + x2) / 2
mid_y = (y1 + y2) / 2

print("Midpoint of the line is:", (mid_x, mid_y))