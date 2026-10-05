# Q22. Write a Python program to print the square and cube symbols in the area of a rectangle and the volume of a cylinder.
# Sample output:
# The area of the rectangle is 1256.66cm2
# The volume of the cylinder is 1254.725cm3

# --> To display square (²) and cube (³) symbols, you can use Unicode characters.

area = 1256.66
volume = 1254.725

print(f"The area of the rectangle is {area}cm\u00B2")
print(f"The volume of the cylinder is {volume}cm\u00B3")